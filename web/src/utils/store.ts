import { create } from "zustand";

const inistialState = {};

export const useGptStore = create((set, get) => ({
  ...inistialState,
}));
