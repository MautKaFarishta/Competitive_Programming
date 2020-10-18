import math
import os
import random
import re
import sys

def maxCircle(queries):
    root_dict = {}
    length_dict = {}
    ret_list = []
    ret = 2
  
    def get_root(x):
        # if x is in a disjoint set, then return the root
        if x in root_dict:
            while x != root_dict[x]:
                x = root_dict[x]
        # if x is not in any disjoint sets, then initialize it
        else:
            length_dict[x] = 1
            root_dict[x] = x
        print("In GetRoot--->",root_dict,length_dict)
        return x

    for q in queries:
        r1, r2 = get_root(q[0]), get_root(q[1])
        # if q[0], q[1] are in different disjoint sets, then link the shorter one to longer one
        print(r1,r2)
        if r1 != r2:
            if length_dict[r1] > length_dict[r2]:
                r1, r2 = r2, r1
            root_dict[r1] = r2
            length_dict[r2] += length_dict[r1]
        ret = max(ret, length_dict[r2])
        ret_list.append(ret)
    return ret_list

if __name__ == '__main__':
    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)
    for i in ans:
       print(i)
