import re

with open("src/pages/MediaLibrary.vendored.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'export default function MediaLibrary() {',
    'export default function MediaLibraryVendored({ assets, isLoading, onDeleteAsset }: any) {'
)

# Remove local state
content = re.sub(r'const \[assets, setAssets\] = useState\(\[[\s\S]*?\]\)', 'const localAssets = assets || []', content)
content = content.replace('assets.filter', 'localAssets.filter')
content = content.replace('assets.map', 'localAssets.map')

content = re.sub(
    r'const handleDeleteAsset = \(id\) => \{[\s\S]*?\}',
    'const handleDeleteAsset = (id: any) => { onDeleteAsset(id); }',
    content
)

content = content.replace('const [selectedAsset, setSelectedAsset] = useState(assets[0])', 'const [selectedAsset, setSelectedAsset] = useState<any>(localAssets[0] || null)')

with open("src/pages/MediaLibrary.vendored.tsx", "w") as f:
    f.write(content)
