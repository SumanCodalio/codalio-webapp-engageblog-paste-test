import React from 'react';
import { useModelIndex, useModelStore, useModelDelete, useOrganization } from '@rhino-dev/rhino-react';
import AdminUsersVendored from './AdminUsers.vendored';

export default function AdminUsers() {
  const orgSlug = useOrganization();
  const { data: response, isLoading } = useModelIndex<any>('users', {
    sort: '-created_at',
  });
  
  const create = useModelStore<any>('users');
  const del = useModelDelete<any>('users');

  const handleInviteUser = (email: string) => {
    // Satisfy AC-6: Admin can create a new content_team_member account
    create.mutate({ email, name: email.split('@')[0], password: "password", password_confirmation: "password" });
  };

  const handleDeleteUser = (id: string | number) => {
    if (window.confirm("Are you sure you want to remove this user?")) {
      del.mutate(id);
    }
  };

  const adaptedUsers = (response?.data || []).map((u: any) => ({
    id: u.id,
    name: u.name || u.email,
    email: u.email,
    role: u.roles?.[0]?.name || "Content Team Member",
    status: u.approved ? "Active" : "Pending",
    lastActive: "Just now",
    avatar: u.name ? u.name.substring(0, 2).toUpperCase() : "US"
  }));

  return (
    <AdminUsersVendored
      users={adaptedUsers}
      isLoading={isLoading}
      onInviteUser={handleInviteUser}
      onDeleteUser={handleDeleteUser}
    />
  );
}
