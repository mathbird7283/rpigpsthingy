database=[(1,2),(1,3),(1,5),(2,46),(3,4),(4,5),(5,6),(5,10),(5,46),(6,7),(6,8),(7,8),(7,9),(8,9),(9,10),(10,14),(10,27),(10,31),(10,41),(10,50),(10,76),(11,17),(11,28),(11,30),(12,27),(12,31),(13,14),(13,16),(14,16),(17,18),(16,17),(18,30),(19,20),(19,22),(19,28),(19,38),(20,24),(21,22),(21,26),(21,28),(21,38),(21,40),(22,33),(22,35),(22,37),(22,39),(23,32),(23,30),(24,39),(24,51),(25,26),(25,40),(25,28),(25,38),(26,35),(28,29),(28,30),(28,34),(29,30),(29,38),(29,40),(30,34),(33,35),(33,38),(33,40),(35,36),(35,40),(36,37),(36,39),(36,45),(36,47),(36,48),(37,40),(37,44),(38,43),(38,44),(38,49),(38,54),(38,55),(39,40),(39,42),(39,44),(42,51),(43,45),(45,47),(45,48),(46,51),(46,57),(47,48),(47,49),(48,49),(48,51),(50,61),(52,61),(51,70),(53,56),(54,55),(54,61),(56,61),(56,66),(57,85),(57,59),(60,61),(60,65),(60,71),(61,62),(61,63),(61,64),(63,64),(63,66),(63,68),(64,67),(64,71),(65,71),(65,76),(66,67),(66,69),(67,68),(69,71),(70,71),(70,89),(71,72),(71,74),(71,76),(71,78),(71,100),(72,73),(72,74),(73,74),(73,75),(73,80),(74,79),(74,80),(75,76),(76,77),(76,81),(76,83),(76,85),(76,87),(76,89),(76,99),(77,82),(79,90),(80,83),(81,82),(81,84),(81,88),(82,83),(82,85),(83,84),(83,88),(83,94),(83,98),(83,100),(86,87),(87,92),(88,91),(88,93),(89,99),(90,99),(91,94),(91,98),(94,95),(95,96),(96,99),(97,98),(98,99)]

def visualize1(n=8):
     if (n<4):
          raise ValueError("graph size must be at least 4")
     from Lgraphics import GraphWin, Circle, Line, Point, Text
     
     w=GraphWin("Rensselaer Polytechnic Institute... simplified",n*100,n*100)
     d={0:'black',1:'blue',2:'red',3:'yellow',4:'orange',5:'pink',6:'green',7:'purple',8:'brown',9:'gray'}
     for i in database:
          x=Circle(Point(n*i[0],n*i[1]),int(n/2-1))
          a=(i[0]+i[1])%10
          #color=d[a]
          x.setFill('black')
          x.draw(w)
     
     for i in database:
          for j in database:
               if (i==j):
                    continue
               s=0
               if (i[0]==j[1]):
                    s=i[0]
               elif (i[0]==j[0]):
                    s=i[0]
               elif (i[1]==j[1]):
                    s=i[1]
               elif (i[1]==j[0]):
                    s=i[1]
               else:
                    continue
               print "Line drawn.",i,j
               l=Line(Point(n*i[0],n*i[1]),Point(n*j[0],n*j[1]))
               l.setOutline(d[s%10])
               l.draw(w)
               
     w.getMouse()
     w.close()
     
visualize1.__doc__="""
This function prints out a simplified RPI campus map.

The colors of the lines represent the last digit of the route number.

{0:'black',1:'blue',2:'red',3:'yellow',4:'orange',5:'pink',6:'green',7:'purple',8:'brown',9:'gray'}

Takes in a number indicating the size of the graph in square hectopixels (must be at least 4, defaults to 8)
"""
#visualize1()

def adj(i1,i2):
     a=i1%2
     b=i2%2
     if (a==1 and b==0):
          return (i2,i1)
     else:
          return (i1,i2)
     
def lookat((a,b),(c,d),database):
     if a==c:
          t=b
          u=d
          if (d<b):
               t=d
               u=b
     if a==d: 
          t=b
          u=c
          if (c<b):
               t=c
               u=b
     if b==c:
          t=a
          u=d
          if (d<a):
               t=d
               u=a
     if b==d:
          t=b
          u=d
          if (d<b):
               t=d
               u=b
     i=t+1
     while i<u:
          if (a,i) in database or (i,a) in database:
               return False
          i+=1
     return True

def visualize2(n=8):
     if (n<6):
          raise ValueError("graph size must be at least 4")
     from Lgraphics import GraphWin, Circle, Line, Point, Text
     
     w=GraphWin("Rensselaer Polytechnic Institute... simplified",n*100,n*100)
     d={0:'black',1:'blue',2:'red',3:'yellow',4:'orange',5:'pink',6:'green',7:'purple',8:'brown',9:'gray'}
     for i in database:
          x=Circle(Point(n*adj(i[0],i[1])[0],n*adj(i[0],i[1])[1]),int(n/2-1))
          a=(i[0]+i[1])%10
          #color=d[a]
          x.setFill('black')
          x.draw(w)
     
     for i in database:
          for j in database:
               if (i==j):
                    continue
               s=0
               if (i[0]==j[1]):
                    s=i[0]
               elif (i[0]==j[0]):
                    s=i[0]
               elif (i[1]==j[1]):
                    s=i[1]
               elif (i[1]==j[0]):
                    s=i[1]
               else:
                    continue
               #print "Line drawn.",i,j
               l=Line(Point(n*adj(i[0],i[1])[0],n*adj(i[0],i[1])[1]),Point(n*adj(j[0],j[1])[0],n*adj(j[0],j[1])[1]))
               l.setOutline(d[s%10])
               if lookat(i,j,database):
                    print i,j
                    l.draw(w)
                    t=Text(l.getCenter(),str(s))
                    t.setSize(n-1)
                    t.draw(w)
               
     w.getMouse()
     w.close()
     
visualize2.__doc__="""
This function prints out a better simplified RPI campus map.

The colors of the lines represent the last digit of the route number.

{0:'black',1:'blue',2:'red',3:'yellow',4:'orange',5:'pink',6:'green',7:'purple',8:'brown',9:'gray'}

Takes in a number indicating the size of the graph in square hectopixels (must be at least 6, defaults to 8)
"""
visualize2()
          




print len(database)

## NEW IDEA: Create a dictionary called "edges" that contains all possible edges betwene 2 points. Whne you look at an edge and have not reached the desired vertex, remove it. 

import sys
sys.setrecursionlimit(140)
n=1
#database=[(1,2),(1,3),(1,4),(4,5),(5,6),(6,7),(7,8),(7,9),(8,9)]

debug=eval(str.capitalize(raw_input("Debug run? If you do many print statements will appear. Enter true or false ==> ")))

pps=raw_input("Enter steps per second (default is 2) ==> ")

if type(eval(pps))==int:
     pps=int(pps)
else:
     pps=2


def dprint(x):
     if debug: print x


walkingspeed=3.5 # mph

walkingspeed*=(5280/3600.) # converts miles per hour to feet per second

steplength=3 # feet

aval=2140335

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

def tsort((a,b)):
     if (a<b):
          return (a,b)
     else:
          return (b,a)
     

ashley=[]

def optimize1(s1,s2,e1,e2,restricted=[],depth=0,path=[],printe=True,d={}):
     if ((s1,s2) not in database and (s2,s1) not in database) or ((e1,e2) not in database and (e2,e1) not in database):
          dprint((s1,s2))
          dprint((e1,e2))
          raise ValueError("point not in sector of examination")
     g=list(path)
     if len(g)==0:
          global ashley
     # this is really just a surprisingly complicated and generalized DFS
     global aval
     global value
     for item in database:
          d[tsort(item)]=9999
     if (d[tsort((s1,s2))]>depth and (depth<aval or ((depth ==aval) and set((s1,s2))==set((e1,e2))))):
          dprint( str(s1)+" "+str(s2)+"///"+str(depth))
          d[tsort((s1,s2))]=depth
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
          dprint(news)
          s=999999 # default values. Treat "999999" like an error.
          # print "curent value:",c
          for item in news:
               d1=1
               #d1=distance(item[0],item[1],s1,s2)
               # print item, path
               # print "Running from vertex:",item[1],",",item[0]
               if ((not d.has_key((item[0],item[1])) and not d.has_key((item[1],item[0]))) or (d.has_key((item[0],item[1])) and d[(item[0],item[1])]>depth) or (d.has_key((item[1],item[0])) and d[(item[1],item[0])]>depth)): # tests if this is the best (currently) path
                    d[tsort((item[0],item[1]))]=depth+d1
                    # print "optimizing route from (",item[1],",",item[0],"): %d: %d"%(depth,1)
                    newpath=path+[(s1,s2)]
                    if ((item[0],item[1])==(e1,e2) or (e1,e2)==(item[1],item[0])):
                         c=depth+d1
                         dprint (("Mommy", depth))
                         aval=depth
                         ashley=newpath
                         print (len(ashley)+1),":",ashley+[(e1,e2)]
                    else:
                         dprint (("RESTRICTED:",restricted))
                         newd=d
                         
                         s=optimize1(item[1],item[0],e1,e2,restricted+[(s1,s2)],depth+d1,newpath,printe,newd)
                    dprint(( item[1],item[0],s ))
               # print "Distance:",s
               if s<minval:
                    minval=s
                    # bestlocation=[(item[1],item[0])]
                    # path[depth]=bestlocation[0]
                 
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
          if len(g)==0:
               dprint((path, "is not None"))
               dprint(ashley)
               dprint(len(path))
         
          return c
print optimize1(1,2,63,64)
print "Number of steps:",aval+1,":",value/walkingspeed 
data="""1	River Street
2	Passes By Pi Kappa Phi
3	3rd Street
4	Broadway
5	6th Ave
6	Path by Uncle Sam Lanes
7	Parking Area (accessible from 9)
8	The Approach
9	8th Street
10	Peoples Ave (turns toward PiPhi)
11	Winding path by Carnegie
12	Parking lot by Alumni House
13	Path to West Hall
14	Sage Avenue (to 15th St)
15	West Hall, Main Path
16	West Hall Lot
17	Path Behind Carnegie
18	Past Pittsburgh to 30
19	Paved path around EMPAC
20	Route (same as 19) to parking garage
21	Walkway by Library
22	Path from 19 (by EMPAC) to 39
23	Path between Sage and Walker
24	College Avenue
25	Two parts: next to 21 most of its way, from AE/Lally to VCC
26	Passes by VCC on right side (coming from 21)
27	11th Street
28	Paved path by Greene/Lally/Eaton. Turns toward 11.
29	Cuts from Sage building, along brick pathtoward JROWL
30	Major paved path from Carnegie to 34
31	Path near J Building
32	Path behind Sage
33	Path from main arterial path around, crossing 33, to Cogswell
34	Principal paved path from Greene/29 to 87 gym
35	Path by basement of Greene. 
36	Sidewalk by 34, extends into Quad
37	Just west of 37, multipave, curves around toward 87 gym
38	Main Path (up to footbridge)
39	Main path by DCC, curves through middle of 86 field
40	Path by J-ROWL
41	13th Street, turns toward Pikes
42	Path by Biotech
43	Path by Chruch 6, between 87 gym and the Quad
44	Path around CII/Biotech
45	U-shaped, from back of RSDH to my dorm
46	Congress Street
47	From 45 to 48
48	From Union around to 36 (through Quad)
49	Path from Biotech Entrace past Playhouse, extends yto end of 47
50	15th St to Sage Ave, Sage Ave to 61
51	15th St (past 50)
52	Parking lot for Union
53	Path by rmory
54	(1500) stinky path
55	Circles the union
56	Main paved parking path by the Mueller Center
57	Pawling St
58	Myrtle Ave
59	Pinewood St
60	extension of 50 (to 71)
61	Griswold Road
62	Path behind Cary and Bray (around Barton)
63	Western path by Wareen
64	Extension of 38
65	Sherry Rd
66	Path by Warren and Nason
67	Like 63 but opposite Commons
68	Path by Sharp (cringe)
69	Parking Lot off of 71
70	Tibbits Ave
71	Burdett Ave
72	Path right of BARH
73	Path through BARH
74	Path left of BARH
75	Extention by Field House
76	Peoples Ave (after 10, toward 89/99)
77	Track Area
78	Colonie Path
79	Around Rahps 9x
80	Parking lot Path not a;lready represented
81	Behind HFH
82	Path fro 81 to 83
83	Paved path by ECAV (vital!)
84	Past ECAV, vertical steps
85	Spin-off of 83
86	83 turns in RAHPS
87	86 turns in RAHPS, reaches parking lot
88	Path by Rugby Field(?)
89	Frat path Sunset Terrace
90	Circular end to 89
91	Path under RAHPS B
92	Next to ECAV?
93	Midway through RAHPS B
94	Out by Stack
95	Past Stack
96	Through Bryck
97	Route to Shirley|s House
98	Path by Colonie and Bryckwyck
99	Sunset Terrace
100	Hoosick Street"""

s=data.replace("\t",":'").replace("\n","',")
print s
t = "{"+s+"'}"
print t

print "Key",eval(t)