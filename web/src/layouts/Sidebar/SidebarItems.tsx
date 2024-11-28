import { SiTerraform } from 'react-icons/si';
import { FaBug } from 'react-icons/fa6';
import { SiHelm } from 'react-icons/si';
import { FaGear } from 'react-icons/fa6';
import { MdInstallDesktop } from 'react-icons/md';
import { FaDocker } from 'react-icons/fa';
import { SiAmazonec2 } from 'react-icons/si';
import { SiAmazons3 } from 'react-icons/si';
import { SiAmazoniam } from 'react-icons/si';
import { SiArgo } from 'react-icons/si';
import { routes, terraformRoutes } from '../../utils/routing';

export const terraformServices = [
  {
    label: 'Docker Service',
    route: terraformRoutes.dockerService,
    icon: FaDocker,
  },
  {
    label: 'EC2 Service',
    route: terraformRoutes.ec2Service,
    icon: SiAmazonec2,
  },
  {
    label: 'S3 Service',
    route: terraformRoutes.s3Service,
    icon: SiAmazons3,
  },
  {
    label: 'IAM Service',
    route: terraformRoutes.iamService,
    icon: SiAmazoniam,
  },
  {
    label: 'ArgoCD Service',
    route: terraformRoutes.argocdService,
    icon: SiArgo,
  },
];

export const sidebarItems = [
  {
    label: 'Basic',
    icon: FaGear,
    route: routes.basicGen,
  },
  {
    label: 'Bug Fix',
    icon: FaBug,
    route: routes.bugFix,
  },
  {
    label: 'Terraform Template',
    icon: SiTerraform,
    route: routes.terraformTemplate,
    children: terraformServices,
  },
  {
    label: 'Installation',
    icon: MdInstallDesktop,
    route: routes.installation,
  },
  {
    label: 'HelmTemplate',
    icon: SiHelm,
    route: routes.helmTemplate,
  },
];
