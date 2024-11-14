import apiClient from "../utils/apiClient";

import { useQuery } from "@tanstack/react-query";
import { ENDPOINTS } from "../features/constants";

const usePost = (endpoint: ENDPOINTS, data: any) =>
  useQuery({
    queryKey: [endpoint],
    queryFn: () => apiClient.post(endpoint, data),
    retry: 4,
    staleTime: 60,
  });

export default usePost;
