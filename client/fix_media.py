import re
with open("src/pages/MediaLibrary.tsx", "r") as f:
    content = f.read()

content = re.sub(
    r'(\s*)\{\/\* Selected Asset Details \*\/}\n\s*<Card className="bg-card border border-border p-5 rounded-2xl shadow-sm space-y-4">',
    r'\1{/* Selected Asset Details */}\n\1{selectedAsset && (\n\1<Card className="bg-card border border-border p-5 rounded-2xl shadow-sm space-y-4">',
    content
)

content = re.sub(
    r'(<VideoPlayerModal[^>]*/>\n\s*</Card>)',
    r'\1\n        )}',
    content
)

content = content.replace(
    'const isSelected = selectedAsset.id === asset.id',
    'const isSelected = selectedAsset?.id === asset.id'
)

with open("src/pages/MediaLibrary.tsx", "w") as f:
    f.write(content)
