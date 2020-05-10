
resultread
==========

Format specification and CSV converter for Daum Ergo Bike result
record files. The result files can be found on the SD-Card in
`data/result/ergo_bike`

Requirements
------------

* `python <https://www.python.org>`_ (version 2.7, 3.7, 3.8)

* `python-construct <https://pypi.python.org/pypi/construct>`_ (version 2.8)

* `docopt <https://pypi.python.org/pypi/docopt>`_ (version 0.6.2)


Usage
-----

resultread
''''''''''

Read Daum Ergo Bike result files and output as CSV.

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

Example usage that reads a result file and prints the CSV header and
maximum 5 data points:

::

    resultread --input  0000000000000001 --limit 5

The CSV output looks like this:

::

    Elapsed Time (s);Distance (km);Phys. kJoule;Slope (%);NM;RPM;Speed (km/h);Watt;Gear;Device Active;Pulse;Pulse Type;Training Type;Training Value;Pulse Time 1;2;3;4;5;6
    1;0.000;0.0;0.0;0.0;0.0;0.0;20;10;1;0;7;16;105.0;0;0;0;0;0;0
    2;0.000;0.0;0.0;95.5;2.0;0.5;20;10;1;0;7;16;105.0;0;0;0;0;0;0
    3;0.000;0.1;0.0;127.3;1.5;0.5;20;10;1;0;7;16;105.0;0;0;0;0;0;0
    4;0.000;0.1;0.0;114.6;1.7;0.4;20;10;1;0;7;16;105.0;0;0;0;0;0;0
    5;0.000;0.1;0.0;47.7;4.0;0.4;20;10;1;0;7;16;105.0;0;0;0;0;0;0

