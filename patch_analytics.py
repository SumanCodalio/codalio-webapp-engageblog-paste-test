import re

with open('client/src/pages/Analytics.tsx', 'r') as f:
    content = f.read()

replacement = """  const [searchQuery, setSearchQuery] = useState("");
  const leaderboard = serverPosts.map(p => ({
    id: p.id,
    title: p.title,
    category: p.status,
    hasVideo: p.videos && p.videos.length > 0,
    views: "N/A",
    completion: "N/A",
    shares: "N/A"
  }));
"""
# Replace from `const [searchQuery, setSearchQuery] = useState("");` to `const filteredLeaderboard = leaderboard.filter(`
pattern = re.compile(r'const \[searchQuery, setSearchQuery\] = useState\(""\);[\s\S]*?const filteredLeaderboard = leaderboard\.filter\(')
content = pattern.sub(replacement + "  const filteredLeaderboard = leaderboard.filter(", content)

with open('client/src/pages/Analytics.tsx', 'w') as f:
    f.write(content)
