import pandas as pd
import numpy as np

nsum=0

def cal_sum(nsum):
   for i in range(10):
        nsum += i
   return nsum

print('nsum=', cal_sum(10))


