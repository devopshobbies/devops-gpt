import { GroupBase, StylesConfig } from 'react-select';

export const selectStyle = (
  controlRadius: string,
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
      border: 'none',
      borderRadius: controlRadius,
      background: isDark ? '#121212' : '#fff',
      color: isDark ? '#fff' : '#121212',
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
        color: '#fff',
      },
    }),
    singleValue: (styles) => ({
      ...styles,
      color: isDark ? '#fff' : '#121212',
    }),
  };
};
