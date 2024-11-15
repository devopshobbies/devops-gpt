import { ReactNode } from "react";

import {
  DrawerBackdrop,
  DrawerBody,
  DrawerCloseTrigger,
  DrawerContent,
  DrawerHeader,
  DrawerRoot,
  DrawerTitle,
} from "../external-ui/drawer";

interface Props {
  title: string;
  content: ReactNode;
  isOpen: boolean;
  onClose: () => void;
}

const Drawer = ({ title, content, isOpen, onClose }: Props) => {
  return (
    <DrawerRoot
      size="xs"
      placement="start"
      open={isOpen}
      onOpenChange={onClose}
    >
      <DrawerBackdrop />
      <DrawerContent>
        <DrawerHeader>
          <DrawerTitle>{title}</DrawerTitle>
        </DrawerHeader>
        <DrawerBody>{content}</DrawerBody>

        <DrawerCloseTrigger />
      </DrawerContent>
    </DrawerRoot>
  );
};

export default Drawer;
