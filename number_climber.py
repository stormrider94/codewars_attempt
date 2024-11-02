def climb(n):
        # my concern is that how do you know if the next number will be gotten by muliplying by 2 
        # or by multiplying by 2 and adding  1?  The secret is to just check if the number is odd or even

        # the only way is to start from n and try getting and try dividing by 1 or adding 2
        # so if we get a decimal after dividing by 2 our only option is to make it even by subtracting 1 and dividing by 2
        
        sequence_li = []
        sequence_li.append(int(n))
        while(n!=1):
            if n%2 ==0:
                n//=2
            else:
                n=(n-1)//2
            sequence_li.append(n)
        print(sorted(sequence_li))
        return sorted(sequence_li)