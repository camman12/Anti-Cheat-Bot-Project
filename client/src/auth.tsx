import { Route, RouteProps, Redirect } from 'react-router-dom';
import jwt_decode from 'jwt-decode';

interface Token {
  exp: number;
  iat: number;
  id: number;
  jti: string;
  rf_exp: number;
  rls: string;
}

function isExpired(token: string): boolean {
  const decoded = jwt_decode<Token>(token);
  const now = new Date();
  return decoded.exp * 1000 < now.getTime();
}

export function isLoggedIn(): boolean {
  const token = localStorage.getItem('token');

  if (token === null) {
    return false;
  }

  return !isExpired(token);
}

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
