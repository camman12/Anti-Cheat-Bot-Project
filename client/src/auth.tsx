import { Route, RouteProps, Redirect } from 'react-router-dom';

export const isLoggedIn = () => localStorage.getItem('token') !== null;

export const logout = () => localStorage.removeItem('token');

export function PrivateRoute(props: RouteProps) {
  if (!isLoggedIn()) {
    return <Redirect to="/login" />;
  }

  return <Route {...props} />;
}

export async function authFetch(url: string, opts?: RequestInit) {
  const token = localStorage.getItem('token');

  if (!token) {
    throw new Error("Not authenticated");
  }

  return await fetch(url, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
    ...opts,
  });
}
