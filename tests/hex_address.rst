Hex addresses
=============

Allow ``0xXXX`` to match hexadecimal memory addresses.

Issue #4: https://github.com/ianb/doctest2/issues/4

It's difficult to verify any output that might include a hexadecimal memory
address. For example, given a class instance::

    >>> class Foo:
    ...     pass
    >>> foo = Foo()

The default ``repr`` for the instance contains an unpredictable hexadecimal
value::

    >>> print(foo)                          # doctest: +SKIP
    <__main__.Foo instance at 0x13c1638>

We might like to verify the format of the output without caring what specific
hexadecimal value is here, for example like this::

    >>> print(foo)                          # doctest: +SKIP
    <__main__.Foo instance at 0xXXX>


