project = 'pcmaticlogin'
author = 'pcmaticlogin'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Bing search verification
html_context = {
    'bing_verification_code': 'EE6D4DD82CF6C5ED2AF3667411F585D7'
}

# Base URL for sitemap
html_baseurl = 'https://pcmaticlogin.readthedocs.io/en/latest/'
