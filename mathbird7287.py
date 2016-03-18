database=[(1,2),(1,3),(1,5),(2,46),(3,4),(4,5),(5,6),(5,10),(5,46),(6,7),(6,8),(7,8),(7,9),(8,9),(9,10),(10,14),(10,27),(10,31),(10,41),(10,50),(10,76),
    (11,17),(11,28),(11,30),(12,27),(12,31),(13,14),(13,16),(14,16),(17,18),(16,17),(18,30),(19,20),(19,22),(19,28),(19,38),(20,24),(21,22),(21,26),(21,28),(21,38),(21,40),(22,33),(22,35),(22,37),(22,39),(23,32),(23,30),(24,39),(24,51),(25,26),(25,40),(25,28),(25,38),(26,35),(28,29),(28,30),(28,34),(29,30),(29,38),(29,40),(30,34),(33,35),(33,38),(33,40),(35,36),(35,40),(36,37),(36,39),(36,45),(36,47),(36,48),(37,40),(37,44),(38,43),(38,44),(38,49),(38,54),(38,55),(39,40),(39,42),(39,44),(42,51),(43,45),(45,47),(45,48),(46,51),(46,57),(47,48),(47,49),(48,49),(48,51),(50,61),(52,61),(51,70),(53,56),(54,55),(54,61),(56,61),(56,66),(57,85),(57,59),(60,61),(60,65),(60,71),(61,62),(61,63),(61,64)]

import sys
sys.setrecursionlimit(200)
n=1
#database=[(1,2),(1,3),(1,4),(4,5),(5,6),(6,7),(7,8),(7,9),(8,9)]

pps=raw_input("Enter steps per second (default is 2) ==> ")

if type(eval(pps))==int:
     pps=int(pps)
else:
     pps=2





walkingspeed=1

def i(s1):
     r=[]
     for m in database:
          if m[0]==s1:
               r.append(m[1])
          if m[1]==s1:
               r.append(m[0])
     return r
#print i(1)
#print i(2)
#print i(3)

value=0

def distance((s1,s2),(e1,e2)):
    return float(abs(s1-e1)/2.+abs(s2-e2)/2.)
    
    
def optimize1(s1,s2,e1,e2,restricted=[],depth=0,path=[],lookedat={},printe=True):
    global value
    print s1,s2, "///",depth
    path=[(0,0)]*99 # this is just a base thing
    # print s1,s2,e1,e2
    if (s1==e1 and s2==e2):
        return depth; # this is clearly incorrect, but it doesn't really matter.
    #what is printed matters.
    news=[]
    for a in i(s1):
        if (a,s1) not in restricted  and (s1,a) not in restricted and a!=s2:
            news.append((a,s1))
    for b in i(s2):
        if (b,s2) not in restricted  and (s2,b) not in restricted and b!=s1:
            news.append((s2,b)) # where you can go...
    minval=999999
    c=999999
    print news
    s=999999 # default values. Treat "999999" like an error.
    # print "curent value:",c
    for item in news:
        d=1
        #d=distance(item[0],item[1],s1,s2)
        # print item, path
        # print "Running from vertex:",item[1],",",item[0]
        if ((not lookedat.has_key((item[0],item[1])) and not lookedat.has_key((item[1],item[0]))) or (lookedat.has_key((item[0],item[1])) and lookedat[(item[0],item[1])]>depth+d) or (lookedat.has_key((item[1],item[0])) and lookedat[(item[1],item[0])]>depth+d)): # tests if this is the best (currently) path
            lookedat[(item[0],item[1])]=depth+d
            # print "optimizing route from (",item[1],",",item[0],"): %d: %d"%(depth,1)
            if ((item[0],item[1])==(e1,e2) or (e1,e2)==(item[1],item[0])):
                c=depth+d
                print "Mommy"
            print "RESTRICTED:",restricted
            s=optimize1(item[1],item[0],e1,e2,restricted+[(s1,s2)],depth+d,path)
            print item[1],item[0],s
        # print "Distance:",s
        if s<minval:
            minval=s
            bestlocation=[(item[1],item[0])]
            path[depth]=bestlocation[0]
            
            c=minval
            
            
            # print "go to %d, %d after you"%(b[0][0],b[0][1])
            
    #print depth+c, "depth"
    if depth==0:
        that=(s1,s2)
        for it in path:
            if it!=(0,0):
                
                print "to",it
                value+=distance(it,that)
                print distance(it,that)
                # value+=1
                that=it
                # optimize1(it[0],it[1],e1,e2)
    
    return c

print optimize1(1,2,8,9)
print "Number of steps:",value/walkingspeed            