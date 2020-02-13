#do this hash fuction later 
import math
def h2Uni(x,m):
        """
        A 2-universal hash function of a positive integer
        x is the value to be hashed
        m is the hash table size

        """

        return (((60843 * x) + 470521)  % m)

def hashfunc(x,m):
        return h2Uni(x,m)


...
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
                fill = 4294967295                                 # all bits set
        else:
                fill = 0                                      # all bits cleared

        bitArray = array.array('I')          # 'I' = unsigned 32-bit integer

        bitArray.extend((fill,) * intSize)

        return(bitArray)
 # testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
def testBit(array_name, bit_num):
     record = bit_num >> 5
     offset = bit_num & 31
     mask = 1 << offset
     return(array_name[record] & mask)

def setBit(array_name, bit_num):
     record = bit_num >> 5
     offset = bit_num & 31
     mask = 1 << offset
     array_name[record] |= mask
     return(array_name[record])


class BloomFilter ():
        def __init__ ( self , n , fp_rate ):
                self.R = n*math.log(fp_rate - 0.618)
                self.val = makeBitArray(bitSize = self.R,fill = 0) 
        
        #hashing a value and adding it into the bloom filter
        def insert ( self , key ):
                #hashing the key first
                bit_pos = hashfunc(key,self.R)
                #setBit() returns an integer with the bit at 'bit_num' set to 1.
                return setBit(self.val,bit_pos)



        ...
        #method used to know whether a query is in the set or not
        def test ( self , key ):
                bit_pos = hashfunc(key,self.R)
                key_in_set = testBit(self.val, bit_pos)
                if bit_pos != 0:
                        return True
                return False
