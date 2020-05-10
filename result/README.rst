
resultread
==========

Format specification and CSV converter for Daum Ergo Bike result
record files. The result files can be found on the SD-Card in
`data/result/ergo_bike`

Requirements
------------

* `python <https://www.python.org>`_ (version 2.7, 3.7, 38)

* `python-construct <https://pypi.python.org/pypi/construct>`_ (version 2.8)

* `docopt <https://pypi.python.org/pypi/docopt>`_ (version 0.6.2)


Usage
-----

resultread
''''''''''

Read and Print Daum Ergo Bike Result Files to CSV.

::

   Usage:
        resultread [-r] [-i FILE] [-o FILE] [-l LIMIT]

    Options:
        -h, --help               Show this.
            --version            Show version.
        -i, --input FILE         Input result file (default: stdin).
        -o, --output FILE        Output text file (default: stdout).
        -r, --raw                Output raw data in verbose format
        -l, --limit LIMIT        Limit of data points to print.

Example usage that reads a result file and prints the CVS header and
maximum 5 data points:

::

    resultread --input  0000000000000001 --limit 5
