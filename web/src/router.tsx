import { createBrowserRouter } from "react-router-dom";
import Layout from "./layouts/Layout";
import BasicGen from "./features/basicGen/BasicGen";
import BugFix from "./features/bugFix/BugFix";
import ErrorPage from "./components/internal-ui/ErrorPage";
import { routes } from "./utils/routing";
import Terraform from "./features/terraform/Terraform";
import Download from "./features/listDirectory/Download";
export const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <BasicGen /> },
      { path: routes.bugFix, element: <BugFix /> },
      { path: routes.terraformTemplate, element: <Terraform /> },
      { path: routes.listDirectory, element: <Download /> },
    ],
  },
]);
