# Daum Ergo Bike Cross Toolchain

The toolchain subdirectory contains a Makefile to build a cross
compiler for the Samsung S3C2410 SoC used by the control cockpit of
the Daum Premium 8i indoor bike trainer. The source code is available
on the
[manufacturer's website](http://www.daum-electronic.de/de/download/GPL/).
The necessary files will be downloaded automatically during the build and
checked against known good SHA256 sums.

## Prerequisites

Building the arm cross compiler (gcc-3.3.2) needs a pretty old host
compiler. I've found the compat gcc 3.4 included in Fedora 28 to work
well for that purpose.

Install prerequisites on Fedora 28:

```
sudo dnf install compat-gcc-34 flex bison
```

## Building

The following step will build and install the cross compiler:

```
cd toolchain
make
```

The compiler will be installed into the `arm` directory in the
source tree by default. Change `DAUM_PREFIX` to install somewhere else.

## Usage

With a working compiler toolchain it's easy to build additional
utilities. To avoid modifying the Daum base operating system, I'd
suggest to build with a prefix like `/card/tools` so that the
resulting utilies can be run from the SD-Card. Here is an example to
cross-compile strace-4.8.5:

    export PATH=/path/to/arm/toolchain:$PATH
	cd strace-4.8.5
	./configure --host=arm-9tdmi-linux-gnu --prefix=/card/tools
	make
	DESTDIR=/path/to/sdcard/staging/dir make install
