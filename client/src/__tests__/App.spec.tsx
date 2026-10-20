import { describe, it, expect, vi, beforeAll } from 'vitest';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Login from '../pages/Login';
import CreatePost from '../pages/CreatePost';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

beforeAll(() => {
  global.ResizeObserver = class ResizeObserver {
    observe() {}
    unobserve() {}
    disconnect() {}
  };
});

vi.mock('@rhino-dev/rhino-react', async (importOriginal) => {
  const actual = await importOriginal<any>();
  return {
    ...actual,
    useAuth: () => ({
      login: vi.fn().mockResolvedValue({ success: true, organization_slug: 'demo-org' }),
      setOrganization: vi.fn(),
      isAuthenticated: false
    }),
    useOrganization: () => 'demo-org',
    useModelStore: () => ({ mutate: vi.fn(), isPending: false }),
    useUserRole: () => ({ hasRole: vi.fn().mockReturnValue(true) }),
  };
});

describe('Login Page', () => {
  it('renders login form', () => {
    render(
      <MemoryRouter>
        <Login />
      </MemoryRouter>
    );
    expect(screen.getByText('Sign In to engageblog testing deployment')).toBeTruthy();
  });
});

describe('CreatePost Page', () => {
  it('renders create post form', () => {
    const queryClient = new QueryClient();
    render(
      <QueryClientProvider client={queryClient}>
        <MemoryRouter>
          <CreatePost />
        </MemoryRouter>
      </QueryClientProvider>
    );
    expect(screen.getByText('Create & Publish Article')).toBeTruthy();
  });
});
