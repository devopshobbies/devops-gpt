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
    title: 'ArgoCD Service',
  },
];

const TerraformTemplate: FC = () => {
  return (
    <div className="flex h-[calc(100vh-56px)] items-center">
      <div className="flex h-full w-full max-w-96 flex-col items-center justify-center divide-y divide-gray-500 border-r border-gray-500">
        {menu.map((link) => (
          <NavLink
            key={link.url}
            to={link.url}
            className={({ isActive }) =>
              `block w-full p-4 text-center text-black outline-none transition-all dark:text-white ${isActive ? 'bg-orange-base text-white' : ''}`
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
