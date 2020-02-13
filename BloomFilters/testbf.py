import numpy as np
import random
import bf

S=np.random.randint(low=10000, high=99999, size=10000)
#S=set(S)
print(len(S))

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



