doctest2
========

This project is an effort to make Python's doctest_ module more awesome.


Goals
-----

- Iron out some of the wrinkles and warts in Python's doctest_
- Retain backward compatibility with existing doctest behavior
- Distribute as a package installable with pip_
- Eventually propose a merge into the standard Python distribution


Plan
----

- Use doctest-driven development
- Initially ``+SKIP`` any features that aren't implemented
- Take out ``+SKIP`` directives as things get finished


Testing
-------

Testing is mostly done with nose_ at the moment. Tests are in the ``tests``
directory, and nose configuration is in ``setup.cfg``. Run nose like this::

    $ nosetests

There is also a quick-and-dirty ``test.py`` script designed to cover the
``doctest2.py`` file itself, as well as the ``tests/rst/*.rst`` files that
describe new features. These should be merged into the nose tests if possible.


Credits
-------

- `Ian Bicking`_ got it started
- `Eric Pierce`_ is continuing it


License
-------

This software is licensed under the Python Software Foundation License
(`PSFL`_).

.. _doctest: http://docs.python.org/library/doctest.html
.. _pip: http://www.pip-installer.org/en/latest/index.html
.. _nose: https://nose.readthedocs.org/en/latest/
.. _Ian Bicking: http://ianbicking.appspot.com/
.. _Eric Pierce: http://github.com/wapcaplet
.. _issues: http://github.com/wapcaplet/doctest2/issues
.. _PSFL: http://docs.python.org/license.html
