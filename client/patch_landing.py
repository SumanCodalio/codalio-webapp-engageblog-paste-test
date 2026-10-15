import re

with open("src/pages/Landing.vendored.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'export default function Landing() {',
    'export default function LandingVendored({ posts, metrics, isLoading, onDeletePost }: any) {'
)

# Replace local `posts` state with the prop
content = re.sub(r'const \[posts, setPosts\] = useState\(\[[\s\S]*?\]\);', 'const localPosts = posts || [];', content)

# Replace metrics local state
content = re.sub(r'const metrics = \[[\s\S]*?\];', 'const localMetrics = metrics || [];', content)
content = content.replace('metrics.map', 'localMetrics.map')
content = content.replace('metrics[1]', 'localMetrics[1]')

# Change filteredPosts to use localPosts
content = content.replace('const filteredPosts = posts.filter(', 'const filteredPosts = localPosts.filter(')

# Replace handleDeletePost logic
content = re.sub(
    r'const handleDeletePost = \(id: string\) => \{[\s\S]*?\}\n  \};',
    'const handleDeletePost = (id: string) => {\n    onDeletePost(id);\n  };',
    content
)

# Remove unused setPosts references (if any in batch delete etc)
content = re.sub(r'setPosts\([\s\S]*?\);', '', content)

with open("src/pages/Landing.vendored.tsx", "w") as f:
    f.write(content)
