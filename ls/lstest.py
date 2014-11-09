#!/usr/bin/python3
#Filename:lstest
import os
import sys
if len(sys.argv)!=1:
  if ('/' in sys.argv[-1])or('~' in sys.argv[-1]):
    a=os.listdir(sys.argv[-1])
    if ('-a' in sys.argv)or('-aR' in sys.argv)or('-al' in sys.argv):
        print('.\n..')
        for i in a:
          print(i)
    else:
        for i in a:
           if i[0]!='.':
            print(i)
  else:
    a=os.listdir(os.getcwd())
    if ('-a' in sys.argv)or('-aR' in sys.argv)or('-al' in sys.argv):
      print('.\n..')
      for i in a:
          print(i)
else:
  a=os.listdir(os.getcwd())
  for i in a:
    if i[0]!='.':
      print(i)
