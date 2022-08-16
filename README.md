# python3-coding-exercise

I was given the following exercise: Write a ~10 lines long function in Python 3 that you would
consider as ideal code, and explain why it is ideal?

Note that I went straight to docs.python.org for tutorials as I have never coded in Python before. I
am a quick study, and have looked it over in the past and found it to borrow elements from many
other languages that I have written in, including Perl, PHP, and CoffeeScript.

Please find herein a simple function that is exactly ten lines as my submission of "ideal". This can
be executed simply with `python3 api_client.py`. I chose to use a mini-representation of something
that would be useful in the world of back-end systems automation and integration: a script that may
receive some data from one source and pass it to another destination by way of a RESTful HTTP API interface.

I used this opportunity to explore python3 beyond simply writing a function, but also to understand
code structure, imports, CLI invocation, Class structures/methods, possible approaches to dependency
injection, iteration, http request/response handling, regular expression string processing, and
formatting output for print/logging.

To me, the "ideal" aspects of the send_events() function are:
 * Comments that express intent rather than simply reword the code statements
 * Concise code that eliminates redundant statements without being too clever or difficult to read
 * A single-purpose function that declares what it is going to do and does nothing more
 * Scope-contained configuration (apihost) that eliminates the use of any sort of globals
 * Error checking/handling/logging for observability so that problems will not go unnoticed
 * Compiled regular expression that is reused for each event processed to reduce overhead

Had this been a real application, there would have been much more to this including dependency
injection, configuration management, indirect output through some log/result/event stream, setup and
teardown, unit test coverage, and packaging as a reusable module ready for an application to use the
ApiClient.

