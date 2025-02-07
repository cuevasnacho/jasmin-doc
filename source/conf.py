# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jasmin'
copyright = '2025, Jasmin contributors'
author = 'The Jasmin developer team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_rtd_theme"]

myst_enable_extensions = ['colon_fence']

# templates_path = ['_templates']
# exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
  'sticky_navigation': False
}
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "lyonel2017", # Username
    "github_repo": "jasmin-doc", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}
# html_static_path = ['_static']
