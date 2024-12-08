import { GroupBase, StylesConfig } from 'react-select';

export const selectStyle = (
  isDark?: boolean,
  error?: boolean,
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
      border: error ? '1px solid #ef4444' : '1px solid #6b7280',
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
      border: '1px solid #fff',
      borderRadius: '6px',
      boxShadow: isDark
        ? '0 10px 10px 4px #000'
        : '0 5px 5px 2px rgba(0, 0, 0, 0.3)',
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
