import random
def maxinrange(tab,a,b):
    maxi = tab[0]
    i = 0
    for i in range(a,b+1):
        if tab[i] > maxi:
            maxi = tab[i]
    for i in range(a,b+1):
        if tab[i] == maxi:
            return i
    return i
def trie(tab,n):
    for i in range(n-1,0,-1):
        s = tab[i]
        l = maxinrange(tab,0,i)
        tab[i] = tab[l]
        tab[l] = s
    return tab
def esttrie(tab):
    for i in range(len(tab)-1):
        if t[i] > t[i+1]:
            return False
    return True
for m in range(0,input("Nb de repetition: ")):   
    t = [0]*20
    for i in range(20):
       t[i] = random.randint(-50,50)
    print(trie(t,len(t)),esttrie(t))

