def IsPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def FindPrimesForChunk(nMin,nMax):
    primes = set()
    for i in range(nMin,nMax):
        if IsPrime(i):
            primes.add(i)
    return primes

def FindPrimesForChunkList(chunkPair):
    if len(chunkPair) < 2:
        return set()
    return FindPrimesForChunk(chunkPair[0],chunkPair[1])