from setuptools import setup

import datetime
import codecs
import os

major = 0
minor = 1

timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
version = f"{major}.{minor}.{timestamp}"

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()
    
setup(
  name = 'renderlab',
  version = version,
  license = 'MIT',
  description = 'Render Gymnasium environments in Google Colaboratory',
  long_description_content_type = "text/markdown",
  long_description = long_description,
  author = 'Ryan Rudes',
  author_email = 'ryanrudes@gmail.com',
  url = 'https://github.com/ryanrudes/renderlab',
  keywords = ['colab', 'gym', 'gymnasium', 'render', 'openai', 'rl'],
  packages = ['renderlab'],
  install_requires = ['moviepy', 'gymnasium'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)
