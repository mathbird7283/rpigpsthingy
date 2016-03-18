database=[(1,2),(1,3),(1,4),(2,46),(3,4),(4,5),(5,6),(5,10),(5,46),(6,7),(6,8),(7,8),(7,9),(8,9)]



# database=[(1,2),(1,3),(1,4),(4,5),(5,6),(6,7),(7,8),(7,9),(8,9)]


def i(s1):
    r=[]
    for m in database:
        if m[0]==s1:
            r.append(m[1])
        if m[1]==s1:
            r.append(m[0])
    return r
print i(1)
print i(2)
print i(3)


def optimize1(s1,s2,e1,e2,restricted=[],depth=0,path=[],lookedat={}):

    
    
    path=[(0,0)]*999
    # print s1,s2,e1,e2
    if (s1==e1 and s2==e2):
        return depth;
    news=[]
    for a in i(s1):
        if (a,s1) not in restricted  and (s1,a) not in restricted and a!=s2:
            news.append((a,s1))
    for b in i(s2):
        if (b,s2) not in restricted  and (s2,b) not in restricted and b!=s1:
            news.append((s2,b))
    minval=999999
    c=999999
    s=999999
    # print "curent value:",c
    for item in news:
        print item
        # print "Running from vertex:",item[1],",",item[0]
        if ((not lookedat.has_key((item[0],item[1])) and not lookedat.has_key((item[1],item[0]))) or (lookedat.has_key((item[0],item[1])) and lookedat[(item[0],item[1])]>depth+c) or (lookedat.has_key((item[1],item[0])) and lookedat[(item[1],item[0])]>depth+c)):
            lookedat[(item[0],item[1])]=depth+c
            print "optimizing route from (",item[1],",",item[0],"): %d: %d"%(depth,c)
            if ((item[0],item[1])==(e1,e2) or (e1,e2)==(item[1],item[0])):
                c=depth+1
            s=optimize1(item[1],item[0],e1,e2,restricted+[(s1,s2)],depth+1,path)
        # print "Distance:",s
        if s<minval:
            minval=s
            print "Mommy."
            bestlocation=[(item[1],item[0])]
        
            path[depth]=bestlocation
            
            b=bestlocation
            c=minval
            
            # print "go to %d, %d after you"%(b[0][0],b[0][1])
            
    #print depth+c, "depth"
    if depth==0:
        for it in path:
            if it!=(0,0):
                print "to",it
    return c

print optimize1(1,2,8,9)
            