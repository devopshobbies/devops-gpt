import { create } from "zustand";
import { UserType } from "../features/constants";

interface Message {
  user: UserType;
  content: string;
}

interface DevOpsStore {
  isOpen: boolean;
  setIsOpen: (bool: boolean) => void;

  messages: Message[];
  addMessage: (user: UserType, content: string) => void;
}

const initialState: Pick<DevOpsStore, "isOpen" | "messages"> = {
  isOpen: true,
  messages: [],
};

const useGptStore = create<DevOpsStore>((set) => ({
  ...initialState,
  setIsOpen: (bool) => set({ isOpen: bool }),
  addMessage: (user, content) =>
    set((state) => ({
      messages: [...state.messages, { user, content }],
    })),
}));

export default useGptStore;
