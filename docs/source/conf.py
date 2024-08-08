from datetime import datetime

# pylint: disable=W0622

project = 'Ansible Collection - Systemd'
copyright = f'{datetime.now().year}, AnsibleGuy'
author = 'AnsibleGuy'
extensions = ['piccolo_theme']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_logo = 'https://brand.systemd.io/assets/svg/systemd-dark.svg'
html_favicon = '_static/img/favicon.png'
html_css_files = ['css/main.css']
master_doc = 'index'
display_version = True
sticky_navigation = True
source_suffix = {
    '.rst': 'restructuredtext',
}
html_theme_options = {
    'banner_text': '<a href="https://github.com/ansibleguy/collection_systemd">Repository on GitHub</a> | '
                   '<a href="https://github.com/ansibleguy/collection_systemd/issues/new/choose">Report errors</a>'
}
html_short_title = 'Ansible Systemd'
