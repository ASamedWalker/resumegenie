// lib/firebaseConfig.ts
import { initializeApp, getApps, cert, App } from "firebase-admin/app";
import { getFirestore } from "firebase-admin/firestore";
import { getStorage as getAdminStorage } from "firebase-admin/storage";
import { getAuth as getAdminAuth } from "firebase-admin/auth";

import { initializeApp as initializeClientApp } from "firebase/app";
import { getAuth, signInAnonymously } from "firebase/auth";
import { getFunctions, httpsCallable } from 'firebase/functions';
import { getStorage, ref, getDownloadURL } from "firebase/storage";

// Client-side configuration
const clientConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Client-side initialization
const clientApp = initializeClientApp(clientConfig);
const clientAuth = getAuth(clientApp);
const clientFunctions = getFunctions(clientApp, 'us-central1');
const clientStorage = getStorage(clientApp);


// Export client-side Firebase instances and functions
export {
  clientApp,
  clientAuth,
  clientFunctions,
  clientStorage,
  ref,
  getDownloadURL,
};

// Server-side (Admin) configuration and initialization
// This part will only be included in server-side bundles
if (typeof window === 'undefined') {
  const serverConfig = {
    credential: cert({
      projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
      privateKey: process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n'),
    }),
    storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  };

  let adminApp: App;
  if (!getApps().length) {
    adminApp = initializeApp(serverConfig);
  } else {
    adminApp = getApps()[0];
  }

  const adminFirestore = getFirestore(adminApp);
  const adminStorage = getAdminStorage(adminApp);
  const adminAuth = getAdminAuth(adminApp);

  // Export admin SDK instances
  module.exports = {
    ...module.exports,
    adminApp,
    adminFirestore,
    adminStorage,
    adminAuth,
  };
}