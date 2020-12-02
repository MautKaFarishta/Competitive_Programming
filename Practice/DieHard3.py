def Pour(toJugCap, fromJugCap, d):
    fromJug = fromJugCap
    toJug  = 0

    step = 1
    while ((fromJug  is not d) and (toJug is not d)):
 
        temp = min(fromJug, toJugCap-toJug)
 
        toJug = toJug + temp
        fromJug = fromJug - temp
 
        step =  step + 1
        if ((fromJug == d) or (toJug == d)):
            break
 
        if fromJug == 0:
            fromJug = fromJugCap
            step =  step + 1
 
        if toJug == toJugCap:
            toJug = 0
            step =  step + 1
             
    return step