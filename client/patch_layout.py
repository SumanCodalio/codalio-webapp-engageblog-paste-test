import re

with open('src/components/Layout.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'const { logout } = useAuth();',
    'const { logout } = useAuth();\n  const { hasRole } = require("@rhino-dev/rhino-react").useUserRole();'
)

# Use hasRole('admin') to guard adminItems
content = content.replace(
    '{adminItems.map((adm) => (',
    '{hasRole("admin") && adminItems.map((adm) => ('
)

with open('src/components/Layout.tsx', 'w') as f:
    f.write(content)
