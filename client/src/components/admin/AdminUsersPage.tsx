// @ts-nocheck
import { useModelIndex, useModelStore, useModelUpdate, useModelDelete } from '@rhino-dev/rhino-react';
export const AdminUsersPage = () => {
  const users = useModelIndex('users');
  const createUser = useModelStore('users');
  const updateUser = useModelUpdate('users');
  const deleteUser = useModelDelete('users');
  return <div>AdminUsersPage</div>;
};
