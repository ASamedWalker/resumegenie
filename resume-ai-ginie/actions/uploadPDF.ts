'use server';

import { adminStorage } from '@/lib/firebaseConfig';
import { auth} from '@clerk/nextjs/server';
import { Buffer } from 'buffer';

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
    const { userId }: { userId: string | null } = auth()
    if (!userId) {
      throw new Error('User is not authenticated');
    }

    const timestamp = Date.now();
    const fullPath = `uploads/${userId}/${timestamp}_${fileName}`;

    // Remove the base64 prefix (e.g., "data:application/pdf;base64,")
    const base64Data = fileData.split(',')[1];

    // Convert the base64 string to a binary buffer
    const buffer = Buffer.from(base64Data, 'base64');

    // Create a reference to the file in Firebase Storage
    const bucket = adminStorage.bucket();
    const fileRef = bucket.file(fullPath);

    // Upload the buffer to Firebase Storage
    await fileRef.save(buffer, {
      contentType: fileType,
      metadata: {
        firebaseStorageDownloadTokens: userId,
      },
    });

    // Get the download URL
    const [downloadUrl] = await fileRef.getSignedUrl({
      action: 'read',
      expires: Date.now() + 24 * 60 * 60 * 1000, // 24 hours
    });

    return { success: true, downloadUrl };
  } catch (error) {
    console.error('Unexpected error:', error);
    return { success: false, error: 'Unexpected error occurred' };
  }
};
