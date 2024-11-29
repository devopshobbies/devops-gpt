import axios, { AxiosInstance } from 'axios';
import { BASE_API } from '@/config/global';

export const apiClient: AxiosInstance = axios.create({
  baseURL: BASE_API,
  headers: {
    'Content-Type': 'application/json',
  },
});
