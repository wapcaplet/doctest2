Blank lines
===========

Allow a single period to represent ``<BLANKLINE>``

Issue #13: https://github.com/ianb/doctest2/issues/13

Sometimes we want to verify the presence of a blank line in output. The
official doctest handles this by accepting the ``<BLANKLINE>`` marker.

For example::

    >>> output = "\n".join(["Wait for it...", "", "", "Now!"])
    >>> print(output)
    Wait for it...
    <BLANKLINE>
    <BLANKLINE>
    Now!

This is a bit ugly; we'd also like to accept something a little less obtrusive
in place of the blank line. A single period has been suggested::

    >>> print(output)
    Wait for it...
    .
    .
    Now!

If you need to verify the literal presence of a single period in the output, you
can enable the `DONT_ACCEPT_BLANKLINE` flag::

    >>> output = "\n".join(["Literal periods", ".", "."])
    >>> print(output)   # doctest: +DONT_ACCEPT_BLANKLINE
    Literal periods
    .
    .

The same goes for the literal presence of the string `<BLANKLINE>`::

    >>> output = "\n".join(["Literal <BLANKLINE>", "<BLANKLINE>"])
    >>> print(output)   # doctest: +DONT_ACCEPT_BLANKLINE
    Literal <BLANKLINE>
    <BLANKLINE>

Or a mixture of the two::

    >>> output = "\n".join(["Literal period and <BLANKLINE>", ".", "<BLANKLINE>"])
    >>> print(output)   # doctest: +DONT_ACCEPT_BLANKLINE
    Literal period and <BLANKLINE>
    .
    <BLANKLINE>

