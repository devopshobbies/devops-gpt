import { createBrowserRouter } from "react-router-dom";
import Layout from "../layouts/Layout";
import BasicGen from "../features/basicGen/BasicGen";
import { ENDPOINTS } from "../features/constants";
import BugFix from "../features/bugFix/BugFix";
import ErrorPage from "../components/internal-ui/ErrorPage";
export const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <BasicGen /> },
      { path: ENDPOINTS.postFix, element: <BugFix /> },
    ],
  },
]);
