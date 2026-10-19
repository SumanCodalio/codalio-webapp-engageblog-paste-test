import React from "react";
import { ArrowLeft } from "lucide-react";
import { Button } from "../components/ui/button";
import { useNavigate } from "react-router-dom";

export default function AdminSystemReports() {
  const navigate = useNavigate();
  return (
    <div className="min-h-screen bg-background pb-12 w-full flex flex-col items-center justify-center space-y-4">
      <Button variant="ghost" onClick={() => navigate("/admin")}><ArrowLeft className="mr-2 h-4 w-4" />Back to Admin</Button>
      <h1 className="text-xl font-bold text-foreground">System Reports</h1>
      <p className="text-muted-foreground text-sm">This feature is not yet available.</p>
    </div>
  );
}