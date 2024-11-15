import Header from "./Header";
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <Header />
      <div className="w-full px-28 h-full ">
        <Outlet />
      </div>
    </>
  );
};

export default Layout;
