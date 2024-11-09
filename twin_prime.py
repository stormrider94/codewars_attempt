def is_twinprime(n):
    def checkPrime(v):
        factors=[]
        for i in range(1,v+1):
            if v%i==0:
                factors.append(i)
        if len(factors)==2:
            return True
        else:
            return False
    return checkPrime(n) and (checkPrime(n+2) or checkPrime(n-2))