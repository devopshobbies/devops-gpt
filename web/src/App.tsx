import { Route, Routes, useLocation } from 'react-router';
import MainLayout from '@/components/layouts/main-layout/main-layout';
import { TerraformTemplate } from '@/pages/terraform-template/index/terraform-template';
import Docker from '@/pages/terraform-template/Docker/docker';
import EC2 from './pages/terraform-template/EC2/ec2';
import S3 from './pages/terraform-template/S3/s3';
import IAM from './pages/terraform-template/IAM/iam';
import Argocd from './pages/terraform-template/ARGOCD/argocd';

function App() {
  const location = useLocation();
  return (
    <div>
      <div className="container mx-auto border-l border-r border-gray-700 h-dvh max-w-7xl">
        <Routes location={location}>
          <Route element={<MainLayout />}>
            <Route path="terraform-template" element={<TerraformTemplate />}>
              <Route path="docker" element={<Docker />} />
              <Route path="ec2" element={<EC2 />} />
              <Route path="s3" element={<S3 />} />
              <Route path="iam" element={<IAM />} />
              <Route path="argocd" element={<Argocd />} />
            </Route>
          </Route>
        </Routes>
      </div>
    </div>
  );
}

export default App;
