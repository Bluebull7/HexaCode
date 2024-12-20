# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HexaCode'
copyright = '2024, Lance Henry'
author = 'Lance Henry'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "style_external_links": True,
    "titles_only": False,
}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
