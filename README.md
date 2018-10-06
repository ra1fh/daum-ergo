# Daum Ergo Bike Tools

Collection of things related to Daum Premium 8i indoor bike trainer.

## Toolchain

The toolchain subdirectory contains a Makefile to build a cross
compiler for the Samsung S3C2410 SoC used by the control cockpit of
the Daum Premium 8i indoor bike trainer. The source code is available
on the
[manufacturer's website](http://www.daum-electronic.de/de/download/GPL/).
The necessary files will be downloaded automatically during the build.

Building the arm cross compiler (gcc-3.3.2) needs a pretty old host
compiler. I've found the compat gcc 3.4 included in Fedora 28 to work
well for that purpose.

Install prerequisites on Fedora 28:

```
sudo dnf install compat-gcc-34 flex bison
```

The following step will build and install the cross compiler:

```
cd toolchain
make
```

The compiler will be installed into the `arm` directory in the
source tree by default. Change `DAUM_PREFIX` to install somewhere else.

## Control

The control directory contains a remote control client that
connects via TCP to port 51955 of the bike. This is work
in progress.

