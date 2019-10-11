#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TEMP_PACKAGE documentation build configuration file, created by
# sphinx-quickstart on Fri Jan  5 14:20:43 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# NOTE:
# pip install sphinx_rtd_theme
# is needed in order to build the documentation
import os
import sys
# this line is needed, if the TEMP_PACKAGE is not installed
sys.path.insert(0, os.path.abspath("../../"))

from TEMP_PACKAGE import __version__ as ver


def skip(app, what, name, obj, skip, options):
    if name in ["__call__"]:
        return False
    return skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",  # parameters look better than with numpydoc only
    "numpydoc",
]

# autosummaries from source-files
autosummary_generate = True
# dont show __init__ docstring
autoclass_content = "class"
# sort class members
autodoc_member_order = "groupwise"
# autodoc_member_order = 'bysource'

# don't add full path to module
add_module_names = False

# Notes in boxes
napoleon_use_admonition_for_notes = True
# Attributes like parameters
# napoleon_use_ivar = True
# this is a nice class-doc layout
numpydoc_show_class_members = True
# class members have no separate file, so they are not in a toctree
numpydoc_class_members_toctree = False
# for the covmodels alot of classmembers show up...
numpydoc_show_inherited_class_members = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
# --> this is the sitemap (or content-list in latex -> needs a heading)
# for html: the quickstart (in index.rst)
# gets the "index.html" and is therefore opened first
master_doc = "contents"

# General information about the project.
project = "TEMP_PACKAGE"
copyright = "2019, YOUR_NAME"
author = "YOUR_NAME"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ver
# The full version, including alpha/beta/rc tags.
release = ver

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    #    'canonical_url': '',
    #    'analytics_id': '',
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "top",
    #    'style_external_links': False,
    #    'vcs_pageview_mode': '',
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "TEMP_PACKAGEdoc"


# -- Options for LaTeX output ---------------------------------------------
# latex_engine = 'lualatex'
# logo to big

## add a LOGO
# latex_logo = "pics/logo.png"

# latex_show_urls = 'footnote'
# http://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
latex_elements = {
    "preamble": r"""
\setcounter{secnumdepth}{1}
\setcounter{tocdepth}{2}
\pagestyle{fancy}
""",
    "pointsize": "10pt",
    "papersize": "a4paper",
    "fncychap": "\\usepackage[Glenn]{fncychap}",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "TEMP_PACKAGE.tex",
        "TEMP_PACKAGE Documentation",
        "YOUR_NAME",
        "manual",
    )
]
# latex_use_parts = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "TEMP_PACKAGE", "TEMP_PACKAGE Documentation", [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "TEMP_PACKAGE",
        "TEMP_PACKAGE Documentation",
        author,
        "TEMP_PACKAGE",
        "A Python TEMP_PACKAGE.",
        "Miscellaneous",
    )
]

suppress_warnings = [
    "image.nonlocal_uri",
    #    'app.add_directive',  # this evtl. suppresses the numpydoc induced warning
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "Python 3.6": ("https://docs.python.org/3.6", None),
    "Python": ("https://docs.python.org/", None),
    "NumPy": ("http://docs.scipy.org/doc/numpy/", None),
    "matplotlib": ("http://matplotlib.org", None),
    "Sphinx": ("http://www.sphinx-doc.org/en/stable/", None),
}