import { createBrowserRouter } from "react-router-dom";
import Layout from "./layouts/Layout";
import BasicGen from "./features/basicGen";
import BugFix from "./features/bugFix";
import ErrorPage from "./components/internal-ui/ErrorPage";
import { routes, terraformRoutes } from "./utils/routing";
import Terraform from "./features/terraform";
import Docker from "./features/terraform/components/Docker";
import EC2 from "./features/terraform/components/EC2";
import S3 from "./features/terraform/components/S3";
import IAM from "./features/terraform/components/IAM";
import Argocd from "./features/terraform/components/Argocd";
export const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <BasicGen /> },
      { path: routes.bugFix, element: <BugFix /> },
      {
        path: routes.terraformTemplate,
        element: <Terraform />,
        children: [
          {
            path: routes.terraformTemplate + terraformRoutes.dockerService,
            element: <Docker />,
          },
          {
            path: routes.terraformTemplate + terraformRoutes.ec2Service,
            element: <EC2 />,
          },
          {
            path: routes.terraformTemplate + terraformRoutes.s3Service,
            element: <S3 />,
          },
          {
            path: routes.terraformTemplate + terraformRoutes.iamService,
            element: <IAM />,
          },
          {
            path: routes.terraformTemplate + terraformRoutes.argocdService,
            element: <Argocd />,
          },
        ],
      },
    ],
  },
]);
