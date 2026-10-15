import re

with open('client/src/pages/MediaLibrary.tsx', 'r') as f:
    content = f.read()

replacement = """import { useModelIndex, useModelStore, useModelDelete, useBaseOwnerId, useUser } from "@rhino-dev/rhino-react";

export default function MediaLibrary() {
    const [searchTerm, setSearchTerm] = useState("")
    const [selectedType, setSelectedType] = useState("All")
    const [uploadModalOpen, setUploadModalOpen] = useState(false)
    const baseOwnerId = useBaseOwnerId();
    const user = useUser();
    
    const { data: videosResponse, isLoading, refetch } = useModelIndex("videos", {
      includes: ['user'],
      sort: '-created_at'
    });
    
    const store = useModelStore("videos");
    const del = useModelDelete("videos");
    
    const assets = (videosResponse?.data ?? []).map(v => ({
      id: v.id,
      title: v.title,
      type: "video",
      format: "mp4",
      size: "N/A",
      duration: v.duration ? `${Math.floor(v.duration/60)}:${(v.duration%60).toString().padStart(2, '0')}` : "0:00",
      resolution: "1080p",
      bitrate: "N/A",
      url: v.url,
      uploadDate: v.created_at ? new Date(v.created_at).toLocaleDateString() : ""
    }));
    
    const [selectedAsset, setSelectedAsset] = useState(assets[0] || null)
    
    // Update selected asset when data loads if null
    import_React.useEffect(() => {
      if (!selectedAsset && assets.length > 0) {
        setSelectedAsset(assets[0]);
      }
    }, [assets, selectedAsset]);
"""
# Replace from `export default function MediaLibrary() {` to `const [selectedAsset, setSelectedAsset] = useState(assets[0])`
pattern = re.compile(r'export default function MediaLibrary\(\) \{[\s\S]*?const \[selectedAsset, setSelectedAsset\] = useState\(assets\[0\]\)')
content = pattern.sub(replacement, content)
content = content.replace("import_React", "React")

with open('client/src/pages/MediaLibrary.tsx', 'w') as f:
    f.write(content)
