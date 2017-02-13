.PHONY: build clean default download

DAUM_GCC     = gcc34

DAUM_PREFIX := $(CURDIR)/arm
DAUM_SOURCE := $(CURDIR)/source
DAUM_BUILD  := $(CURDIR)/build
DAUM_PATCHES:= $(CURDIR)/patches

default: build

download:
	if ! [ -e $(DAUM_SOURCE) ]; then \
		mkdir $(DAUM_SOURCE); \
		cd $(DAUM_SOURCE) && \
		wget -c http://www.daum-electronic.de/de/download/GPL/GPL/kernel/linux-2.4.21.tar.bz2 && \
		wget -c http://www.daum-electronic.de/de/download/GPL/GPL/kernel/patch-2.4.21-rmk1.bz2 && \
		wget -c http://www.daum-electronic.de/de/download/GPL/GPL/kernel/patch-2.4.21-rmk1-gmc_daum.bz2 && \
		wget -c http://www.daum-electronic.de/de/download/GPL/GPL/kernel/config && \
        wget -c http://www.daum-electronic.de/de/download/GPL/GPL/crosstool/crosstool-0.26.tar.gz && \
		wget -c http://www.daum-electronic.de/de/download/GPL/GPL/crosstool/gmc-crosstool-0.26.patch && \
		wget -c http://www.kegel.com/crosstool/ptxdist-testing-20031113.tar.gz && \
		wget -c https://ftp.gnu.org/gnu/make/make-3.81.tar.gz && \
		wget -c https://ftp.gnu.org/gnu/gcc/gcc-3.3.2.tar.gz && \
		wget -c https://ftp.gnu.org/gnu/glibc/glibc-2.3.2.tar.bz2 && \
		wget -c https://ftp.gnu.org/gnu/glibc/glibc-linuxthreads-2.3.2.tar.bz2 && \
		wget -c https://www.kernel.org/pub/linux/devel/binutils/binutils-2.14.90.0.5.tar.gz && \
		true; \
	fi
	cd $(DAUM_SOURCE) && sha256sum -c ../sha256sum.txt

build: download
	mkdir -p $(DAUM_BUILD)
	mkdir -p $(DAUM_PREFIX)
    # build make
	if ! [ -f $(DAUM_PREFIX)/bin/gmake ]; then \
		cd $(DAUM_BUILD) && \
			tar xvzf $(DAUM_SOURCE)/make-3.81.tar.gz && \
			cd make-3.81 && \
				./configure --prefix=$(DAUM_PREFIX) && \
				make && \
				make install && \
				ln -s make $(DAUM_PREFIX)/bin/gmake; \
	fi
    # prepare kernel source
	if ! [ -f $(DAUM_SOURCE)/gmc-2.4.21.tar.bz2 ]; then \
		cd $(DAUM_SOURCE) && \
			echo "extracting linux-2.4.21.tar.bz2" && \
			tar xjf linux-2.4.21.tar.bz2 && \
			cd linux-2.4.21 && \
				echo "patching linux-2.4.21" && \
				bzcat $(DAUM_SOURCE)/patch-2.4.21-rmk1.bz2 | patch -s -p1 && \
				bzcat $(DAUM_SOURCE)/patch-2.4.21-rmk1-gmc_daum.bz2 | patch -s -p1 && \
				patch -s -p1 -i $(DAUM_PATCHES)/linux-2.4.21-bash-compatibility.patch && \
				cp $(DAUM_SOURCE)/config .config && \
		cd $(DAUM_SOURCE) && \
			mv linux-2.4.21 gmc-2.4.21 && \
			echo "creating gmc-2.4.21.tar.bz2" && \
			tar cjf gmc-2.4.21.tar.bz2 gmc-2.4.21 && \
			rm -rf gmc-2.4.21; \
	fi
	cd $(DAUM_BUILD) && \
		tar xvzf $(DAUM_SOURCE)/crosstool-0.26.tar.gz && \
		cd crosstool-0.26 && \
			patch -b -z .gmc -s -i $(DAUM_SOURCE)/gmc-crosstool-0.26.patch -p1 && \
			patch -b -z .fedora -s -i $(DAUM_PATCHES)/crosstool-0.26-fedora-25.patch -p1 && \
			export DAUM_SOURCE=$(DAUM_SOURCE) && \
			export DAUM_PREFIX=$(DAUM_PREFIX) && \
			export DAUM_GCC=$(DAUM_GCC) && \
			export PATH=$(DAUM_PREFIX)/bin:$$PATH && \
			sh ./demo.sh

clean:
	rm -rf $(DAUM_BUILD)
