import axios from "axios";

export default axios.create({
  baseURL: import.meta.env.VITE_API_CLIENT_BASE_URL,
  headers: {
    Accept: "application/json",
  },
});
