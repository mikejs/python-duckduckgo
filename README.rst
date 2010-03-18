==================
python-duckduckgo
==================

A Python library for querying the Duck Duck Go API.

Copyright Michael Stephens <me@mikej.st>, released under a BSD-style license.

Source: http://github.com/mikejs/python-duckduckgo

Installation
============

To install run

    ``python setup.py install``

Usage
=====

    >>> import duckduckgo
    >>> r = duckduckgo.query('Duck Duck Go')
    >>> r.type
    'answer'
    >>> r.results[0].text
    'Official site'
    >>> r.results[0].url
    'http://duckduckgo.com/'
    >>> r.abstract.url
    'http://en.wikipedia.org/wiki/Duck_Duck_Go'
    >>> r.abstract.source
    'Wikipedia'
    
    >>> r = duckduckgo.query('Python')
    >>> r.type
    'disambiguation'
    >>> r.related[6].text
    'Python (programming language), a computer programming language'
    >>> r.related[6].url
    'http://duckduckgo.com/Python_(programming_language)'

    >>> r = duckduckgo.query('1 + 1')
    >>> r.type
    'nothing'
    >>> r.answer.text
    '1 + 1 = 2'
    >>> r.answer.type
    'calc'
