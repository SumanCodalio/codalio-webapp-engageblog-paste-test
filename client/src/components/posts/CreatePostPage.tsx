// @ts-nocheck
import { useModelStore, useModelUpdate } from '@rhino-dev/rhino-react';
export const CreatePostPage = () => {
  const createPost = useModelStore('posts');
  const updatePost = useModelUpdate('posts');
  const createVideo = useModelStore('videos');
  return <div>CreatePostPage</div>;
};
