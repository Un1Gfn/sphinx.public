#!/bin/env python3
# https://stackoverflow.com/questions/26666859/how-do-i-print-all-labels-that-are-defined-in-a-sphinx-project

import pickle

f=open('/tmp/un1gfn.github.io/.doctrees/environment.pickle', "rb")
# f=open('/tmp/un1gfn.github.io/.doctrees/chrome.doctree', "rb")
dat=pickle.load(f,errors="strict")
f.close()

labels=dat.domaindata['std']['labels'].keys()

# print(labels)
for lb in labels:
  print('###%s###'%(lb,))
