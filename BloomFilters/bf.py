#do this hash fuction later 
import math
from sklearn.utils import murmurhash3_32

def hashfunc(m):
        #defining my hash function with the right m
        def myhash(x,seed):
                return (murmurhash3_32(x,seed=seed)) % m
        return myhash


import array
def makeBitArray(bitSize, fill = 0):
        '''
        initializing a bit array of size bitSize 
        filled in with all zeros
        '''
        intSize = bitSize >> 5     # number of 32 bit integers
        if (bitSize & 31): # if bitSize != (32 * n) add
                intSize += 1                        #    a record for stragglers
        if fill == 1:
                fill = 4294967295         # all bits set
        else:
                fill = 0                # all bits cleared

        bitArray = array.array('I')          # 'I' = unsigned 32-bit integer

        bitArray.extend((fill,) * intSize)

        return(bitArray)
 # testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
def testBit(array_name, bit_num):
     record = bit_num >> 5
     offset = bit_num & 31
     mask = 1 << offset
     return(array_name[record] & mask)
 #setBit() returns an integer with the bit at 'bit_num' set to 1.
def setBit(array_name, bit_num):
     record = bit_num >> 5
     offset = bit_num & 31
     mask = 1 << offset
     array_name[record] |= mask
     return(array_name[record])


class BloomFilter ():
        def __init__ ( self , n , fp_rate ):
                self.R = int(n*(math.log(fp_rate) // math.log(0.618)))
                self.val = makeBitArray(bitSize = self.R, fill = 0) 
                self.kval = int((self.R / n) * math.log(2))
                self.hfunc = hashfunc(self.R)

        def insert (self, key):
                #Retrieved the hash function
                for i in range(self.kval): #hashing the vlaue for each k value
                        bit_pos = self.hfunc(x = key, seed = i)
                        setBit(array_name = self.val, bit_num = bit_pos )

        # testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
        #method used to know whether a query is in the set or not
        def test (self, key):
                #OKAY so I have my k hash functions. If I check and one of them is 0, the query wasn't seen before 
                #If I check and all them are set to 1, then I've most likely seen the query
                flag = True
                for i in range(self.kval):
                        bit_pos = self.hfunc(x = key, seed = i)
                        is_in_bloom = testBit(array_name = self.val, bit_num = bit_pos)
                        if is_in_bloom == 0: #one of the hash functions had nver seen it
                                flag = False
                                break
                return flag

