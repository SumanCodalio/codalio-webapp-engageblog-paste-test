import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'import { useAuth } from "@rhino-dev/rhino-react";',
    'import { useAuth, useUserRole } from "@rhino-dev/rhino-react";'
)

admin_guard = """
const AdminOnlyRoute = () => {
  const { hasRole } = useUserRole();
  if (!hasRole("admin")) return <Navigate to="/" replace />;
  return <Outlet />;
};

function App() {
"""

content = content.replace('function App() {', admin_guard)

content = content.replace(
    '<Route path="/admin" element={<Admin />} />',
    '<Route element={<AdminOnlyRoute />}><Route path="/admin" element={<Admin />} />'
)
content = content.replace(
    '<Route path="/admin/system-reports" element={<AdminSystemReports />} />',
    '<Route path="/admin/system-reports" element={<AdminSystemReports />} /></Route>'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
