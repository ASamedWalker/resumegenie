import { Button } from "@/components/ui/button";
import UploadPDF from "@/components/UploadPDF";
import { create } from "domain";
import { File, Pencil, Trash2, Upload } from "lucide-react";
import Link from "next/link";

const Documents = () => {
  const documents = [
    {
      fileName: "Samed.pdf",
      fileSize: "1 MB",
      createdAt: "3 days ago",
    },
    {
      fileName: "Linda.pdf",
      fileSize: "2 MB",
      createdAt: "5 Weeks ago",
    },
    {
      fileName: "Rishi.pdf",
      fileSize: "6 MB",
      createdAt: "7 days ago",
    },
  ];
  return (
    <section className="bg-[#faf9f6] min-h-screen">
      <div className="section-container">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-4xl font-bold text-[#333]">Documents</h1>
          <UploadPDF />
        </div>

        <div className="bg-white rounded shadow w-full overflow-hidden">
          <table className="min-w-full">
            <tbody>
              {documents.map((document, index) => (
                <tr
                  key={index}
                  className={
                    index === documents.length - 1
                      ? " "
                      : "border-b border-hray-200"
                  }
                >
                  <td className="p-4 text-left flex items-center">
                    <File
                      size={20}
                      className="w-4 h-4 mr-2"
                      style={{ strokeWidth: "3" }}
                    />
                    <Link href="#">
                      <span className="text-ellipsis overflow-hidden whitespace-normal max-w-[300px] text-sm font-medium">
                        {document.fileName}
                      </span>
                    </Link>
                  </td>
                  <td className="p-4 text-right text-sm text-gray-500 whitespace-nowrap w-20">
                    {document.fileSize}
                  </td>
                  <td className="p-4 text-right text-sm text-gray-500 whitespace-nowrap w-20">
                    {document.createdAt}
                  </td>
                  <td className="p-4 text-right w-4">
                    <Pencil
                      size={20}
                      className="w-4 h-4 cursor-pointer"
                      style={{ strokeWidth: "3" }}
                    />
                  </td>
                  <td className="p-4 text-right w-4">
                    <Trash2
                      size={20}
                      className="w-4 h-4 cursor-pointer"
                      style={{ strokeWidth: "3" }}
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
};

export default Documents;
