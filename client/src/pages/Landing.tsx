import React from 'react';
import { useModelIndex, useModelDelete } from '@rhino-dev/rhino-react';
import LandingVendored from './Landing.vendored';
import { api } from '@rhino-dev/rhino-react';
import { useQuery } from '@tanstack/react-query';
import { useOrganization } from '@rhino-dev/rhino-react';

export default function Landing() {
  const orgSlug = useOrganization();
  const { data: postsRes, isLoading: loadingPosts } = useModelIndex<any>('posts', {
    sort: '-created_at',
    perPage: 10
  });
  
  const { data: metricsRes, isLoading: loadingMetrics } = useQuery({
    queryKey: ['dashboard', orgSlug],
    queryFn: () => api.get(`/api/${orgSlug}/dashboard`).then(res => res.data),
    enabled: !!orgSlug
  });

  const del = useModelDelete<any>('posts');

  const handleDeletePost = (id: string | number) => {
    if (window.confirm("Are you sure you want to delete this post?")) {
      del.mutate(id);
    }
  };
  
  // Adapt backend posts to UI structure
  const adaptedPosts = (postsRes?.data || []).map((p: any) => ({
    id: p.id,
    title: p.title,
    category: 'Engineering',
    readTime: '5 min read',
    status: p.status === 'published' ? 'Published' : 'Draft',
    date: p.published_at ? new Date(p.published_at).toLocaleDateString() : 'Draft',
    author: { name: p.user?.name || 'User', initials: 'US' },
    views: 'N/A'
  }));

  const adaptedMetrics = [
    { label: "Total Content Reach", value: metricsRes?.total_views || "0", trend: "+12.5%", isPositive: true },
    { label: "Published Videos", value: metricsRes?.total_videos || "0", trend: "+3", isPositive: true },
    { label: "Engagement Rate", value: "4.8%", trend: "+0.6%", isPositive: true },
    { label: "Drafts Pending", value: "8", trend: "-2", isPositive: false }
  ];

  return (
    <LandingVendored
      posts={adaptedPosts}
      metrics={adaptedMetrics}
      isLoading={loadingPosts || loadingMetrics}
      onDeletePost={handleDeletePost}
    />
  );
}
