def ranks(a):
    #a represents the array passed into the function
    #we create an empty array and push the ranks as values into the array
    rank_dic={}
    print(a)
    rank=1
    #we want the biggest number to have the highest rank much like positions in results
    print(sorted(a,reverse=True))
    for el in sorted(a,reverse=True):
        if el not in rank_dic:
            rank_dic[el]=rank
            rank= rank+1
        else:
            rank=rank+1
    # we loop through each member in a and return its corresponding rank
    rank_list=[rank_dic[num] for num in a]
    print(rank_list)
    return(rank_list)