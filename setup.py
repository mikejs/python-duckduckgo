from distutils.core import setup
from duckduckgo import __version__

long_description = open('README.rst').read()

setup(name='duckduckgo',
      version=__version__,
      py_modules=['duckduckgo'],
      description='Library for querying the Duck Duck Go API',
      author='Michael Stephens',
      author_email='me@mikej.st',
      license='BSD',
      url='http://github.com/mikejs/python-duckduckgo/',
      long_description=long_description,
      platforms=['any'],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
                   ],
      )
