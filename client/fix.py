with open("src/pages/MediaLibrary.vendored.tsx", "r") as f:
    text = f.read()

text = text.replace("const handleDeleteAsset = (id: any) => { onDeleteAsset(id); }\n    }", "const handleDeleteAsset = (id: any) => { onDeleteAsset(id); }")
with open("src/pages/MediaLibrary.vendored.tsx", "w") as f:
    f.write(text)
