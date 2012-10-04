This is a fork of Ian Bicking's `doctest2`_ repository. After reading his `blog
post about doctest.js`_, I was inspired to dive in and start looking for ways I
could help. I think doctest is one of Python's greatest features, but I agree
with Ian that there are many wrinkles and warts.

I'll see how far I can get on my own, but I would welcome any assistance. I plan
to keep an eye on any forks of Ian's project, to avoid any duplication of
effort.


Goals
-----

- Make doctest more awesome
- Retain backward compatibility with existing doctest behavior


Plan
----

- Use doctest-driven development
- Initially ``+SKIP`` any features that aren't implemented
- Take out ``+SKIP`` directives as things get finished


Testing
-------

For now, just run the test script::

    $ python test.py

This covers all files in the ``tests`` directory, as well as doctests in
``doctest2.py`` itself.


.. _doctest2: http://github.com/ianb/doctest2
.. _issues: http://github.com/ianb/doctest2/issues
.. _blog post about doctest.js: http://blog.ianbicking.org/2012/10/02/why-doctest-js-is-better-than-pythons-doctest/

