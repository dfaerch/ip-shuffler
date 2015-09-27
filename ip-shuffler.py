#!/usr/bin/python
from netaddr import *
import random, sys, os
import pprint;

def usage(err):
  print "ERROR: %s\nUsage:\n $ %s input_file  out_dir/ [ batch_size ]" % (err,sys.argv[0]);
  print "where:"
  print "  input_file:  file containing a list (or mixture) of CIDR notations or ip-adresses (1 per line)"
  print "  out_dir   :  directory where to write all the output files"
  print "  batch_size:  number if ips per output file"
  exit(1)

stdout = 0;
if (len(sys.argv)<2):
  usage("Not enough arguments")

if (len(sys.argv)>2):
  out_dir = sys.argv[2]
else:
  stdout  = 1;

ip_list_file = sys.argv[1]

# Default batch size. Can be overriden on cmdline
batch_size = 31000;

# out-file counter
step = 0;



if (len(sys.argv)>3):
  batch_size = int(sys.argv[3])

if not os.path.isfile(ip_list_file):
  usage(ip_list_file+" is not a file")

if not stdout and not os.path.isdir(out_dir):
    usage(out_dir+" is not a dir")

try:
  f = open(ip_list_file, 'r')
except IOError:
  print "File open failed!"
  exit();

cidr_list = []

print "Reading %s" % (ip_list_file);

for line in f:
  if "/" not in line:
    line.append("/32")
  cidr_list.append(IPNetwork(line))

# Expand networks into individual IPs
ip_list = []
# cidr_merge to remove overlapping subnets.
for line in cidr_merge(cidr_list):
  ip_list.extend(list(IPNetwork(line)))

random.shuffle(ip_list)
ip_list_max = len(ip_list)

done=0

# iterate until there are no more IPs
while not done:

  if not stdout:
    filename = "%s/iplist-%08d.out" % (out_dir,step)
    print " - writing %s" % (filename)
    o = open(filename,'w')

  for x in range( step*batch_size, ((step+1) * batch_size) ):
    #Are we done?
    if (x>ip_list_max-1):
      done=1
      continue

    if stdout:
      print str(ip_list[x]);
    else:
      o.write(str(ip_list[x])+"\n")

  if not stdout:
    o.close()

  step=step+1


