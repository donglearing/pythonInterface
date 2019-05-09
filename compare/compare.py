def compare(L):
    minnum = L[0]
    maxnum = L[0]
    for i in range(len(L)):
       # minnum=L[0]
       # maxnum=L[0]
        if minnum>L[i]:
            minnum=L[i]
        elif maxnum<L[i]:
            maxnum=L[i]
    return (maxnum,minnum)
#if __name__ == "__main__":
  #  lista=[2,33,1,44,56]
  #  print(compare(lista))
