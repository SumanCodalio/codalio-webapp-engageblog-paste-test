import { useState, type FormEvent } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import { useResetPassword, usePasswordRecover } from "@rhino-dev/rhino-react";
import { Layers } from "lucide-react";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Label } from "../components/ui/label";
import { Alert, AlertDescription } from "../components/ui/alert";

export default function ResetPassword() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const token = searchParams.get("token");
  
  const recover = usePasswordRecover();
  const reset = useResetPassword();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");
  const [status, setStatus] = useState("");
  const [error, setError] = useState("");

  const handleRecover = async (e: FormEvent) => {
    e.preventDefault();
    try {
      await recover.mutateAsync({ email });
      setStatus("Recovery email sent.");
      setError("");
    } catch (err: any) {
      setError("Failed to send recovery email.");
    }
  };

  const handleReset = async (e: FormEvent) => {
    e.preventDefault();
    try {
      await reset.mutateAsync({ token: token!, email, password, password_confirmation: passwordConfirmation });
      setStatus("Password reset successful.");
      setError("");
      setTimeout(() => navigate("/login"), 2000);
    } catch (err: any) {
      setError("Failed to reset password.");
    }
  };

  return (
    <div className="min-h-screen bg-background w-full min-w-0 overflow-x-hidden">
      <div className="flex items-center justify-center min-h-[85vh] px-4 w-full min-w-0">
        <div className="max-w-md mx-auto my-12 bg-card border border-border shadow-xl rounded-2xl p-6 sm:p-8 space-y-6 text-center">
          <div className="mx-auto w-12 h-12 rounded-xl bg-primary text-primary-foreground flex items-center justify-center shadow-md shadow-primary/30">
            <Layers className="h-6 w-6" />
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Reset Password</h1>
          
          {status && (
            <Alert className="bg-emerald-500/10 border-emerald-500/20 text-emerald-600 dark:text-emerald-400 py-2.5">
              <AlertDescription className="text-xs font-medium ml-2">{status}</AlertDescription>
            </Alert>
          )}

          {error && (
            <Alert className="bg-destructive/10 border-destructive/20 text-destructive py-2.5">
              <AlertDescription className="text-xs font-medium">{error}</AlertDescription>
            </Alert>
          )}

          {!token ? (
            <form onSubmit={handleRecover} className="space-y-4 text-left">
              <div className="space-y-1.5">
                <Label htmlFor="email" className="text-xs font-medium">Email</Label>
                <Input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
              </div>
              <Button type="submit" disabled={recover.isPending} className="w-full">
                {recover.isPending ? "Sending..." : "Send Recovery Email"}
              </Button>
            </form>
          ) : (
            <form onSubmit={handleReset} className="space-y-4 text-left">
              <div className="space-y-1.5">
                <Label htmlFor="email" className="text-xs font-medium">Email</Label>
                <Input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
              </div>
              <div className="space-y-1.5">
                <Label htmlFor="password" className="text-xs font-medium">New Password</Label>
                <Input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
              </div>
              <div className="space-y-1.5">
                <Label htmlFor="passwordConfirm" className="text-xs font-medium">Confirm Password</Label>
                <Input id="passwordConfirm" type="password" value={passwordConfirmation} onChange={(e) => setPasswordConfirmation(e.target.value)} required />
              </div>
              <Button type="submit" disabled={reset.isPending} className="w-full">
                {reset.isPending ? "Resetting..." : "Reset Password"}
              </Button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
