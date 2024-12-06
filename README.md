# HexaCode Playground

HexaCode is a custom French-based programming language designed for educational and creative purposes. The HexaCode Playground provides an intuitive web-based environment to write and execute HexaCode scripts, along with hosted documentation to help you get started.

## Features

- **French-Based Programming Language**: Simple commands like `AFFICHE`, `SI`, and `ALORS` make it easy to learn and use.
- **Interactive Playground**: Write, run, and debug HexaCode scripts in your browser.
- **Hosted Documentation**: Comprehensive docs are available at `/docs` to guide users through HexaCode's syntax and features.
- **Modular Structure**: Clean separation of backend (Flask), frontend (React), and documentation (Sphinx).
- **Responsive Design**: The playground is optimized for both desktop and mobile users.

---

## Project Structure

```plaintext
HexaCode/
├── backend/                        # Flask backend
│   ├── app/
│   │   ├── __init__.py             # Flask app factory
│   │   ├── routes.py               # API routes
│   │   ├── interpreter.py          # HexaCode logic (tokenize/execute)
│   │   ├── utils.py                # Utility functions (optional)
│   ├── static_docs/                # Sphinx-generated documentation
│   │   ├── index.html              # Documentation index
│   │   ├── _static/                # Static assets (CSS, JS, etc.)
│   │   ├── _sources/               # ReStructuredText sources
│   └── app.py                      # Backend entry point
│
├── docs/                           # Sphinx source files
│   ├── _build/                     # Built documentation (HTML, etc.)
│   ├── conf.py                     # Sphinx configuration
│   ├── index.rst                   # Documentation index
│   ├── introduction.rst            # Introduction section
│   ├── usage.rst                   # Usage section
│   ├── api-reference.rst           # API reference
│   └── contributing.rst            # Contribution guide
│
├── frontend/                       # React frontend
│   ├── public/                     # Static assets
│   │   ├── index.html              # Main HTML template
│   │   ├── favicon.ico             # Favicon
│   │   └── manifest.json           # Manifest for PWA
│   ├── src/                        # React source files
│   │   ├── components/             # React components
│   │   │   ├── Editor.jsx          # Editor component
│   │   │   ├── Console.jsx         # Console component
│   │   │   └── Header.jsx          # Header/NavBar component
│   │   ├── App.js                  # Main React app
│   │   ├── index.js                # React entry point
│   │   ├── styles.css              # Global styles
│   │   └── utils/                  # Helper functions (optional)
│   ├── package.json                # React dependencies and scripts
│   └── package-lock.json           # Lockfile for React dependencies
│
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
├── README.md                       # Project README
└── LICENSE                         # Project license (optional)
