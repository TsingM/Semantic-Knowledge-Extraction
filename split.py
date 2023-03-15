# -*- coding:utf-8 -*-
#Dataset splitting
import random
from random import randint
import numpy as np
 
oldf = open('with_hash/SkillKG_V1_with_hash.txt', 'r',encoding='utf-8')
validf = open('valid.txt', 'w',encoding='utf-8')   #valid
testf = open('test.txt', 'w',encoding='utf-8')   #test
n = 0
resultList = random.sample(range(0, 10768), 2000)
lines = oldf.readlines()
for i in resultList:
    validf.write(lines[i])
    np.delete(lines, i)
oldf.close()