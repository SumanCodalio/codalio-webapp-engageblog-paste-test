import re

with open("src/pages/AdminUsers.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'export default function AdminUsers() {',
    'export default function AdminUsersVendored({ users, isLoading, onInviteUser, onDeleteUser }: any) {'
)

content = re.sub(r'const \[users, setUsers\] = useState\(\[[\s\S]*?\]\)\n', 'const localUsers = users || []\n', content)
content = content.replace('users.filter', 'localUsers.filter')
content = content.replace('users.map', 'localUsers.map')
content = content.replace('{users.length}', '{localUsers.length}')

content = re.sub(
    r'const handleSendInvite = \(\) => \{[\s\S]*?\}',
    'const handleSendInvite = () => { onInviteUser(inviteEmail); setIsInviteModalOpen(false); }',
    content
)

content = re.sub(
    r'const handleDeleteUser = \(id\) => \{[\s\S]*?\}',
    'const handleDeleteUser = (id: any) => { onDeleteUser(id); }',
    content
)

with open("src/pages/AdminUsers.vendored.tsx", "w") as f:
    f.write(content)
