import { storage } from "@rhino-dev/rhino-react";

export function useUser() {
  try {
    const userStr = storage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
  } catch (e) {
    return null;
  }
}
