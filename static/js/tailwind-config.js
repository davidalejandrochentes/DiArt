tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#722F37",
          light: "#9B4D57",
          dark: "#5C262D",
          50: "#FDF2F3",
          100: "#FAE5E7",
          200: "#F5CBCF",
          300: "#EBA1A8",
          400: "#E07782",
          500: "#722F37",
          600: "#5C262D",
          700: "#481F24",
          800: "#35171A",
          900: "#230E11",
        },
        accent: {
          gold: "#D4AF37",
          rose: "#E8A4B8",
          cream: "#FFF8F0",
        },
        glass: {
          light: "rgba(255, 255, 255, 0.7)",
          dark: "rgba(114, 47, 55, 0.2)",
        },
        "background-light": "#f8fafc",
        "background-dark": "#101622",
        "risk-high": "#dc2626",
        "risk-moderate": "#ea580c",
        "risk-minor": "#135bec",
        "success-green": "#16a34a",
        "slate-850": "#162032"
      },
      fontFamily: {
        display: ["Inter", "system-ui", "sans-serif"],
        heading: ["Cormorant Garamond", "serif"],
        accent: ["Space Grotesk", "sans-serif"],
      },
      borderRadius: {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "2xl": "1rem",
        "3xl": "1.5rem",
        "full": "9999px"
      },
      boxShadow: {
        'macbook': '0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(0, 0, 0, 0.8) inset',
        'card': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)',
        'glow-sm': '0 0 20px rgba(114, 47, 55, 0.3)',
        'glow-md': '0 0 40px rgba(114, 47, 55, 0.4)',
        'glow-lg': '0 0 60px rgba(114, 47, 55, 0.5)',
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'float-slow': 'float 8s ease-in-out infinite',
        'glow-pulse': 'glow-pulse 2s ease-in-out infinite',
        'shimmer': 'shimmer 2s linear infinite',
        'border-flow': 'border-flow 3s ease infinite',
        'gradient-shift': 'gradient-shift 4s ease infinite',
        'fade-up': 'fade-up 0.6s ease-out forwards',
        'scale-in': 'scale-in 0.5s ease-out forwards',
        'slide-down': 'slideDown 0.3s ease-out',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        'glow-pulse': {
          '0%, 100%': { boxShadow: '0 0 20px rgba(114, 47, 55, 0.4)' },
          '50%': { boxShadow: '0 0 40px rgba(114, 47, 55, 0.6)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '200% 0' },
          '100%': { backgroundPosition: '-200% 0' },
        },
        'border-flow': {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
        'gradient-shift': {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
        'fade-up': {
          '0%': { opacity: '0', transform: 'translateY(30px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        'scale-in': {
          '0%': { opacity: '0', transform: 'scale(0.9)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        slideDown: {
          from: { opacity: '0', transform: 'translateY(-10px)' },
          to: { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
}
