.PHONY: build clean default download gdb

DAUM_PREFIX := $(CURDIR)/arm
DAUM_SOURCE := $(CURDIR)/source
DAUM_BUILD  := $(CURDIR)/build
DAUM_PATCHES:= $(CURDIR)/patches
DAUM_CROSS  := $(CURDIR)/arm/gcc-3.3.2-glibc-2.3.2/arm-9tdmi-linux-gnu/bin
DAUM_URL    := https://web.archive.org/web/20160123151000/http://www.daum-electronic.de/de/download/GPL
PTXDIST_URL := https://web.archive.org/web/20230407132744/http://www.kegel.com/

# As of April 2023, Daum files are still available from the following
# URL: http://www.ergo-lyps.de/de/download/GPL

GDB_VERSION:= 6.3a
GDB_DIR    := 6.3

default: build

download: $(DAUM_SOURCE)/download.stamp
$(DAUM_SOURCE)/download.stamp:
	if [ -e /etc/debian_version -a "$$(cat /etc/debian_version)" = "3.1" ]; then \
		echo ; \
		echo "ERROR: download needs to run outside chroot"; \
		echo ; \
		exit 1; \
	fi
	if ! [ -e $(DAUM_SOURCE) ]; then \
		mkdir $(DAUM_SOURCE); \
		cd $(DAUM_SOURCE) && \
		wget -c $(DAUM_URL)/GPL/kernel/linux-2.4.21.tar.bz2 && \
		wget -c $(DAUM_URL)/GPL/kernel/patch-2.4.21-rmk1.bz2 && \
		wget -c $(DAUM_URL)/GPL/kernel/patch-2.4.21-rmk1-gmc_daum.bz2 && \
		wget -c $(DAUM_URL)/GPL/kernel/config && \
		wget -c $(DAUM_URL)/GPL/crosstool/crosstool-0.26.tar.gz && \
		wget -c $(DAUM_URL)/GPL/crosstool/gmc-crosstool-0.26.patch && \
		wget -c $(PTXDIST_URL)/crosstool/ptxdist-testing-20031113.tar.gz && \
		wget -c https://ftp.gnu.org/gnu/gdb/gdb-$(GDB_VERSION).tar.gz && \
		wget -c https://ftp.gnu.org/gnu/gcc/gcc-3.3.2.tar.gz && \
		wget -c https://ftp.gnu.org/gnu/glibc/glibc-2.3.2.tar.bz2 && \
		wget -c https://ftp.gnu.org/gnu/glibc/glibc-linuxthreads-2.3.2.tar.bz2 && \
		wget -c https://www.kernel.org/pub/linux/devel/binutils/binutils-2.14.90.0.5.tar.gz && \
		true; \
	fi
	cd $(DAUM_SOURCE) && sha256sum -c ../sha256sum.txt
	touch $(DAUM_SOURCE)/download.stamp

build: $(DAUM_SOURCE)/download.stamp
	mkdir -p $(DAUM_BUILD)
	mkdir -p $(DAUM_PREFIX)
        # prepare kernel source
	if ! [ -f $(DAUM_SOURCE)/gmc-2.4.21.tar.bz2 ]; then \
		cd $(DAUM_SOURCE) && \
			echo "extracting linux-2.4.21.tar.bz2" && \
			tar xjf linux-2.4.21.tar.bz2 && \
			cd linux-2.4.21 && \
				echo "patching linux-2.4.21" && \
				bzcat $(DAUM_SOURCE)/patch-2.4.21-rmk1.bz2 | patch -s -p1 && \
				bzcat $(DAUM_SOURCE)/patch-2.4.21-rmk1-gmc_daum.bz2 | patch -s -p1 && \
				cp $(DAUM_SOURCE)/config .config && \
		cd $(DAUM_SOURCE) && \
			mv linux-2.4.21 gmc-2.4.21 && \
			echo "creating gmc-2.4.21.tar.bz2" && \
			tar cjf gmc-2.4.21.tar.bz2 gmc-2.4.21 && \
			rm -rf gmc-2.4.21; \
	fi
	cd $(DAUM_BUILD) && \
		tar xvf $(DAUM_SOURCE)/crosstool-0.26.tar.gz && \
		cd crosstool-0.26 && \
			patch -b -z .gmc -s -i $(DAUM_SOURCE)/gmc-crosstool-0.26.patch -p1 && \
			patch -b -z .sarge -s -i $(DAUM_PATCHES)/crosstool-0.26-debian-sarge.patch -p1 && \
			export DAUM_SOURCE=$(DAUM_SOURCE) && \
			export DAUM_PREFIX=$(DAUM_PREFIX) && \
			sh ./demo.sh

gdb: $(DAUM_PREFIX)/bin/arm-9tdmi-linux-gnu-gdb $(DAUM_PREFIX)/bin/gdbserver
	if ! [ -e $(DAUM_CROSS)/gcc ]; then \
		echo ; \
		echo "ERROR: toolchain needs to be build first. Please run make in toolchain."; \
		echo ; \
		exit 1;\
	fi
	mkdir -p $(DAUM_PREFIX)
	mkdir -p $(DAUM_BUILD)
	if ! [ -f $(DAUM_PREFIX)/bin/arm-9tdmi-linux-gnu-gdb ]; then \
		cd $(DAUM_BUILD) && \
			if ! [ -d $(DAUM_SOURCE)/gdb-$(GDB_DIR) ]; then \
				tar xvzf $(DAUM_SOURCE)/gdb-$(GDB_VERSION).tar.gz; \
			fi && \
			cd gdb-$(GDB_DIR) && \
				if [ -f  $(DAUM_PATCHES)/gdb-$(GDB_DIR).patch ]; then \
					patch -p1 -i $(DAUM_PATCHES)/gdb-$(GDB_DIR).patch; \
				fi && \
		cd $(DAUM_BUILD) && \
			mkdir -p gdb-build && \
			cd gdb-build && \
				$(DAUM_BUILD)/gdb-$(GDB_DIR)/configure \
					--prefix=$(DAUM_PREFIX) \
					--disable-nls \
					--target=arm-9tdmi-linux-gnu && \
				make && \
				make install; \
	fi
	if ! [ -f $(DAUM_PREFIX)/bin/arm-9tdmi-linux-gnu-gdbserver ]; then \
		cd $(DAUM_BUILD) && \
			if ! [ -d $(DAUM_SOURCE)/gdb-$(GDB_DIR) ]; then \
				tar xzf $(DAUM_SOURCE)/gdb-$(GDB_VERSION).tar.gz; \
			fi && \
			mkdir -p gdbserver-build && \
			cd gdbserver-build && \
				PATH=$(DAUM_CROSS):$$PATH \
				$(DAUM_BUILD)/gdb-$(GDB_DIR)/gdb/gdbserver/configure \
					--prefix=$(DAUM_PREFIX) \
					--host=arm-9tdmi-linux-gnu && \
				PATH=$(DAUM_CROSS):$$PATH \
				make && \
				PATH=$(DAUM_CROSS):$$PATH \
				make install; \
	fi

clean:
	rm -rf $(DAUM_BUILD) $(DAUM_PREFIX)
