import re
with open("src/pages/Landing.tsx", "r") as f:
    content = f.read()

content = content.replace('useBaseOwnerId', 'useOrganization')
with open("src/pages/Landing.tsx", "w") as f:
    f.write(content)
