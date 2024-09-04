"use server";

import { adminStorage } from "@/lib/firebaseConfig";
import { auth } from "@clerk/nextjs/server";
import { Buffer } from "buffer";

interface UploadPDFParams {
  fileName: string;
  fileType: string;
  fileData: string;
}

export const uploadPDF = async ({
  fileName,
  fileType,
  fileData,
}: UploadPDFParams) => {
  try {
    const { userId }: { userId: string | null } = auth();
    if (!userId) {
      throw new Error("User is not authenticated");
    }

    // 1. Generate a unique file name
    const timestamp = Date.now();
    const uniqueFileName = `${timestamp}_${fileName}`;
    const fullPath = `uploads/${userId}/${uniqueFileName}`;

    // 2. Convert base64 data to a buffer
    const base64Data = fileData.split(",")[1];
    const buffer = Buffer.from(base64Data, "base64");

    // 3. Upload to Firebase Storage
    const bucket = adminStorage.bucket();
    const fileRef = bucket.file(fullPath);
    await fileRef.save(buffer, {
      contentType: fileType,
      metadata: {
        firebaseStorageDownloadTokens: userId,
      },
    });

    // 4. Get the download URL
    const [downloadUrl] = await fileRef.getSignedUrl({
      action: "read",
      expires: Date.now() + 24 * 60 * 60 * 1000, // 24 hours
    });

    return { success: true, downloadUrl, fullPath, fileKey: uniqueFileName };
  } catch (error) {
    console.error("Unexpected error during PDF upload:", error);
    if (error instanceof Error) {
      return { success: false, error: error.message };
    }
    return { success: false, error: "Unexpected error occurred during PDF upload" };
  }
};