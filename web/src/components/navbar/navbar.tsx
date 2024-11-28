import { FC } from 'react';
import { NavLink } from 'react-router';

const navbar = [
  {
    url: '/',
    title: 'Basic',
  },
  {
    url: '/bug-fix',
    title: 'Bug Fix',
  },
  {
    url: '/terraform-template',
    title: 'Terraform Template',
  },
  {
    url: '/installation',
    title: 'Installation',
  },
  {
    url: '/helm-template',
    title: 'Helm Template',
  },
];

const Navbar: FC = () => {
  return (
    <nav className="flex items-center p-4 border-b border-gray-500 h-14">
      <div className="flex items-center justify-between w-full gap-4">
        <img src="/images/logo-svg.svg" className="mr-8" width={60} />
        <div className="flex items-center gap-5">
          {navbar.map((link) => (
            <NavLink
              to={link.url}
              className={({ isActive }) => (isActive ? 'text-orange-base' : '')}
            >
              {link.title}
            </NavLink>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
