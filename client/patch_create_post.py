import re

with open("src/pages/CreatePost.vendored.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'export default function CreatePost() {',
    'export default function CreatePostVendored({ isSaving, isPublishing, onSaveDraft, onPublishPost, errorMsg }: any) {'
)

# Remove internal state that we now pass as props
content = re.sub(r'const \[isSaving, setIsSaving\] = useState\(false\)\n', '', content)
content = re.sub(r'const \[isPublishing, setIsPublishing\] = useState\(false\)\n', '', content)

# Replace the handlers with props calls
content = re.sub(
    r'const handleSaveDraft = \(\) => \{[\s\S]*?\}, 500\)\n    \}',
    'const handleSaveDraft = () => {\n      onSaveDraft({ title, content: bodyText, status: "draft" })\n    }',
    content
)

content = re.sub(
    r'const handlePublish = \(\) => \{[\s\S]*?\}, 700\)\n    \}',
    'const handlePublish = () => {\n      onPublishPost({ title, content: bodyText, status: "published" })\n    }',
    content
)

with open("src/pages/CreatePost.vendored.tsx", "w") as f:
    f.write(content)
