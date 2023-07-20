#import time
#import psutil


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

    #t0 = time.time_ns()
    
    # A list is used to exploit pass-by-reference of mutable objects
    model_count = [0]  # Keep track of count of model
    res = tt_check(kb, query, symbols, {}, model_count)
    

    if res:
        print('YES: ' + str(model_count[0]))
    else:
        print('NO')
        
    #Part of data collection for performance    
    #t1 = time.time_ns()
    #mem = psutil.virtual_memory().available    
    #print('Runtime: ' + str(t1 - t0))
    #print('Memory: ' + str(mem))