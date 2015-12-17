#!/usr/bin/python
#
# yarpg.py - Yet Another Random Password Generator
#
# Usage: yarpg.py -L <length> -n <numofpasswords> -t [complex|alphanumeric]
#

import getopt
import random
import string
import sys

DEFAULT_PWLEN=8
DEFAULT_NUMPW=3

def main(argv):
  numpw = DEFAULT_NUMPW
  pwlen = DEFAULT_PWLEN
  pwtype = "both"
  r = random.SystemRandom() 
  typeflag = 3 # This is related to the pwtype.
  usage_text = "usage: yarpg.py -L pwlength -n numberofpw -t type.\n\nDefault passwords: 3\nDefault Length: 8\nDefault Type: both alphanumeric and complex\n"

  try:
    opts, args = getopt.getopt(argv,"hL:n:t:",["pwlen=", "numpw=", "pwtype", "help"])  
  except getopt.GetoptError:
    sys.exit(usage_text)

  for opt, arg in opts:
    if opt == '-h':
      print usage_text
      sys.exit(0)
    elif opt in ("-L", "--passwordlength"):
      pwlen = int(arg)
    elif opt in ("-n", "--number"):
      numpw = int(arg)
      if numpw < 1:
        sys.exit("Oops. You need at least one password to generate.")
    elif opt in ("-t", "--type"):
       pwtype = str(arg)
       if pwtype in "alphanumeric":
         typeflag = 1
       elif pwtype in "complex":
         typeflag = 2

  for x in range(numpw):
    if (typeflag == 1):
      print "Alphanumeric Password #" + str(x+1) + ": " + "".join([r.choice(string.ascii_letters + string.digits) for _ in xrange(pwlen)]) 
    elif (typeflag == 2):
      print "Complex Password #" + str(x+1) + ": " + "".join([r.choice(string.ascii_letters + string.digits + string.punctuation) for _ in xrange(pwlen)]) 
    elif (typeflag == 3):
      print "Alphanumeric Password #" + str(x+1) + ": " + "".join([r.choice(string.ascii_letters + string.digits) for _ in xrange(pwlen)]) 
      print "Complex Password #" + str(x+1) + ": " + "".join([r.choice(string.ascii_letters + string.digits + string.punctuation) for _ in xrange(pwlen)]) 

if __name__ == "__main__":
  main(sys.argv[1:])
