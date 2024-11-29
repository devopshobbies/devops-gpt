import {
  AxiosError,
  AxiosHeaders,
  AxiosInstance,
  AxiosRequestConfig,
  AxiosResponse,
} from 'axios';
import { useMutation } from '@tanstack/react-query';
import { apiClient } from '@/lib/axios';

async function request<R, B, E = unknown>(
  axiosInstance: AxiosInstance,
  method: 'get' | 'post' | 'put' | 'patch',
  url: string,
  body?: B,
  headers?: AxiosHeaders,
  config?: AxiosRequestConfig,
): Promise<AxiosResponse<R>> {
  try {
    return await axiosInstance({
      method,
      url,
      ...(method !== 'get' && { data: body }),
      headers,
      ...config,
    });
  } catch (error) {
    throw error as AxiosError<E>;
  }
}

function mutationHook(method: 'get' | 'post' | 'put' | 'patch') {
  return function useCustomMutation<R, B, E = unknown>(
    url: string,
    key: string,
    headers?: AxiosHeaders,
    configs?: AxiosRequestConfig,
  ) {
    return useMutation<AxiosResponse<R>, AxiosError<E>, B>({
      mutationKey: [key],
      mutationFn: (body: B) =>
        request<R, B, E>(apiClient, method, url, body, headers, configs),
    });
  };
}

// Export hooks for each HTTP method.
export const useGet = mutationHook('get');
export const usePost = mutationHook('post');
export const usePut = mutationHook('put');
export const usePatch = mutationHook('patch');
