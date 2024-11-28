import { Route, Routes, useLocation } from 'react-router';
import MainLayout from '@/components/layouts/main-layout/main-layout';

function App() {
  const location = useLocation();
  return (
    <div>
      <div className="container mx-auto border-l border-r border-gray-700 h-dvh max-w-7xl">
        <Routes location={location}>
          <Route element={<MainLayout />}>
            <Route path="/" />
          </Route>
        </Routes>
      </div>
    </div>
  );
}

export default App;
