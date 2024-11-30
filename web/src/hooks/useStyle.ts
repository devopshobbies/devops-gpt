import { create } from 'zustand';

interface StyleSlice {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

const useStyle = create<StyleSlice>((set) => ({
  darkMode: localStorage.getItem('theme') === 'dark',
  toggleDarkMode: () => {
    const theme = localStorage.getItem('theme') === 'dark' ? 'light' : 'dark';
    set({ darkMode: theme === 'dark' });
  },
}));

export default useStyle;
