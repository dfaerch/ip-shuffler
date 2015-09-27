# ip-shuffler
Randomizing of IP addresses from CIDR ranges for scanning tools like Nmap

## Description

This tool reads a text file, containing networks in CIDR notation (or pure IPs) and outputs a randomized list of all IPs, from all subnets, to either STDOUT or to one or more files.


## Usage
    $ ./ip-shuffler.py input_file  [ out_dir/ [ batch_size ] ]

where:

* input_file:  file containing a list (or mixture) of CIDR notations or ip-adresses (1 per line).
* out_dir   :  directory where to write all the output files. Will print to STDOUT if omitted.
* batch_size:  number if ips per output file. (default: 31000)


## Examples
### input_file example

    172.16.99.1/24
    10.0.0.10/20
    127.0.0.1
    10.0.0.12/24
    192.168.1.1/25


This example highlights 2 points:

1. Mixing if regular IPs with CIDR notation is perfectly valid.
2. There are 2 CIDR ranges that are actually overlapping on the list. These will
automagically be merged, thus removing duplicate IPs.

### Usage example

Make a file containing networks. Eg. use the above example listing and save as "example_ip_list"

Make a directory to hold the output files

    $ mkdir outdir

Now run ip-shuffler on the example list, writing files to "outdir" with 1000 ip's per file.

    $ ./ip-shuffler.py example_ip_list outdir 1000
    Reading example_ip_list
     - writing outdir/iplist-00000000.out
     - writing outdir/iplist-00000001.out
     - writing outdir/iplist-00000002.out
     - writing outdir/iplist-00000003.out
     - writing outdir/iplist-00000004.out

## Install notes

You must have the python "netaddr" library installed.

On Debian/Ubuntu:

    $ apt-get install python-netaddr


## Copyright and license

Code released under GPLv2 (see included LICENSE file). Copyright 2015 Dan Faerch - NullQ.com



