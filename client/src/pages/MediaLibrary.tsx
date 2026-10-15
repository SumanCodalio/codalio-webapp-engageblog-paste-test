import React from 'react';
import { useModelIndex, useModelDelete, useModelStore, useOrganization, storage } from '@rhino-dev/rhino-react';
import MediaLibraryVendored from './MediaLibrary.vendored';

export default function MediaLibrary() {
  const { data: response, isLoading } = useModelIndex<any>('videos', {
    sort: '-created_at',
  });
  const del = useModelDelete<any>('videos');
  const store = useModelStore<any>('videos');
  const organization_id = useOrganization();
  const userStr = storage.getItem("user");
  const user = userStr ? JSON.parse(userStr) : null;

  const handleDeleteAsset = (id: string | number) => {
    if (window.confirm("Are you sure you want to delete this video?")) {
      del.mutate(id);
    }
  };

  const handleUploadDrop = (data: any) => {
    store.mutate({ ...data, organization_id, user_id: user?.id });
  };

  const adaptedAssets = (response?.data || []).map((v: any) => ({
    id: v.id,
    title: v.title,
    type: "video",
    format: "mp4",
    size: "142.4 MB",
    duration: v.duration ? `${Math.floor(v.duration / 60)}:${v.duration % 60}` : "Unknown",
    date: v.created_at ? new Date(v.created_at).toLocaleDateString() : "Just now",
    status: "Ready",
    resolution: "1920x1080",
    bitrate: "4.5 Mbps",
    url: v.url
  }));

  return (
    <MediaLibraryVendored
      assets={adaptedAssets}
      isLoading={isLoading}
      onDeleteAsset={handleDeleteAsset}
      onUploadDrop={handleUploadDrop}
    />
  );
}
