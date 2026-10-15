import React from "react";
import { Routes, Route, Navigate, Outlet } from "react-router-dom";
import { useAuth, useUserRole } from "@rhino-dev/rhino-react";
import Layout from "./components/Layout";
import Landing from "./pages/Landing";
import Login from "./pages/Login";
import CreatePost from "./pages/CreatePost";
import MediaLibrary from "./pages/MediaLibrary";
import Analytics from "./pages/Analytics";
import Admin from "./pages/Admin";
import AdminUsers from "./pages/AdminUsers";
import AdminApiIntegrations from "./pages/AdminApiIntegrations";
import AdminSystemSettings from "./pages/AdminSystemSettings";
import AdminSystemReports from "./pages/AdminSystemReports";
import ResetPassword from "./pages/ResetPassword";
import AcceptInvitation from "./pages/AcceptInvitation";
import { AppOwnerProvider } from "./contexts/AppOwnerProvider";

const AuthenticatedRoute = () => {
  const { isAuthenticated } = useAuth();
  if (!isAuthenticated) return <Navigate to="/login" replace />;
  return <Outlet />;
};

const PublicOnlyRoute = () => {
  const { isAuthenticated } = useAuth();
  if (isAuthenticated) return <Navigate to="/" replace />;
  return <Outlet />;
};


const AdminOnlyRoute = () => {
  const { hasRole } = useUserRole();
  if (!hasRole("admin")) return <Navigate to="/" replace />;
  return <Outlet />;
};

function App() {

  return (
    <Routes>
      <Route path="/login" element={<PublicOnlyRoute />} >
        <Route index element={<Login />} />
      </Route>
      <Route path="/auth/signin" element={<Navigate to="/login" replace />} />
      <Route path="/auth/signup" element={<Navigate to="/login" replace />} />
      <Route path="/auth/reset-password" element={<PublicOnlyRoute />} >
        <Route index element={<ResetPassword />} />
      </Route>
      <Route path="/invitations/accept" element={<PublicOnlyRoute />} >
        <Route index element={<AcceptInvitation />} />
      </Route>
      <Route element={<AuthenticatedRoute />}>
        <Route element={<AppOwnerProvider><Layout /></AppOwnerProvider>}>
          <Route path="/" element={<Landing />} />
          <Route path="/create-post" element={<CreatePost />} />
          <Route path="/media-library" element={<MediaLibrary />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route element={<AdminOnlyRoute />}><Route path="/admin" element={<Admin />} />
          <Route path="/admin/users" element={<AdminUsers />} />
          <Route path="/admin/api-integrations" element={<AdminApiIntegrations />} />
          <Route path="/admin/system-settings" element={<AdminSystemSettings />} />
          <Route path="/admin/system-reports" element={<AdminSystemReports />} /></Route>
        </Route>
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default App;
