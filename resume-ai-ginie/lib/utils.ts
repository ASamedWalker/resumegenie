import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge";
import { toast } from "react-toastify";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getPDFFileNameFromURL(url: string) {
  const matches = url.match(/\/([^/?#]+)[^/]*$/);

  if (matches && matches.length > 1) {
    const fileNameWithExtension = matches[1];
    const fileExtension = fileNameWithExtension.split('.').pop();

    if (fileExtension?.toLowerCase() === 'pdf') {
      return fileNameWithExtension;
    }
  }

  // Return null if the URL does not end with a PDF file
  return null;
}


export function showToast(message: string, type: "success" | "warn" | "error") {
  toast(message, {
    position: type === "error" ? "top-center" : "top-right",
    className: "foo-bar",
  });
}