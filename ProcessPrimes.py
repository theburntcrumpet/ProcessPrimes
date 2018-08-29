from multiprocessing import Pool
from multiprocessing import cpu_count
import logging,datetime
from Primes import *

"""
    A Quick and Dirty Demonstration of Concurrancy in python using a pool of processes from multiprocessing
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s')
MIN_SEARCH = 1
MAX_SEARCH = 250000
CHUNK_SIZE = 100
PROCESSES  = cpu_count()

def GenerateChunks(nMin,nMax,nChunkSize):
    chunks = []
    nCurrentMin = nMin
    nCurrentMax = nMin + nChunkSize
    while nCurrentMax < nMax:
        chunks.append([nCurrentMin,nCurrentMax])
        nCurrentMin = nCurrentMax
        nCurrentMax = nCurrentMin + nChunkSize
    chunks.append([nCurrentMin,nMax])
    return chunks

if __name__ == "__main__":
    primes = set()
    logging.info("Generating Chunks Specified by Application Constants")
    chunks = GenerateChunks(MIN_SEARCH,MAX_SEARCH,CHUNK_SIZE)
    logging.info("Creating Pool of {} Processes".format(PROCESSES))
    tBegin = datetime.datetime.now()
    with Pool(PROCESSES) as p:
        for i in p.map(FindPrimesForChunkList,chunks):
            primes.update(i)
    logging.info("Finished processing, sorting primes")
    primes = sorted(primes)
    for i in primes:
        logging.info("\t{}".format(i))
    logging.info("Finished in {}, found {} primes between {} and {}".format(datetime.datetime.now() - tBegin,len(primes),MIN_SEARCH,MAX_SEARCH))
