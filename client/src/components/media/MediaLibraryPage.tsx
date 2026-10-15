// @ts-nocheck
import { useModelIndex, useModelStore, useModelDelete } from '@rhino-dev/rhino-react';
export const MediaLibraryPage = () => {
  const videos = useModelIndex('videos');
  const createVideo = useModelStore('videos');
  const deleteVideo = useModelDelete('videos');
  return <div>MediaLibraryPage</div>;
};
