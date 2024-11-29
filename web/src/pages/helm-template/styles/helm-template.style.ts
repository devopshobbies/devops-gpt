import { GroupBase, StylesConfig } from 'react-select';

export const selectStyle:
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
  | undefined = {
  control: (styles) => ({
    ...styles,
    border: 'none',
    borderRadius: '6px',
    background: '#121212',
    height: '40px',
    color: '#fff',
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
    background: '#121212',
    border: 'none',
  }),
  option: (styles) => ({
    ...styles,
    background: '#121212',
    color: '#fff',
    ':hover': {
      background: '#f86609',
    },
  }),
  singleValue: (styles) => ({
    ...styles,
    color: '#fff',
  }),
};
