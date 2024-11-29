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
    <nav className="flex h-14 items-center border-b border-gray-500 p-4">
      <div className="flex w-full items-center justify-between gap-4">
        <img src="/images/logo-svg.svg" className="mr-8" width={60} />
        <div className="flex items-center gap-5">
          {navbar.map((link) => (
            <NavLink
              key={link.url}
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
