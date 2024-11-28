import { useNavigate } from 'react-router-dom';

import { MdKeyboardArrowDown, MdKeyboardArrowRight } from 'react-icons/md';

import { sidebarItems } from './SidebarItems';

const Sidebar = () => {
  const navigate = useNavigate();

  return (
    <div className="w-20 transition-all sm:w-80 border-r drop-shadow-sm h-full">
      {sidebarItems.map((item) => (
        <div
          className="cursor-pointer"
          key={item.route}
          onClick={() => navigate(item.route)}
        >
          <div className="px-4 py-4 flex justify-between text-lg hover:bg-orange-100">
            <div className="flex items-end w-full justify-center sm:justify-start">
              {<item.icon className="text-mainOrange-500 mr-2 size-6" />}
              <span className="hidden sm:inline">{item.label}</span>
            </div>
            {item.children ? (
              <MdKeyboardArrowDown className="size-6 text-mainOrange-500 hidden sm:block" />
            ) : null}
          </div>
          {item?.children ? (
            <div className="px-0 sm:px-6">
              {item.children.map((subItem) => (
                <div
                  key={subItem.label}
                  className="p-4 flex items-center text-lg hover:bg-orange-100 w-full justify-center sm:justify-start"
                  onClick={(e) => {
                    e.stopPropagation();
                    navigate(subItem.route);
                  }}
                >
                  <MdKeyboardArrowRight className="text-mainOrange-500 mr-2 size-6 hidden sm:block" />
                  <subItem.icon className="text-mainOrange-500 mr-2 size-6" />
                  <span className="hidden sm:inline">{subItem.label}</span>
                </div>
              ))}
            </div>
          ) : null}
        </div>
      ))}
    </div>
  );
};

export default Sidebar;
