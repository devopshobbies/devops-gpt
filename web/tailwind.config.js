/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: ["./src/**/*.{html,js,ts,tsx,jsx}"],
  theme: {
    extend: {
      fontFamily: {
        figtree: ['figtree', 'sans-serif']
      },
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        orange: {
          base: "#f86609"
        },
      }
    }
  },
  plugins: [require("tailwindcss-animate"), require('daisyui')],
}

