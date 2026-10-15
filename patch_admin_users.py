import re

with open('client/src/pages/AdminUsers.tsx', 'r') as f:
    content = f.read()

content = content.replace('users_roles.role', 'user_roles.role')
content = content.replace('u.users_roles?.[0]', 'u.user_roles?.[0]')

with open('client/src/pages/AdminUsers.tsx', 'w') as f:
    f.write(content)
