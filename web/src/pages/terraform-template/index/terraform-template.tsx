import { FC } from 'react';
import { NavLink, Outlet } from 'react-router';

const menu = [
  {
    url: 'docker',
    title: 'Docker Service',
  },
  {
    url: 'ec2',
    title: 'EC2 Service',
  },
  {
    url: 's3',
    title: 'S3 Service',
  },
  {
    url: 'iam',
    title: 'IAM Service',
  },
  {
    url: 'argocd',
    title: 'ARGOCD Service',
  },
];

export const TerraformTemplate: FC = () => {
  return (
    <div className="flex items-center h-dvh">
      <div className="flex flex-col items-center justify-center w-full h-full border-r border-gray-500 divide-y divide-gray-500 max-w-96">
        {menu.map((link) => (
          <NavLink
            to={link.url}
            className={({ isActive }) =>
              `block w-full p-4 text-center outline-none transition-all ${isActive ? 'bg-orange-base' : ''}`
            }
          >
            {link.title}
          </NavLink>
        ))}
      </div>
      <div className="flex items-center justify-center w-2/3 h-full">
        <Outlet />
      </div>
    </div>
  );
};
