# Daum Ergo Bike Tools

Collection of things related to Daum Premium 8i indoor bike trainer.

## Toolchain

The toolchain subdirectory contains a Makefile to build a cross
compiler for the Samsung S3C2410 SoC used by the control cockpit of
the Daum Premium 8i indoor bike trainer.

## Control

The control directory contains a remote control client that
connects via TCP to port 51955 of the bike. This is work
in progress.

## Result

The result directory contains a converter and format specification for
Daum Ergo Bike result records that are stored on the SD-Card.  The
tool converts to CSV similar to emc2edit.
