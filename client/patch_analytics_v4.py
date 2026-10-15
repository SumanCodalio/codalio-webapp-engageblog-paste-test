import re
with open("src/pages/Analytics.tsx", "r") as f:
    content = f.read()

content = content.replace('useBaseOwnerId', 'useOrganization')
with open("src/pages/Analytics.tsx", "w") as f:
    f.write(content)
