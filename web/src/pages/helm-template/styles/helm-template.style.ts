import { GroupBase, StylesConfig } from 'react-select';

export const selectStyle = (
  isDark?: boolean,
):
  | StylesConfig<
      {
        label: string;
        value: string;
      },
      false,
      GroupBase<{
        label: string;
        value: string;
      }>
    >
  | undefined => {
  return {
    control: (styles) => ({
      ...styles,
      border: isDark ? 'none' : '1px solid #e3e3e3',
      borderRadius: '6px',
      background: isDark ? '#121212' : '#fff',
      color: isDark ? '#fff' : '#121212',
      height: '40px',
      ':focus-within': {
        border: 'none',
        boxShadow: '0 0 0 1px #f86609',
      },
      ':active': {
        border: 'none',
      },
    }),
    menu: (styles) => ({
      ...styles,
      background: isDark ? '#121212' : '#fff',
      border: 'none',
    }),
    option: (styles) => ({
      ...styles,
      background: isDark ? '#121212' : '#fff',
      color: isDark ? '#fff' : '#121212',
      ':hover': {
        background: '#f86609',
      },
    }),
    singleValue: (styles) => ({
      ...styles,
      color: isDark ? '#fff' : '#121212',
    }),
  };
};
