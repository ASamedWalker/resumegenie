// app/actions/uploadPDF.ts
'use server'

import { storage } from '@/lib/firebaseConfig';
import { ref, uploadString, getDownloadURL } from 'firebase/storage';

export const uploadFile = async (fileData: { name: string, type: string, base64: string } | null, url: string | null) => {
  if (fileData) {
    const { name, type, base64 } = fileData;
    const timestamp = Date.now();
    const fileName = `${timestamp}_${name}`;
    const storageRef = ref(storage, `uploads/${fileName}`);
    try {
      const snapshot = await uploadString(storageRef, base64, 'data_url');
      const downloadURL = await getDownloadURL(snapshot.ref);
      return { success: true, downloadURL };
    } catch (error) {
      console.error("Error uploading file:", error);
      let errorMessage = 'Failed to upload file';
      if (error instanceof Error) {
        errorMessage += `: ${error.message}`;
      }
      return { success: false, error: errorMessage };
    }
  } else if (url) {
    // Here you might want to download the file from the URL and then upload it to Firebase
    // For simplicity, we'll just return the URL
    return { success: true, downloadURL: url };
  } else {
    return { success: false, error: 'No file or URL provided' };
  }
};