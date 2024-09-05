"use client";
import { useCallback, useState, useTransition } from "react";
import { useDropzone } from "react-dropzone";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Loader2, Upload, UploadCloud, X } from "lucide-react";
import { uploadPDF } from "@/actions/uploadPDF";
import { processAndStoreEmbeddings } from "@/actions/uploadToFirestore";
import { getPDFFileNameFromURL } from "@/lib/utils";
import { showToast } from "@/lib/utils";

const CORS_PROXY = "https://corsproxy.io/?";

const UploadPDF = () => {
  const [file, setFile] = useState<File | null>(null);
  const [url, setUrl] = useState<string>("");
  const [isButtonEnabled, setIsButtonEnabled] = useState<boolean>(false);
  const [open, setOpen] = useState(false);
  const [isPending, startTransition] = useTransition();
  const [isLoading, setIsLoading] = useState(false);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const pdfFile = acceptedFiles[0];
    if (!pdfFile) {
      alert("Please upload only PDF file");
      return;
    }
    if (pdfFile.size > 10 * 1024 * 1024) {
      alert("File size should not exceed 5MB");
      return;
    }

    setFile(pdfFile);
    setIsButtonEnabled(true);
    setUrl("");
  }, []);

  const { getRootProps, getInputProps } = useDropzone({
    accept: { "application/pdf": [".pdf"] },
    multiple: false,
    onDrop,
  });

  const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const urlValue = e.target.value;
    setUrl(urlValue);

    const fileName = getPDFFileNameFromURL(urlValue);
    if (fileName) {
      setIsButtonEnabled(true);
      setFile(null); // Clear the file if URL is used
    } else {
      setIsButtonEnabled(false);
    }
  };

  const handleRemoveFile = () => {
    setFile(null);
    setIsButtonEnabled(false);
  };

  const resetForm = () => {
    setFile(null);
    setUrl("");
    setIsButtonEnabled(false);
  };

  const handleOpenDialog = () => {
    setOpen(!open);
    resetForm();
  };

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!file && !url) {
      showToast("Please select a file or enter a URL", "warn");
      return;
    }

    setIsLoading(true);

    startTransition(async () => {
      try {
        let uploadResult;
        let fileKey;

        if (file) {
          const readFileAsBase64 = (file: File): Promise<string> => {
            return new Promise((resolve, reject) => {
              const reader = new FileReader();
              reader.readAsDataURL(file);
              reader.onloadend = () => resolve(reader.result as string);
              reader.onerror = () => reject(new Error("File reading failed"));
            });
          };

          const base64File = await readFileAsBase64(file);

          uploadResult = await uploadPDF({
            fileName: file.name,
            fileType: file.type,
            fileData: base64File,
          });

          if (uploadResult.success) {
            fileKey = uploadResult.fileKey;
          }
        } else if (url) {
          const fileName = getPDFFileNameFromURL(url);

          if (!fileName) {
            showToast("Invalid URL. Please enter a valid PDF URL", "warn");
            setIsLoading(false);
            return;
          }

          const proxyUrl = `${CORS_PROXY}${encodeURIComponent(url)}`;
          const response = await fetch(proxyUrl);
          if (!response.ok) {
            throw new Error("Failed to download PDF from URL");
          }

          const blob = await response.blob();
          const base64File = await new Promise<string>((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(blob);
            reader.onloadend = () => resolve(reader.result as string);
            reader.onerror = reject;
          });

          uploadResult = await uploadPDF({
            fileName,
            fileType: blob.type,
            fileData: base64File,
          });

          if (uploadResult.success) {
            fileKey = uploadResult.fileKey;
          }
        }

        if (!uploadResult || !uploadResult.success || !fileKey) {
          throw new Error(uploadResult?.error || "Upload failed");
        }

        // Generate embeddings using the fileKey
        const embeddingResult = await processAndStoreEmbeddings(fileKey);

        if (embeddingResult.success) {
          showToast(
            "File uploaded and embeddings generated successfully!",
            "success"
          );
          console.log("Embeddings generated and stored successfully");
          console.log(
            `Number of embeddings stored: ${embeddingResult.embeddingsCount}`
          );
          console.log("Full content length:", embeddingResult.fullContent.length);
          console.log("Number of chunks:", embeddingResult.chunks.length);

          // Log a sample of the content (first 500 characters)
          console.log("Sample content from the PDF:");
          console.log(embeddingResult.fullContent.slice(0, 500) + "...");

          // Log the first chunk
          console.log("First chunk:");
          console.log(embeddingResult.chunks[0]);
        } else {
          console.error("Error generating embeddings:", embeddingResult.error);
          showToast(
            `File uploaded, but error generating embeddings: ${embeddingResult.error}`,
            "error"
          );
        }
        setOpen(false);
      } catch (error) {
        console.error("Error in form submission:", error);
        showToast(
          `An unexpected error occurred: ${
            error instanceof Error ? error.message : "Unknown error"
          }`,
          "error"
        );
      } finally {
        setIsLoading(false);
        resetForm();
      }
    });
  };

  return (
    <>
      <Dialog open={open} onOpenChange={handleOpenDialog}>
        <DialogTrigger asChild>
          <Button variant="orange">
            <Upload
              size={20}
              className="w-4 h-4 mr-2"
              style={{ strokeWidth: "3" }}
            />
            Upload
          </Button>
        </DialogTrigger>

        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>Upload a document</DialogTitle>
            <DialogDescription>
              Please select a PDF file to upload. The file should not exceed 5MB
              in size.
            </DialogDescription>
          </DialogHeader>

          {/* form */}
          <form onSubmit={handleFormSubmit} className="space-y-4">
            <div className="bg-white rounded-xl">
              <div className="border-dashed border-2 rounded-md bg-gray-50 h-36 w-full">
                {file ? (
                  <div className="h-full flex justify-center items-center text-black/70">
                    <span className="overflow-hidden whitespace-nowrap text-ellipsis text-sm max-w-[200px]">
                      {file ? file.name : "or click to browse"}
                    </span>
                    <button
                      type="button"
                      onClick={handleRemoveFile}
                      className="ml-2 text-gray-400 cursor-pointer"
                    >
                      <X size={20} className="w-4 h-4" />
                    </button>
                  </div>
                ) : (
                  <div
                    {...getRootProps()}
                    className="flex flex-col items-center justify-center h-full cursor-pointer"
                  >
                    <input name="file" {...getInputProps()} />
                    <UploadCloud
                      size={40}
                      className="text-gray-400 w-10 h-10"
                      style={{ color: "#ff612f" }}
                    />
                    <p className="text-slate-400 text-sm mt-2">
                      Drag and drop a file here
                    </p>
                  </div>
                )}
              </div>
            </div>

            <div className="flex items-center">
              <div className="flex-grow border-t border-gray-200"></div>
              <span className="flex-shrink mx-4 uppercase text-gray-600 text-xs">
                or
              </span>

              <div className="flex-grow border-t border-gray-200"></div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="url">Import from URL</Label>
              <Input
                id="url"
                name="url"
                value={url}
                onChange={handleUrlChange}
                className="font-light"
                placeholder="https://cdn.openai.com/papers/gpt-4.pdf"
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <Button
                variant="orange"
                type="submit"
                disabled={!isButtonEnabled || isLoading}
              >
                {isLoading ? (
                  <Loader2
                    className="h-5 w-5 text-white/80 animate-spin"
                    style={{ strokeWidth: "3" }}
                  />
                ) : (
                  `Upload`
                )}
              </Button>
              <DialogTrigger asChild>
                <Button variant="light">Cancel</Button>
              </DialogTrigger>
            </div>
          </form>
        </DialogContent>
      </Dialog>
    </>
  );
};

export default UploadPDF;
