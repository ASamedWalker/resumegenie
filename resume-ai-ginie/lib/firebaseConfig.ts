// lib/firebaseConfig.ts
import { initializeApp, getApps, cert, App } from "firebase-admin/app";
import { getFirestore } from "firebase-admin/firestore";
import { getStorage } from "firebase-admin/storage";
import { getAuth as getAdminAuth } from "firebase-admin/auth";

import { initializeApp as initializeClientApp } from "firebase/app";
import { getAuth, signInAnonymously } from "firebase/auth";
import { getFunctions, httpsCallable } from 'firebase/functions';

// Server-side (Admin) configuration
const serverConfig = {
  credential: cert({
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
    clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
    privateKey: process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n'),
  }),
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
};

// Client-side configuration
const clientConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Server-side (Admin) initialization
let adminApp: App;
let adminFirestore;
let adminStorage;
let adminAuth;

if (typeof window === 'undefined') {
  if (!getApps().length) {
    adminApp = initializeApp(serverConfig);
  } else {
    adminApp = getApps()[0];
  }
  adminFirestore = getFirestore(adminApp);
  adminStorage = getStorage(adminApp);
  adminAuth = getAdminAuth(adminApp);
}

// Client-side initialization
let clientApp;
let clientAuth;
let clientFunctions;

if (typeof window !== 'undefined') {
  clientApp = initializeClientApp(clientConfig);
  clientAuth = getAuth(clientApp);
  clientFunctions = getFunctions(clientApp, 'us-central1');
}

// Vector search function
export async function queryVectorIndex(query: string, limit: number = 5, prefilters?: any[]) {
  if (typeof window === 'undefined') {
    throw new Error('Vector search can only be performed on the client side');
  }

  try {
    await signInAnonymously(clientAuth);
    const queryCallable = httpsCallable(clientFunctions, 'ext-firestore-vector-search-queryCallable');
    const result = await queryCallable({
      query,
      limit,
      prefilters
    });
    return result.data;
  } catch (error) {
    console.error('Error querying vector index:', error);
    throw error;
  }
}

export {
  adminApp,
  adminFirestore,
  adminStorage,
  adminAuth,
  clientApp,
  clientAuth,
  clientFunctions
};