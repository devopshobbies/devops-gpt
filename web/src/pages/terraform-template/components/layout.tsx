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

const TerraformTemplate: FC = () => {
  return (
    <div className="flex h-dvh items-center">
      <div className="flex h-full w-full max-w-96 flex-col items-center justify-center divide-y divide-gray-500 border-r border-gray-500">
        {menu.map((link) => (
          <NavLink
            key={link.url}
            to={link.url}
            className={({ isActive }) =>
              `block w-full p-4 text-center outline-none transition-all ${isActive ? 'bg-orange-base' : ''}`
            }
          >
            {link.title}
          </NavLink>
        ))}
      </div>
      <div className="flex h-full w-2/3 items-center justify-center">
        <Outlet />
      </div>
    </div>
  );
};

export default TerraformTemplate;
