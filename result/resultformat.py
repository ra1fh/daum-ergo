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

"""
Daum Ergo Bike result record format definition
"""

from __future__ import absolute_import, print_function

from construct import *

result_file = GreedyRange(
    "result_record" / Struct(
        "elapsed_time"  / Int32ul,   # s
        "distance"      / Float32l,  # m
        "energy"        / Float32l,  # kJ
        "slope"         / Int16sl,   # 1/10 %
        "torque"        / Int16ul,   # 1/10 NM
        "rpm"           / Int16ul,   # 1/10 RPM
        "speed"         / Int16ul,   # 1/10 km/h
        "power"         / Int16ul,   # Watt
        "gear"          / Int8ul,
        "device_active" / Int8ul,    # 1
        "pulse"         / Int8ul,    # bpm
        "pulse_type"    / Int8ul,    # 7=invalid pulse, 0/4=valid pulse?
        "pulse_time_1"  / Int16ul,
        "pulse_time_2"  / Int16ul,
        "pulse_time_3"  / Int16ul,
        "pulse_time_4"  / Int16ul,
        "pulse_time_5"  / Int16ul,
        "pulse_time_6"  / Int16ul,
        "training_type" / Int16ul,
        "training_value"/ Float32l
))
