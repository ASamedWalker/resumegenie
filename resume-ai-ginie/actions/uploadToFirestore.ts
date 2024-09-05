"use server";

import { auth } from "@clerk/nextjs/server";
import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";
import { OpenAIEmbeddings } from "@langchain/openai";
import { supabase } from "@/lib/supabase";
import { adminStorage } from "@/lib/firebaseConfig";


// Function to clean text of invalid characters
function cleanText(text: string): string {
  // Remove null bytes and other control characters
  return text.replace(/[\x00-\x1F\x7F-\x9F]/g, "")
    // Replace Unicode escape sequences with a space
    .replace(/\\u[0-9a-fA-F]{4}/g, " ")
    // Remove any remaining backslashes
    .replace(/\\/g, "");
}

async function batchInsertEmbeddings(
  embeddings,
  userId,
  fileKey,
  chunkContents
) {
  const batchSize = 1000; // Adjust based on your needs
  for (let i = 0; i < embeddings.length; i += batchSize) {
    const batch = embeddings.slice(i, i + batchSize).map((vector, index) => ({
      user_id: userId,
      file_key: fileKey,
      chunk_index: i + index,
      content: cleanText(chunkContents[i + index]),
      embedding: vector,
    }));

    const { error } = await supabase.from("embeddings").upsert(batch, {
      onConflict: "user_id,file_key,chunk_index",
      ignoreDuplicates: false,
    });

    if (error) throw error;
  }
}

export const processAndStoreEmbeddings = async (fileKey: string) => {
  try {
    const { userId }: { userId: string | null } = auth();
    if (!userId) {
      throw new Error("User is not authenticated");
    }

    // Get the file from Firebase Storage
    const bucket = adminStorage.bucket();
    const file = bucket.file(`uploads/${userId}/${fileKey}`);

    // Download the file content
    const [fileContent] = await file.download();

    // Create a Blob from the file content
    const blob = new Blob([fileContent], { type: "application/pdf" });

    // Load and parse the PDF
    const pdfLoader = new PDFLoader(blob);
    const pages = await pdfLoader.load();

    console.log(`Loaded PDF with ${pages.length} pages`);

    // Combine all page content, trim, and split
    const fullText = cleanText(pages
      .map((page) => page.pageContent.trim())
      .join(" ")
      .replace(/\s+/g, " "));

    // Split the text into chunks
    const textSplitter = new RecursiveCharacterTextSplitter({
      chunkSize: 1000,
      chunkOverlap: 200,
    });
    const textChunks = await textSplitter.createDocuments([fullText]);

    console.log(`Split PDF into ${textChunks.length} chunks`);

    // Initialize OpenAI embeddings
    const embeddings = new OpenAIEmbeddings({
      openAIApiKey: process.env.OPENAI_API_KEY,
    });

    // Generate embeddings for each chunk
    const embeddingVectors = await embeddings.embedDocuments(
      textChunks.map(chunk => chunk.pageContent)
    );

    // Store embeddings in Supabase using batch insertion
    await batchInsertEmbeddings(
      embeddingVectors,
      userId,
      fileKey,
      textChunks.map(chunk => chunk.pageContent)
    );

    console.log(`Stored ${embeddingVectors.length} embeddings in Supabase`);

    return {
      success: true,
      message: "PDF processed and embeddings stored in Supabase",
      fullContent: fullText,  // Return the full content instead of a sample
      embeddingsCount: embeddingVectors.length,
      chunks: textChunks.map(chunk => chunk.pageContent),  // Return all chunks
    };
  } catch (error) {
    console.error("Error in processAndStoreEmbeddings:", error);
    return {
      success: false,
      error:
        error instanceof Error ? error.message : "An unexpected error occurred",
    };
  }
};