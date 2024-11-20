import { create } from "zustand";
import { Endpoints, UserType } from "../features/constants";
import { Message } from "../features/model";

interface GeneratorQuery {
  isSuccess: boolean;
  endpoint: Endpoints | "";
}

interface DevOpsStore {
  isOpen: boolean;
  setIsOpen: (bool: boolean) => void;

  messages: Message[];
  addMessage: (user: UserType, content: string, id: string) => void;

  resetMessages: () => void;

  generatorQuery: GeneratorQuery;
  setGeneratorQuery: (isSuccess: boolean, endpoint: Endpoints | "") => void;
}

const initialState: Pick<
  DevOpsStore,
  "isOpen" | "messages" | "generatorQuery"
> = {
  isOpen: false,
  generatorQuery: { isSuccess: false, endpoint: "" },
  messages: [],
};

const useGptStore = create<DevOpsStore>((set) => ({
  ...initialState,
  setIsOpen: (bool) => set({ isOpen: bool }),
  addMessage: (user, content, id) =>
    set((state) => ({
      messages: [...state.messages, { user, content, id }],
    })),
  resetMessages: () => set({ messages: [] }),
  setGeneratorQuery: (bool, endpoint) =>
    set({ generatorQuery: { isSuccess: bool, endpoint: endpoint } }),
}));

export default useGptStore;
