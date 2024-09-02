// lib/firebaseConfig.ts
import { initializeApp, getApps, cert, App } from "firebase-admin/app";
import { getAuth } from "firebase-admin/auth";
import { getStorage} from "firebase-admin/storage";


const serverConfig = {
  apiKey: process.env.FIREBASE_API_KEY,
  clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
  privateKey: process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n'),
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};


let adminApp;
let adminAuth;
let adminStorage;

if (!getApps().length) {
  adminApp = initializeApp({
    credential: cert(serverConfig),
    storageBucket: serverConfig.storageBucket,
  });
} else {
  adminApp = getApps()[0];
}

adminAuth = getAuth(adminApp);
adminStorage = getStorage(adminApp);

export { adminAuth, adminStorage };