import Header from './Header';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar/Sidebar';

const Layout = () => {
  return (
    <div className="h-full flex flex-col">
      <Header />
      <div className="flex flex-1">
        <Sidebar />
        <div className="flex-1 px-4 sm:px-8 max-w-5xl mx-auto">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default Layout;
