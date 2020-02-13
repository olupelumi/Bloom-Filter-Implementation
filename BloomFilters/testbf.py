import numpy as np
import random
import bf

np.random.seed(seed = 123)
S=np.random.randint(low=10000, high=99999, size=10000)
S = S.tolist()
#print(len(S))

#need to generate a list of 1000 numbers in and not in S
random.seed( 31 )
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


for fp_rate in [0.01, 0.001, 0.0001]:
        #Initializing my bloom filter class
        bloom1 = bf.BloomFilter(10000, fp_rate)
        #print(len(bloom1.val))
        print(bloom1.R)
        #adding the values from the membership set into the bloom filter
        for member in S:
                bloom1.insert(member)

        #looking up all the items in the test and computing the false positive rate.
        fp_count = 0
        for memb in not_in_S:
                in_bloom = bloom1.test(memb)
                if (in_bloom):
                        fp_count += 1
        print("fp_count" +"(" + str(fp_rate) + "): "+ str(fp_count))
        print("fp_rate: "  +"(" + str(fp_rate) + "): "+ str(fp_count/1000.0))





