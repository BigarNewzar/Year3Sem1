from collections import deque
from HornClause import HornClause
#import time
#import psutil


def fc_entail(kb, query, symbols):
    def fc(kb, query, count, agenda, inferred):
        while agenda:
            p = agenda.popleft()
            if p == query:
                return True
            if not inferred[p]:
                inferred[p] = True
                for clause in kb:
                    if p in clause.head():
                        count[clause] -= 1
                        if count[clause] == 0:
                            agenda.append(clause.tail())

    #t0 = time.time_ns()
    count = {}
    inferred = {}
    agenda = deque([])
    horn = set()

    for clause in kb:
        if isinstance(clause, HornClause):
            horn.add(clause)
            count[clause] = len(clause.head())
            for prem in clause.head():
                inferred[prem] = False
            inferred[clause.tail()] = False
        else:
            inferred[clause] = False
            agenda.append(clause)

    res = fc(horn, query, count, agenda, inferred)
     


    if res:
        out = 'YES: '
        for sym in inferred.keys():
            if inferred[sym]:
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
