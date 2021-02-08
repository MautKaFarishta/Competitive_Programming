def Pour(toJugCap, fromJugCap, d):
    fromJug = fromJugCap
    toJug  = a =0

    while a<10:
 
        temp = min(fromJug, toJugCap-toJug)
 
        toJug = toJug + temp
        fromJug = fromJug - temp
 
        if ((fromJug == d) or (toJug == d)):
            return True
 
        if fromJug == 0:
            fromJug = fromJugCap
 
        if toJug == toJugCap:
            toJug = 0
        a-=1
             
    return False

if Pour(25,20,10):
   print("YES")