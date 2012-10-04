Ellipses
========

Allow the use of ellipses to ignore part of the output.

Issue #14: https://github.com/ianb/doctest2/issues/14

Problem
-------

Given some multi-line text::

    >>> menu = "\n".join(["Spam", "Spam", "Eggs", "Spam"])

We may want to write a doctest that ignores some part of the result.
For example, without special directives, we would have to verify the full
output::

    >>> print(menu)
    Spam
    Spam
    Eggs
    Spam

Or, using the ``+ELLIPSIS`` directive, we can ignore parts of it::

    >>> print(menu)      # doctest: +ELLIPSIS
    Spam
    ...

    >>> print(menu)      # doctest: +ELLIPSIS
    Spam
    Spam
    ...

    >>> print(menu)      # doctest: +ELLIPSIS
    Spam
    Spam
    Eggs
    ...

    >>> print(menu)      # doctest: +ELLIPSIS
    Spam
    ...
    Spam

    >>> print(menu)      # doctest: +ELLIPSIS
    Spam
    ...
    Eggs
    Spam

But there are some problems with the existing ellipsis marker. For starters, it
is identical to the continuation prompt ``...``, as in::

    >>> def foo():
    ...     return 'foo'

It is also greedy, sometimes matching too much. For example, these examples
fail because the ellipsis swallows up the ending lines before they can be
matched::

    >>> print(menu)      # doctest: +ELLIPSIS, +SKIP
    ...
    Spam

    >>> print(menu)      # doctest: +ELLIPSIS, +SKIP
    ...
    Eggs
    Spam

    >>> print(menu)      # doctest: +ELLIPSIS, +SKIP
    ...
    Spam
    Eggs
    Spam

Finally, there is the aesthetic ugliness of including the ``+ELLIPSIS``
directive. Anyone reading your documentation can tell from the context what
``...`` means, so doctest should be able to as well.


Solution
--------

We would like to have a new ellipsis marker that:

    - Does not conflict with the continuation prompt ``...``
    - Does not greedily match too much
    - Does not require including an ``+ELLIPSIS`` directive

Using a new marker such as ``(...)`` could solve the first two problems, while
the third could, one hopes, be handled with a bit of regexp cleverness.

A few essential behaviors could be outlined as follows. First, the new ellipsis
marker should be able to match all output::

    >>> print(menu)         # doctest: +SKIP
    (...)

This would be equivalent to::

    >>> print(menu)         # doctest: +ELLIPSIS, +SKIP
    ...

...if that actually worked. While not much of a doctest, this allows executing
code that may produce arbitrary output, but whose output you aren't interested
in testing (either because it's too long, or because it's outside the scope of
what you hope to document and test in the example).

Another essential behavior is for the ellipsis to match no output, or the empty
string. Again, perhaps you're testing something that may or may not produce
output, but your test doesn't care whether it does::

    >>> print(menu)         # doctest: +SKIP
    (...)
    Spam
    Spam
    Eggs
    Spam

    >>> print(menu)         # doctest: +SKIP
    (...)
    Spam
    Spam
    Eggs
    Spam
    (...)

    >>> print(menu)         # doctest: +SKIP
    Spam
    Spam
    (...)
    Eggs
    Spam

    >>> print(menu)         # doctest: +SKIP
    Spam
    Spam
    Eggs
    Spam
    (...)

More often, we'll want it to match one or more lines. We may only care about
the first few lines of the output::

    >>> print(menu)         # doctest: +SKIP
    Spam
    (...)

    >>> print(menu)         # doctest: +SKIP
    Spam
    Spam
    (...)

    >>> print(menu)         # doctest: +SKIP
    Spam
    Spam
    Eggs
    (...)

Or something in the middle::

    >>> print(menu)         # doctest: +SKIP
    (...)
    Eggs
    (...)

    >>> print(menu)         # doctest: +SKIP
    (...)
    Spam
    (...)

    >>> print(menu)         # doctest: +SKIP
    (...)
    Spam
    Eggs
    (...)

Or only the end::

    >>> print(menu)         # doctest: +SKIP
    (...)
    Spam

    >>> print(menu)         # doctest: +SKIP
    (...)
    Eggs
    Spam

Maybe even just the beginning and the end::

    >>> print(menu)         # doctest: +SKIP
    Spam
    (...)
    Spam

    >>> print(menu)         # doctest: +SKIP
    Spam
    Spam
    (...)
    Spam

    >>> print(menu)         # doctest: +SKIP
    Spam
    (...)
    Eggs
    Spam


