import { storage } from '@rhino-dev/rhino-react';
export const useUser = () => {
    const userStr = storage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
}
