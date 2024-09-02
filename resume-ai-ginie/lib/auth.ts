// lib/auth.ts
import { adminAuth } from './firebaseConfig';
import { getAuth } from "firebase-admin/auth";

export async function generateFirebaseToken(clerkUserId: string) {
  if (!clerkUserId) {
    throw new Error('Clerk user ID is required to generate a Firebase token');
  }

  // Ensure we're on the server side
  if (typeof window !== 'undefined') {
    throw new Error('generateFirebaseToken should only be called on the server side');
  }

  try {
    // If adminAuth is not available, try to get it again
    const auth = adminAuth || getAuth();

    if (!auth) {
      throw new Error('Firebase Admin Auth is not initialized');
    }

    const firebaseToken = await auth.createCustomToken(clerkUserId);

    if (!firebaseToken) {
      throw new Error('Failed to generate Firebase token');
    }

    return firebaseToken;
  } catch (error) {
    console.error('Error generating Firebase token:', error);
    throw error;
  }
}