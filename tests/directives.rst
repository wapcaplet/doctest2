Cleaner directives
==================

Directives are a bit ugly, and could be nicer-looking.

Currently, doctest accepts directives in a comment to the right of one of the
lines being tested::

    >>> print("foo\nbar") # doctest: +ELLIPSIS
    foo
    ...

This can get especially ugly with multiple long directives::

    >>> print("foo\nbar") # doctest: +NORMALIZE_WHITESPACE, +DONT_ACCEPT_BLANKLINE
    foo
    bar

It might be nice if these directives could immediately precede the example in a
line marked as a comment. Because each directive begins with a ``+`` or ``-``,
the leading ``doctest:`` bit seems unnecessary::

    # +ELLIPSIS
    >>> print("foo\nbar")               # doctest: +SKIP
    foo
    ...

The all-caps keywords may be unnecessary as well::

    # +ellipsis
    >>> print("foo\nbar")               # doctest: +SKIP
    foo
    ...

