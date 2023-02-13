def isEugle():
    g = [[0,1,6,0],[0,0,9,1],[7,7,6,7],[1,0,0,0]]
    h = []
    e = []
    idk = 0
    for i in g:
        h.append(sum(i))
    for j in h:
        e.append(j%2)
    for k in e:
        if k == 1:
            idk += 1
            if idk == 3:
                return False
    return True        
print(isEugle())
