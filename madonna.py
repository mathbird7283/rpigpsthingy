def i(s1):
    r=[]
    for m in database:
        if m[0]==s1:
            r.append(m[1])
        if m[1]==s1:
            r.append(m[0])
    return r


def optimize1(s1,s2,e1,e2,restricted=[]):
    if (s1==s2 and e1==e2):
        print "go to %d, %d\n after you "%(s1,s2)
        return 0;
    news=[]
    for a in i(s1):
        news.append((a,s1))
    for b in i(s2):
        news.append((s2,b))
    minval=999999
    for item in news:
        s=optimize1(news[1],news[0],e1,e2,restricted+[(s1,s2)])
        if s<minval:
            minval=s
            bestlocation=[(news[1],news[0])]
        
    b=bestlocation
    c=minval
    
    print "go to %d,%d\n after you"%(b[0][0],b[0][1])
    return c;
            