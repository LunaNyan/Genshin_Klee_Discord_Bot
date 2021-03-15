#!/usr/bin/python3
import sys, fcntl

pid_file = 'kleebot.lock'
fp = open(pid_file, 'w')

try:
    fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print("FATAL   : Another bot isntance is running!")
    print("          Terminate another bot and try again.")
    sys.exit(1)

sys.path.append('./modules/')
import main
