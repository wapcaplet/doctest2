Ellipses
========

Improve support for ellipses for ignoring part of the output.

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

This can cause problems when attempting to match arbitrary text at the beginning
of the output, because the ``...`` is interpreted as a continuation, rather than
an ellipsis::

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

There is the aesthetic ugliness of including the ``+ELLIPSIS`` directive. Anyone
reading your documentation can tell from the context what ``...`` means, so
doctest should be able to as well.


Solution
--------

We would like to have a new ellipsis marker that:

- Does not conflict with the continuation prompt ``...``
- Does not greedily match too much
- Does not require including an ``+ELLIPSIS`` directive

Using a new marker such as ``<...>`` could solve the first two problems, while
the third could, one hopes, be handled with a bit of regexp cleverness.

A few essential behaviors could be outlined as follows. First, the new ellipsis
marker should be able to match all output::

    >>> print(menu)         # doctest: +ELLIPSIS
    <...>

This would be equivalent to::

    >>> print(menu)         # doctest: +ELLIPSIS, +SKIP
    ...

...if that actually worked. While not much of a doctest, this allows executing
code that may produce arbitrary output, but whose output you aren't interested
in testing (either because it's too long, or because it's outside the scope of
what you hope to document and test in the example).

Another essential behavior is for the ellipsis to match no output, or the empty
string. Again, perhaps you're testing something that may or may not produce
output; maybe it's a nondeterministic function::

    >>> import random
    >>> def meal():
    ...     if random.choice([True, False]):
    ...         print("Baked beans")
    ...     print("Spam")

You could still test to make sure you get "Spam", regardless of whether "Baked
beans" appears::

    >>> meal()          # doctest: +SKIP
    <...>
    Spam

More often, we'll want it to match one or more lines. We may only care about
the first few lines of the output::

    >>> print(menu) # this one's OK to have a comment here
    Spam
    <...>

    >>> print(menu)
    Spam
    Spam
    <...>

    >>> print(menu)
    Spam
    Spam
    Eggs
    <...>

Or something in the middle::

    >>> print(menu)
    <...>
    Eggs
    <...>

    >>> print(menu)
    <...>
    Spam
    <...>

    >>> print(menu)
    <...>
    Spam
    Eggs
    <...>

Or only the end::

    >>> print(menu)
    <...>
    Spam

    >>> print(menu)
    <...>
    Eggs
    Spam

Maybe even just the beginning and the end::

    >>> print(menu)
    Spam
    <...>
    Spam

    >>> print(menu)
    Spam
    Spam
    <...>
    Spam

    >>> print(menu)
    Spam
    <...>
    Eggs
    Spam


Embedded ellipses
-----------------

One thing that the ``+ELLIPSIS`` directive allows is matching of substrings
within a line; for example::

    >>> items = ["Spam", "Egg", "Sausage", "Spam"]

    >>> items               # doctest: +ELLIPSIS
    ['Spam', ..., 'Spam']

This would be a bit ugly using the new ``<...>`` marker::

    >>> items
    ['Spam', <...>, 'Spam']

In this context, ``...`` would not be confused with the continuation marker, so
it might be possible to simply handle it automatically, without needing the
``+ELLIPSIS`` directive::

    >>> items               # doctest: +SKIP
    ['Spam', ..., 'Spam']

