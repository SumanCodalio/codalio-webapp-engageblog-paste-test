import { useState, useEffect } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import { useAcceptInvitation } from "@rhino-dev/rhino-react";
import { Layers } from "lucide-react";
import { Button } from "../components/ui/button";

export default function AcceptInvitation() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const token = searchParams.get("token");
  const accept = useAcceptInvitation();
  const [status, setStatus] = useState<"loading" | "invalid" | "error" | "success">("loading");

  useEffect(() => {
    if (!token) {
      setStatus("invalid");
      return;
    }
    accept.mutate(token, {
      onSuccess: (result) => {
        setStatus("success");
        setTimeout(() => navigate(`/`), 2000);
      },
      onError: () => setStatus("error"),
    });
  }, [token]);

  return (
    <div className="min-h-screen bg-background w-full min-w-0 overflow-x-hidden">
      <div className="flex items-center justify-center min-h-[85vh] px-4 w-full min-w-0">
        <div className="max-w-md mx-auto my-12 bg-card border border-border shadow-xl rounded-2xl p-6 sm:p-8 space-y-6 text-center">
          <div className="mx-auto w-12 h-12 rounded-xl bg-primary text-primary-foreground flex items-center justify-center shadow-md shadow-primary/30">
            <Layers className="h-6 w-6" />
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">ContentReach</h1>
          <div className="text-muted-foreground mt-4">
            {status === "loading" && <p>Accepting invitation...</p>}
            {status === "invalid" && <p>Invalid invitation link.</p>}
            {status === "error" && <p>This invitation has expired or was already used.</p>}
            {status === "success" && <p>Welcome! Redirecting...</p>}
          </div>
        </div>
      </div>
    </div>
  );
}
