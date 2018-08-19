# asyncionext
A collection of features proposed for the asyncio standard library for Python.

Commentary is welcome as GitHub issues. Contributions are welcome in the form of
pull requests provided that you have copyright claim over the contributed code
or can at least vouch for the code's eligibility to be licensed or relicensed
under the terms of the Apache License Version 2.0.

The project currently uses the [aiofiles](https://github.com/Tinche/aiofiles)
library as implementation for file I/O features. In order to function as a
reference implementation, this library may eventually incorporate or
re-implement code from aiofiles.


## Proposed Additions to the Asyncio Module
* asyncio.input
* asyncio.open
* asyncio.stat

Note: now that sendfile was accepted in Python 3.7, asyncio.os might not make
sense as a submodule anymore.

### _coroutine_ `asyncionext.input([prompt], [loop], [executor]])`
If the prompt argument is present, it is written to standard output without a
trailing newline. The function asynchronously awaits a line from input, converts
it to a string (stripping a trailing newline), and returns that. Example:

    >>> s = await input('--> ')  
    --> Monty Python's Flying Circus
    >>> s  
    "Monty Python's Flying Circus"

A future implementation might choose to not use an executor when one is not
passed in and features are available from the operating system that either
implement threads more efficiently or operate in the main thread.

### _coroutine_ `asyncionext.open(filename, [loop], [executor])`
Like the open built-in function, except is awaitable and returns a file-like
object with several methods exposed as coroutines. This implementation uses the
passed in executor or the event loop's default executor. A future implementation
might choose to not use an executor when one is not passed in and a features are
available from the operating system that either implement threads more
efficiently or operate in the main thread.

### _coroutine_ `asyncionext.stat(path, *, dir_fd=None, follow_symlinks=True, [loop], [executor])`
Get the status of a file or a file descriptor. Perform the equivalent of a
`stat()` system call on the given path. path may be specified as either a string
or bytes – directly or indirectly through the PathLike interface – or as an open
file descriptor. Return a stat_result object.

This function normally follows symlinks; to stat a symlink add the argument
follow_symlinks=False, or use lstat().

This function can support specifying a file descriptor and not following
symlinks.


## Alternate Layout
If the asyncio module suffers from namespace fatigue, asyncio can be split into
submodules for the major categories of input and output in Python 4.
* asyncio.files.open
* asyncio.files.open_fd
* asyncio.files.stat
* asyncio.net.open_connection
* asyncio.net.open_unix_connection
* asyncio.net.start_server
* asyncio.net.start_unix_server
* asyncio.process.create_subprocess_exec
* asyncio.process.create_subprocess_shell


## Rights
Copyright is reserved by Justin Turner Arthur and contributors to this project.
In the event a formal Python Enhancement Proposal is submitted or in
the event this project's contents are included in a Pull Request to the CPython
project, this project's contents will be licensed to the Python Software
Foundation under the terms of the Apache License Version 2.0.
