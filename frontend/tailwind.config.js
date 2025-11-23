/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'user-color': '#3b82f6', // blue
        'llm-color': '#ef4444',  // red
      }
    },
  },
  plugins: [],
}
