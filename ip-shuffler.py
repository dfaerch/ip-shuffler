#!/usr/bin/python
from netaddr import *
import random, sys, os

def usage(err):
  print "ERROR: %s\nUsage:\n $ %s input_file  out_dir/ [ batch_size ]" % (err,sys.argv[0]);
  print "where:"
  print "  input_file:  file containing a list (or mixture) of CIDR notations or ip-adresses (1 per line)"
  print "  out_dir   :  directory where to write all the output files"
  print "  batch_size:  number if ips per output file"
  exit(1)


if (len(sys.argv)<3):
  usage("Not enough arguments")

# Default batch size. Can be overriden on cmdline
batch_size = 31234;

# out-file counter
step = 0;

ip_list_file = sys.argv[1]
out_dir      = sys.argv[2]

if (len(sys.argv)>3):
  batch_size = int(sys.argv[3])

if not os.path.isfile(ip_list_file):
  usage(ip_list_file+" is not a file")

if not os.path.isdir(out_dir):
  usage(out_dir+" is not a dir")

try:
  f = open(ip_list_file, 'r')
except IOError:
  print "File open failed!"
  exit();    
    
ip_list = []

print "Reading %s" % (ip_list_file);

for line in f:
  if "/" in line:
    ip_list.extend(list(IPNetwork(line)))
  else:
    ip_list.append(IPAddress(line))

random.shuffle(ip_list)
ip_list_max = len(ip_list)

done=0

# iterate until there are no more IPs
while not done:

  filename = "%s/iplist-%08d.out" % (out_dir,step);
  print " - writing %s" % (filename);
  o = open(filename,'w')

  for x in range( step*batch_size, ((step+1) * batch_size) ):
    if (x>ip_list_max-1):
      done=1
      continue

    o.write(str(ip_list[x])+"\n")

  o.close()
  step=step+1
    

