import daisyui from 'daisyui';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        mainOrange: {
          500: '#fe6601',
        },
      },
    },
  },
  plugins: [daisyui, require('tailwind-scrollbar')],
};
