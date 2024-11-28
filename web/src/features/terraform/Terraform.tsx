import { useNavigate } from 'react-router-dom';
import { terraformServices } from '../../layouts/Sidebar/SidebarItems';

const Terraform = () => {
  const navigate = useNavigate();

  return (
    <div className="flex gap-4 flex-wrap justify-center items-center pt-16">
      {terraformServices.map((service) => (
        <div
          key={service.label}
          onClick={() => navigate(service.route)}
          className="border-orange-300 w-40 cursor-pointer flex flex-col items-center gap-4 border p-4 text-mainOrange-500 rounded-md hover:bg-orange-100"
        >
          <service.icon className="size-12" />
          <div className="font-bold">{service.label}</div>
        </div>
      ))}
    </div>
  );
};

export default Terraform;
