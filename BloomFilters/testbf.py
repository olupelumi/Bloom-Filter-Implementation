import numpy as np
import random
import bf

np.random.seed(seed = 6)
S=np.random.randint(low=10000, high=99999, size=10000)
S = S.tolist()
#print(len(S))

#need to generate a list of 1000 numbers in and not in S

#first for the things in S
in_S = [random.choice(S) for i in range(1000)]

#now the ones not in S
not_in_S = []
count_len=0
for numb in range(10000,99999):
        if numb not in S:
                not_in_S.append(numb);
                count_len += 1
        if count_len == 1000:
                break

#Initializing my bloom filter class
bloom1 = bf.BloomFilter(10000, 0.01)
#print(len(bloom1.val))
 #adding the values from the membership set into the bloom filter
for member in S:
        bloom1.insert(member)
print(bloom1.val)  



