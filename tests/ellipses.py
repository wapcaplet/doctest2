"""Allow the use of ellipses to ignore part of the output.

Given some multi-line text:

    >>> menu = "\n".join(["Spam", "Spam", "Eggs", "Spam"])

We may want to write a doctest that ignores some part of the result.
For example, ordinarily we would have to verify the full output::

    >>> print(menu)
    Spam
    Spam
    Eggs
    Spam

But perhaps we're only interested in verifying a subset of the output; we may
wish to ignore lines at the beginning, middle or end. For this, we will use
ellipses ``(...)``, parenthesized in order to distinguish it from the ``...``
that normally means continuation of code on the next line.

The ellipses should match zero or more lines of expected output. In this
example, it could match zero lines in any of several ways::

    >>> print(menu)
    (...)
    Spam
    Spam
    Eggs
    Spam

    >>> print(menu)
    (...)
    Spam
    Spam
    Eggs
    Spam
    (...)

    >>> print(menu)
    Spam
    Spam
    (...)
    Eggs
    Spam

    >>> print(menu)
    Spam
    Spam
    Eggs
    Spam
    (...)

More often, we'll want it to match one or more lines. We may only care about
the first few lines of the output::

    >>> print(menu)
    Spam
    (...)

    >>> print(menu)
    Spam
    Spam
    (...)

    >>> print(menu)
    Spam
    Spam
    Eggs
    (...)

Or something in the middle::

    >>> print(menu)
    (...)
    Eggs
    (...)

    >>> print(menu)
    (...)
    Spam
    (...)

    >>> print(menu)
    (...)
    Spam
    Eggs
    (...)

Or only the end::

    >>> print(menu)
    (...)
    Spam

    >>> print(menu)
    (...)
    Eggs
    Spam

Maybe even just the beginning and the end::

    >>> print(menu)
    Spam
    (...)
    Spam

    >>> print(menu)
    Spam
    Spam
    (...)
    Spam

    >>> print(menu)
    Spam
    (...)
    Eggs
    Spam

The pathological case is when we want to ignore all output::

    >>> print(menu)
    (...)

While not much of a doctest, this allows executing code that may be necessary
to prepare upcoming doctests, but which may produce output you aren't
interested in.
"""

