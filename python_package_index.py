# PYPI

# google for packages in projects


# PIP

# search pypi on google and requests package
# pip3 install requests==2.9.0
# pip3 install requests==2.9.*
# pip3 uninstall requests
# pip3 install requests==2.*
from moshpdf import pdf2text
import requests
response = requests.get("https://google.com")
print(response)


# VIRTUAL ENVIRONMENTS


# PIPENV

# pip3 install pipenv
# pipenv install requests
# pipenv --venv
# ModuleNotFoundError: No module named 'requests'
# pipenv shell


# VIRTUAL ENVIRONMENTS IN VS CODE

# open /Users/rakesh/.local/share/virtualenvs/p1-oaqNYli-


# PIPFILE

# pipenv install --ignore-pipfile
# rm -rf /Users/rakesh/.local/share/virtualenvs/p1-oaqNYli-


# MANAGING DEPENDENCIES

# rakeshs-MacBook-Pro:p1 rakesh$ pipenv graph

# pylint==2.4.4
#   - astroid [required: >=2.3.0,<2.4, installed: 2.3.3]
#     - lazy-object-proxy [required: ==1.4.*, installed: 1.4.3]
#     - six [required: ~=1.12, installed: 1.13.0]
#     - wrapt [required: ==1.11.*, installed: 1.11.2]
#   - isort [required: >=4.2.5,<5, installed: 4.3.21]
#   - mccabe [required: >=0.6,<0.7, installed: 0.6.1]
# requests==2.22.0
#   - certifi [required: >=2017.4.17, installed: 2019.11.28]
#   - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
#   - idna [required: >=2.5,<2.9, installed: 2.8]
#   - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.7]

# pipenv updated --outdated
# pipenv update requests


# PUBLISHING PACKAGES


pdf2text.convert()


# DOCSTRINGS

# always document your library


# PYDOC

# pydoc3 moshpdf.moshpdf.pdf2text
# pydoc3 -w moshpdf.moshpdf.pdf2text
# open moshpdf.moshpdf.pdf2text.html
# pydoc3 -p 1234
