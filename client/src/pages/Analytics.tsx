import React from 'react';
import { useModelIndex, api, useOrganization } from '@rhino-dev/rhino-react';
import { useQuery } from '@tanstack/react-query';
import AnalyticsVendored from './Analytics.vendored';

export default function Analytics() {
  const orgSlug = useOrganization();
  const { data: response, isLoading: loadingData } = useModelIndex<any>('analytics_data', {
    sort: '-recorded_at',
  });
  const { data: metricsRes, isLoading: loadingMetrics } = useQuery({
    queryKey: ['dashboard', orgSlug],
    queryFn: () => api.get(`/api/${orgSlug}/dashboard`).then(res => res.data),
    enabled: !!orgSlug
  });

  const adaptedLeaderboard = (response?.data || []).slice(0, 5).map((d: any) => ({
    id: d.id,
    title: d.post?.title || `Event ${d.id}`,
    type: "Text",
    views: d.event_data?.ip_address ? "1" : "0",
    engagement: "N/A",
    trend: "+0%"
  }));

  const adaptedMetrics = [
    { value: metricsRes?.total_views || "0" },
    { value: "0" },
    { value: "0:00" },
    { value: "0%" }
  ];

  return (
    <AnalyticsVendored
      leaderboardData={adaptedLeaderboard}
      metricsData={adaptedMetrics}
      isLoading={loadingData || loadingMetrics}
    />
  );
}
