import apiClient from "../utils/apiClient";

import { useQuery } from "@tanstack/react-query";
import { ENDPOINTS } from "../features/constants";

const usePost = <T>(endpoint: ENDPOINTS, data: T, id: string) =>
  useQuery({
    queryKey: [endpoint, id],
    queryFn: () =>
      data
        ? apiClient.post<T>(endpoint, data)
        : Promise.reject("No request data"),
    staleTime: 0,
    enabled: !!data && Object.keys(data).length > 0,
    refetchOnWindowFocus: false,
    gcTime: 0,
    retry: false,
  });

export default usePost;
