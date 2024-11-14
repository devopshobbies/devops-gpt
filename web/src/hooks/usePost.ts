import apiClient from "../utils/apiClient";

import { useQuery } from "@tanstack/react-query";
import { ENDPOINTS } from "../features/constants";

const usePost = (endpoint: ENDPOINTS, data: any) =>
  useQuery({
    queryKey: [endpoint],
    queryFn: () =>
      data ? apiClient.post(endpoint, data) : Promise.reject("No request data"),
    retry: 4,
    staleTime: 60,
  });

export default usePost;
