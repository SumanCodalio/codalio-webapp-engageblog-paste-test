// @ts-nocheck
import { Outlet } from 'react-router-dom';
import { useAuth, useOrganization } from '@rhino-dev/rhino-react';

export const AppLayout = () => {
  const { logout } = useAuth();
  const org = useOrganization();
  return (
    <div>
      <nav>
        <span>Org: {org}</span>
        <button onClick={() => logout()}>Logout</button>
      </nav>
      <main><Outlet /></main>
    </div>
  );
};
