import React, { useState } from 'react';
import { useModelStore, useOrganization, storage } from '@rhino-dev/rhino-react';
import { useNavigate } from 'react-router-dom';
import CreatePostVendored from './CreatePost.vendored';

export default function CreatePost() {
  const store = useModelStore<any>('posts');
  
  const organization_id = useOrganization();
  const userStr = storage.getItem("user");
  const user = userStr ? JSON.parse(userStr) : null;
  const navigate = useNavigate();
  const [errorMsg, setErrorMsg] = useState<any>(null);
  
  const handleSave = (data: any) => {
    store.mutate(
      { ...data, organization_id, user_id: user?.id },
      {
        onSuccess: () => navigate('/'),
        onError: (err: any) => setErrorMsg(err.response?.data?.errors || err.message),
      }
    );
  };
  
  return (
    <CreatePostVendored
      isSaving={store.isPending}
      isPublishing={store.isPending}
      onSaveDraft={handleSave}
      onPublishPost={handleSave}
      errorMsg={errorMsg}
    />
  );
}
