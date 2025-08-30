import os
from numpy.core.shape_base import block
import pandas as pd
import numpy as np
 

#inputs
#list of proccess

def bestfit(processes,blocksize):
    not_allocated = []
    for i in range(len(processes)):
        allocation=-1
        smallest=max(blocksize)
        for j in range(len(blocksize)):
            if blocksize[j]-processes[i]>-1:
                allocation=0
                if blocksize[j]-processes[i] < smallest :
                    smallest= blocksize[j]-processes[i]
                    smallest_index=j
        if allocation==-1:
            not_allocated.append(processes[i])
        else:
            blocksize.insert(smallest_index+1,smallest) 
            blocksize[smallest_index] = processes[i]
    print(not_allocated)
    print(blocksize)


print("enter all list of free blocks size pne by one" )
blocksize=list(map(int,input().split()))
print()
print("all processes(size) and files(size) by spaces")
processes=list(map(int,input().split()))
print()
bestfit(processes,blocksize)





