#!/usr/bin/python
#
# yarpg.py - Yet Another Random Password Generator
#
# Usage: yarpg.py -L <length> -n <numofpasswords> -t [complex|alphanumberic|all]
#
# At an opinion, but I wouldn't add a "\n" to the end of the password
# variable - it should be the password and nothing else in the variable.

import random
import string
import sys
import getopt
import optparse


def main(argv):
  numpw = 3
  pwlen = 8
  r = random.SystemRandom() 
  usage_text = "usage: yarpg.py -L pwlength -n numberofpw. Default passwords: 3, Default Length: 8\n"

  try:
    opts, args = getopt.getopt(argv,"hL:n:",["pwlen=","numpw=", 'help'])
  except getopt.GetoptError:
    print usage_text
    sys.exit()

  for opt, arg in opts:
    if opt == '-h':
      print usage_text
      sys.exit(0)
    elif opt in ("-L", "--passwordlength"):
      pwlen = int(arg)
    elif opt in ("-n", "--number"):
      numpw = int(arg)
    #elif opt in ("-t", "--type"):
    #   pwtype = [alphanumeric|complex|all]


  for x in range(numpw):
    print "Complex Password #" + str(x+1) + ": " + "".join([r.choice(string.ascii_letters + string.digits + string.punctuation) for _ in xrange(pwlen)]) 
    print "Alphanumberic Password #" + str(x+1) + ": " + "".join([r.choice(string.ascii_letters + string.digits) for _ in xrange(pwlen)]) 
      
if __name__ == "__main__":
  main(sys.argv[1:])
