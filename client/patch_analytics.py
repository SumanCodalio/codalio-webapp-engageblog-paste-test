import re

with open("src/pages/Analytics.vendored.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'export default function Analytics() {',
    'export default function AnalyticsVendored({ leaderboardData, metricsData, isLoading }: any) {'
)

# Remove local state
content = re.sub(r'const leaderboard = \[[^\]]*\];', 'const leaderboard = leaderboardData || [];', content)

# Keep cards structure but inject metricsData
cards_replacement = """  const cards = [
    { label: "Total Views", value: metricsData?.[0]?.value || "0", trend: "+14.2%", isPositive: true, icon: Eye, color: "text-blue-500", bg: "bg-blue-500/10" },
    { label: "Unique Visitors", value: metricsData?.[1]?.value || "0", trend: "+8.7%", isPositive: true, icon: Users, color: "text-emerald-500", bg: "bg-emerald-500/10" },
    { label: "Avg. Watch Time", value: metricsData?.[2]?.value || "0", trend: "+2.1%", isPositive: true, icon: Clock, color: "text-amber-500", bg: "bg-amber-500/10" },
    { label: "Engagement Rate", value: metricsData?.[3]?.value || "0", trend: "-0.4%", isPositive: false, icon: Sparkles, color: "text-purple-500", bg: "bg-purple-500/10" },
  ];"""

content = re.sub(r'const cards = \[[\s\S]*?\];', cards_replacement, content)

with open("src/pages/Analytics.vendored.tsx", "w") as f:
    f.write(content)
