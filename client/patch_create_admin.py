import re

with open("src/pages/AdminUsers.tsx", "r") as f:
    content = f.read()
content = content.replace('useBaseOwnerId', 'useOrganization')
with open("src/pages/AdminUsers.tsx", "w") as f:
    f.write(content)

with open("src/pages/CreatePost.tsx", "r") as f:
    content = f.read()
content = content.replace('useBaseOwnerId', 'useOrganization')
content = content.replace('useUser, ', '')
content = content.replace('const user = useUser();', '')
content = content.replace('user_id: user?.id, ', '')
with open("src/pages/CreatePost.tsx", "w") as f:
    f.write(content)
