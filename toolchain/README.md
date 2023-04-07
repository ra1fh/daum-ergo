# Daum Ergo Bike Cross Toolchain

The toolchain subdirectory contains a Makefile to build a cross
compiler for the Samsung S3C2410 SoC used by the control cockpit of
the Daum Premium 8i indoor bike trainer. The source code is available
on the
[manufacturer's website](http://www.ergo-lyps.de/de/download/GPL/).

## Prerequisites

These instructions assume building on an x86_64 host using some recent
version of Debian or Ubuntu. The actual build will be done in a
chroot.

A few packages need to be installed on the build host:

```
sudo apt-get install chrootuid debootstrap git libc6-i386 make wget
```

## Building

Building the arm cross compiler (gcc-3.3.2) needs a similarly old host
compiler. The easiest way to get that is creating a Debian Sarge chroot:

```
sudo debootstrap --arch=i386 sarge ~/sarge-chroot http://archive.debian.org/debian
sudo chroot ~/sarge-chroot apt-get -y install bison bzip2 file flex gcc libc6-dev make patch perl-modules
```

Prepare the build directory within the chroot, checkout the repository
and download additional source code:

```
sudo install -d -o $(id -u) -g $(id -g) ~/sarge-chroot/daum-ergo
git clone https://github.com/ra1fh/daum-ergo ~/sarge-chroot/daum-ergo
make -C ~/sarge-chroot/daum-ergo/toolchain download
```

Now enter the chroot and build the cross compiler:

```
sudo chrootuid -i ~/sarge-chroot $(id -un) /usr/bin/make -C daum-ergo/toolchain
```

The compiler will be installed in
`~/sarge-chroot/daum-ergo/toolchain/arm`. It will work outside the
chroot. You can check with:

```
~/sarge-chroot/daum-ergo/toolchain/arm/gcc-3.3.2-glibc-2.3.2/arm-9tdmi-linux-gnu/bin/gcc -dumpmachine
# expected result: arm-9tdmi-linux-gnu
```

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
