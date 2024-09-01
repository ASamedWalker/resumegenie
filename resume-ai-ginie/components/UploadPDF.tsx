"use client";
import { useCallback, useState } from "react";
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
import { Upload, UploadCloud, X } from "lucide-react";

const UploadPDF = () => {
  const [file, setFile] = useState<File | null>(null);
  const [url, setUrl] = useState<string>("");
  const [isButtonEnabled, setisButtonEnabled] = useState<boolean>(false);

  const [open, setOpen] = useState(false);

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
    setisButtonEnabled(true);
    setUrl("");
  }, []);

  const { getRootProps, getInputProps } = useDropzone({
    accept: { "application/pdf": [".pdf"] },
    multiple: false,
    onDrop,
  });

  const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
    setFile(null);
    setisButtonEnabled(e.target.value.length > 0);
  };

  const handleRemoveFile = () => {
    setFile(null);
    setisButtonEnabled(false);
  }

  const resetForm = () => {
    setFile(null);
    setUrl("");
    setisButtonEnabled(false);
  };

  const handleOpenDialog = () => {
    setOpen(!open);
    resetForm();
  }

  const handleFormSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (file) {
      alert("File uploaded successfully");
      console.log(file);
      resetForm();
      setOpen(false);
    } else if (url) {
      alert("File uploaded successfully");
      console.log(url);
      resetForm();
      setOpen(false);
    } else {
      alert("Please upload a file or enter a URL");
    }
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
                      className="ml-2 text-gray-400 cursor-pointer">
                      <X size={20} className="w-4 h-4"/>
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
                disabled={!isButtonEnabled}
              >
                Upload
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
