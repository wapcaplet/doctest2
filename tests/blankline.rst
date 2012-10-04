Blank lines
===========

Allow a single period to represent ``<BLANKLINE>``

Issue #13: https://github.com/ianb/doctest2/issues/13

Sometimes we want to verify the presence of a blank line in output. The
official doctest handles this by accepting the ``<BLANKLINE>`` marker.

For example::

    >>> output = "\n".join(["Wait for it...", "", "Now!"])
    >>> print(output)
    Wait for it...
    <BLANKLINE>
    Now!

This is a bit ugly; we'd also like to accept something a little less obtrusive
in place of the blank line. A single period has been suggested::

    >>> print(output)       # doctest: +SKIP
    Wait for it...
    .
    Now!


