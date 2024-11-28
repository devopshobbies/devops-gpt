import { Route, Routes, useLocation } from 'react-router';
import MainLayout from '@/components/layouts/main-layout/main-layout';
import TerraformTemplate from '@/pages/terraform-template/components/layout';
import { Argocd, Docker, EC2, IAM, Installation, S3 } from './pages';

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
            <Route path="installation" element={<Installation />} />
          </Route>
        </Routes>
      </div>
    </div>
  );
}

export default App;
