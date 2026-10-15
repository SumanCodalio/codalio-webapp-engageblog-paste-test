import re

with open("src/components/Layout.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'import { useAuth, useUser, useOrganization, useUserRole } from "@rhino-dev/rhino-react";',
    'import { useAuth, useOrganization } from "@rhino-dev/rhino-react";'
)

content = content.replace(
    '  const user = useUser();\n  const { hasRole } = useUserRole();\n',
    ''
)

content = content.replace('{user?.name || "User"}', 'User')
content = content.replace('{user?.name?.substring(0,2).toUpperCase() || "US"}', 'US')
content = content.replace('{user?.email}', 'user@example.com')

content = content.replace('hasRole("admin") && ', '')

with open("src/components/Layout.tsx", "w") as f:
    f.write(content)
