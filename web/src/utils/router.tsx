import { createBrowserRouter } from "react-router-dom";
import Layout from "../layouts/Layout";
import Landing from "../components/internal-ui/Landing";
import BasicGen from "../features/basicGen/BasicGen";
import { ENDPOINTS } from "../features/constants";
export const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Landing /> },
      { path: ENDPOINTS.postBasic, element: <BasicGen /> },
    ],
  },
]);
