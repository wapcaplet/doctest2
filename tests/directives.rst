Cleaner directives
==================

Directives are a bit ugly, and could be nicer-looking.

Currently, doctest accepts directives in a comment to the right of one of the
lines being tested::

    >>> print("foo\nbar") # doctest: +ELLIPSIS
    foo
    ...

This can get especially ugly with multiple long directives::

    >>> print("foo\n\nbar   baz") # doctest: +NORMALIZE_WHITESPACE, +REPORT_ONLY_FIRST_FAILURE
    foo
    bar baz

The directives can be included on a continuation line::

    >>> print("foo\n\nbar   baz")
    ... # doctest: +NORMALIZE_WHITESPACE, +REPORT_ONLY_FIRST_FAILURE
    foo
    bar baz

But not on a standalone line above the example::

    # doctest: +NORMALIZE_WHITESPACE, +REPORT_ONLY_FIRST_FAILURE
    >>> print("foo\n\nbar   baz")       # doctest: +SKIP
    foo
    bar baz

It might be nice if these directives could immediately precede the example in a
line marked as a comment. Because each directive begins with a ``+`` or ``-``,
the leading ``doctest:`` bit seems unnecessary::

    # +NORMALIZE_WHITESPACE, +REPORT_ONLY_FIRST_FAILURE
    >>> print("foo\n\nbar   baz")       # doctest: +SKIP
    foo
    bar baz

The all-caps keywords may be unnecessary as well::

    # +normalize_whitespace, +report_only_first_failure
    >>> print("foo\n\nbar   baz")       # doctest: +SKIP
    foo
    bar baz

