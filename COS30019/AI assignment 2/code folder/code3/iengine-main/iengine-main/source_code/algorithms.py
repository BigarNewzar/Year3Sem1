import copy
from collections import deque
from plast import HornClause, NegationExpression, ConjunctionExpression

def tt_entail(kb, query, symbols):
    def tt_check(kb, query, symbols, model, model_count):
        if not symbols:
            if kb.evaluate(model):
                model_count[0] += 1
                return query.evaluate(model)
            else:
                return True
        else:
            stack = list(symbols)  # Make a list-copy of the set symbols, this allows for backtracking
            # Get the last element
            p = stack.pop()

            tmp_model = model.copy()
            model[p] = True
            tmp_model[p] = False
            # rest = symbols

            return tt_check(kb, query, stack, model, model_count) and tt_check(kb, query, stack, tmp_model, model_count)

    # A list is used to exploit pass-by-reference of mutable objects
    model_count = [0]  # Keep track of count of model
    res = tt_check(kb, query, copy.deepcopy(symbols), {}, model_count)
    if res:
        print('YES: ' + str(model_count[0]))
    else:
        print('NO')


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


def bc_entail(kb, query, symbols):
    def bc(kb, query, inferred):
        if query in inferred:
            return True
        for clause in kb:
            if isinstance(clause, HornClause):
                if query == clause.tail():
                    count = len(clause.head())
                    for sym in clause.head():
                        if bc(kb, sym, inferred):
                            count -= 1
                            inferred.add(sym)
                    if count == 0:
                        return True
            else:
                if query == clause:
                    return True
                else:
                    inferred.add(clause)
        return False

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


def dpll_entail(kb, query, symbols):

    def find_pure_symbols(symbols, conjunct, model):
        for s in symbols:
            pos, neg = False, False
            for c in conjunct:
                if s in c:
                    pos = True
                if NegationExpression(s) in c:
                    neg = True
                if pos != neg:
                    return s, pos
        return None, None


    def find_unit_clause(conjunct, model):
        for c in conjunct:
            p, val = None, None
            count = 1
            for literal in c:
                p, val = literal.unit(model)
                if p:
                    count -= 1
                if count < 0: # More than one free variable
                    break
            if p is not None and count == 0:
                return p, val
        return None, None


    def cnfeval(disjunct, model):
        eval = {literal.cnfeval(model) for literal in disjunct}
        if True in eval:
            return True
        elif None in eval:
            return None
        else:
            return False


    def dpll_true(clauses, symbols, model):
        # Early exit
        eval = {cnfeval(c, model) for c in clauses}
        if False in eval:
            return False
        elif None not in eval:
            return True

        # Heuristics
        p, val = find_pure_symbols(symbols, clauses, model)
        if p:
            symbols.remove(p)
            model[p] = val
            return dpll_true(clauses, symbols, model)

        p, val = find_unit_clause(clauses, model)
        if p:
            symbols.remove(p)
            model[p] = val
            return dpll_true(clauses, symbols, model)

        p = symbols.pop()
        # rest = symbols
        tmp_model = model.copy()
        model[p] = True
        tmp_model[p] = False

        return dpll_true(clauses, symbols, model) or dpll_true(clauses, symbols, tmp_model)


    # Using deduction theorem: kb entails q if kb => q is valid, or kb & ~q is unsat
    cnfsat = (ConjunctionExpression(kb.reduce(), NegationExpression(query)).reduce()).flatten()
    res = dpll_true(cnfsat, copy.deepcopy(symbols), {})

    if not res:
        print('YES')
    else:
        print('NO')

    print('{', end="")
    for c in cnfsat:
        print('{', end="")
        for d in c:
            print(str(d), end=",")
        print('}', end="")
    print('}')

