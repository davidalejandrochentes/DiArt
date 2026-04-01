tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
colors: {
"primary": "#722F37",
"primary-dark": "#5C262D",
                "background-light": "#f8fafc",
                "background-dark": "#101622",
                "risk-high": "#dc2626",
                "risk-moderate": "#ea580c",
                "risk-minor": "#135bec",
                "success-green": "#16a34a",
                "slate-850": "#162032"
            },
            fontFamily: {
                "display": ["Inter", "system-ui", "sans-serif"]
            },
            borderRadius: {
                "DEFAULT": "0.25rem",
                "lg": "0.5rem",
                "xl": "0.75rem",
                "2xl": "1rem",
                "full": "9999px"
            },
            boxShadow: {
                'macbook': '0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(0, 0, 0, 0.8) inset',
                'card': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)',
            }
        },
    },
}
