def g(x):
    (q,d) = (1,0)
    while q <= x:
      print ("Step" + str(d) + "," + str(q))
      (q,d) = (q*10,d+1)
    return(d)

q1 = g(31415927)
print (q1)
print ("********************************************************************")
def h(m,n):
    ans = 0
    while (m >= n):
      print ("Step " + str(ans) + "," + str(m))
      (ans,m) = (ans+1,m-n) 
    return(ans)
q2 = h(231,8)
print (q2)
print ("********************************************************************")

def h(n):
 f=0
 for i in range(1,n+1):
  if n% i ==0:
   f = f + 1
 return (f%2 == 1)

q3 = h(169)
print (q3)

print ("********************************************************************")

def f(m):
 if m == 0:
  return(0)
 else:
  return(m+f(m-1))

q4=f(-10)
print (q4)
