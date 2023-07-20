from collections import deque
from HornClause import HornClause
#import time
#import psutil


def bc_entail(kb, query, symbols):
    def bc(kb, query, inferred):
        if query in inferred:
            return True
        for clause in kb:
            if isinstance(clause, HornClause):
                if query == clause.tail():
                    for sym in clause.head():
                        if not bc(kb, sym, inferred):
                            return False
                        else:
                            inferred.add(sym)
                    return True
            else:
                if query == clause:
                    return True
                else:
                    inferred.add(clause)
        return False

    #t0 = time.time_ns()
    inferred = set()
    res = bc(kb, query, inferred)
    

    if res:
        out = 'YES: '
        for sym in inferred:
            out += str(sym)
            out += ', '
        out += str(query)
        print(out)
    else:
        print('NO')
        
    #Part of data collection for performance
    #t1 = time.time_ns()
    #mem = psutil.virtual_memory().available
    #print('Runtime: ' + str(t1 - t0))
    #print('Memory: ' + str(mem))
