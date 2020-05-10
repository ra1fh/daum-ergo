#!/usr/bin/env python
#
# Copyright (c) 2020 Ralf Horstmann <ralf@ackstorm.de>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

'''Read and Print Daum Ergo Bike Result Files to CSV.

Usage:
    resultread [-r] [-i FILE] [-o FILE] [-l LIMIT]

Options:
    -h, --help               Show this.
        --version            Show version.
    -i, --input FILE         Input result file (default: stdin).
    -o, --output FILE        Output text file (default: stdout).
    -r, --raw                Output raw data in verbose format
    -l, --limit LIMIT        Limit of data points to print.

'''

from __future__ import absolute_import, print_function

import docopt
import io
import math
import os
import string
import sys

from resultformat import result_file

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def resultprint(document, limit=None):
    output = StringIO()
    doc = result_file.parse(document)
    output.write("\n")
    output.write("\n".join(map(str, doc[:limit])))
    output.write("\n")
    return output.getvalue()

def round_decimals(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n*factor + 0.5) / factor

def resultcsv(document, limit=None):
    output = StringIO()
    doc = result_file.parse(document)
    output.write("Elapsed Time (s);Distance (km);Phys. kJoule;Slope (%);NM;RPM;Speed (km/h);Watt;Gear;Device Active;Pulse;Pulse Type;Training Type;Training Value;Pulse Time 1;2;3;4;5;6\n")
    for record in doc[:limit]:
        output.write('{0};'.format(record.elapsed_time))
        output.write('{0:.3f};'.format(round_decimals(record.distance / 1000, 3)))
        output.write('{0:.1f};'.format(round_decimals(record.energy,1)))
        output.write('{0:.1f};'.format(round_decimals(record.slope * 0.1, 1)))
        output.write('{0:.1f};'.format(round_decimals(record.torque * 0.1, 1)))
        output.write('{0:.1f};'.format(round_decimals(record.rpm * 0.1, 1)))
        output.write('{0:.1f};'.format(round_decimals(record.speed * 0.1, 1)))
        output.write('{0};'.format(record.power))
        output.write('{0};'.format(record.gear))
        output.write('{0};'.format(record.device_active))
        output.write('{0};'.format(record.pulse))
        output.write('{0};'.format(record.pulse_type))
        output.write('{0};'.format(record.training_type))
        output.write('{0:.1f};'.format(round_decimals(record.training_value,1)))
        output.write('{0};'.format(record.pulse_time_1))
        output.write('{0};'.format(record.pulse_time_2))
        output.write('{0};'.format(record.pulse_time_3))
        output.write('{0};'.format(record.pulse_time_4))
        output.write('{0};'.format(record.pulse_time_5))
        output.write('{0}'.format(record.pulse_time_6))
        output.write("\n")
    return output.getvalue()

def main(argv=None):
    if (sys.version_info < (3,0)):
        reload(sys)
        sys.setdefaultencoding('utf-8')

    if (argv == None):
        argv = sys.argv[1:]

    try:
        args = docopt.docopt(__doc__, argv=argv, version='resultread ' + '1.0')

        limit = None
        if args['--limit']:
            limit = int(args['--limit'])

        if args['--input']:
            with io.open(args['--input'], 'rb') as f:
                if args['--raw']:
                    text = resultprint(f.read(), limit)
                else:
                    text = resultcsv(f.read(), limit)
        else:
            with sys.stdin as f:
                if args['--raw']:
                    text = resultprint(f.read(), limit)
                else:
                    text = resultcsv(f.read(), limit)

        if args['--output']:
            with io.open(args['--output'], 'wb') as outfile:
                outfile.write(text.encode('utf-8'))
        else:
            sys.stdout.write(text)

        return 0

    except KeyboardInterrupt:
        print(" Interrupted.", file=sys.stderr)

    except IOError as error:
        print("error: IOError {0}".format(error, file=sys.stderr))

    return 1

if __name__ == "__main__":
    sys.exit(main())
