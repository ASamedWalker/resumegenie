"use client"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Upload } from "lucide-react"

const UploadPDF = () => {
  return (
    <Dialog>
      <DialogTrigger asChild>
      <Button variant="orange">
            <Upload
              size={20}
              className="w-4 h-4 mr-2"
              style={{ strokeWidth: "3" }}
            />
            Upload
          </Button>
      </DialogTrigger>


      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Upload a document</DialogTitle>
        </DialogHeader>

        {/* form */}
        <form className="space-y-4">
          <div className="flex items-center">
            <div className="flex-grow border-t border-gray-200"></div>
              <span className="flex-shrink mx-4 uppercase text-gray-600 text-xs">
                or
              </span>

              <div className="flex-grow border-t border-gray-200"></div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="url">
              Import from URL
            </Label>
            <Input id="url" name="url" className="font-light" placeholder="https://cdn.openai.com/papers/gpt-4.pdf"/>
          </div>

          <div>
            <Button variant="orange" type="submit">
              Upload
            </Button>
            <DialogTrigger asChild>
              <Button variant="light">Cancel</Button>
            </DialogTrigger>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  )
}

export default UploadPDF;