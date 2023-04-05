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
compiler. The easiest way to get a suitable host compiler is to create
a Debian Sarge chroot, which came with gcc-3.3:

```
sudo debootstrap --arch=i386 sarge sarge-chroot
```

A couple of prerequisites need to be installed within the chroot using
dselect or similar:

* bison
* flex
* gcc
* make

Outside the chroot, run the download target:

```
cd toolchain
make download
```

Inside the Debian Sarge chroot, build and install the cross compiler:

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

