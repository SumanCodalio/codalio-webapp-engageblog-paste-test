import re

with open('src/components/Layout.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'import { useAuth, useOrganization } from "@rhino-dev/rhino-react";',
    'import { useAuth, useOrganization, useUserRole } from "@rhino-dev/rhino-react";'
)

content = content.replace(
    'const { logout } = useAuth();\n  const { hasRole } = require("@rhino-dev/rhino-react").useUserRole();',
    'const { logout } = useAuth();\n  const { hasRole } = useUserRole();'
)

with open('src/components/Layout.tsx', 'w') as f:
    f.write(content)
