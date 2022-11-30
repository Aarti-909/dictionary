# SETS
# KEY POINTS:
'''
1.sets are unordered(indexing not iterable)
2.Use in operator to access the element of a set
3.sets do not allow duplicats
4.We can take Imutable data type in sets(tuple,str,bool) we can't use mutable (list)
5.l=[2,3,4,5,2,5,6] :: s=set(l)
6.Method:

  add() ---
  s={"a","b"}
  s.add("d")

  update---
  t={"1","2"}
  t={1:4,2:3}  if we take t as a dict then only key will be updated
  s.update(t)
  
  Remove()----
  s={1,2,3,4,5,2}
  s.remove(2)
  s.remove(6) it will error show as 6 is not present for this (s.discard(4)) no error will be shown

  clear()-----
  a={12,23,324}
  a.clear()

  union()----
  k={1,1,1,2,2,3}
  l={1,1,2,2,4}
  print(k|l)
  v=k.union(l)
  print(v)

  intersection()-----
  k={1,1,1,2,2,3}
  l={1,1,2,2,4}
  print(k&l)
  v=k.intersection(l)

  intersecton_update()-----
  k={1,1,1,2,2,3}
  l={1,1,2,2,4}
  k.intersection_update(l)

  symmetric difference()-----
  s={1,2,3}
  t={2,3,4}
  print(s^t)
  v=s.symmetric_difference(t) same for update

  .isdisjoint()---- Check whether two sets are disjoint
  s={1,2,3}
  t={2,3,4}
  print(s.isdisjoint(t) False


  is.subset() and is.superset()----
  b={5,9,7}
  s={!,5,9,7,(5,7),(5,9),(9,7),(5,9,7)}
  a={9,7}
  a.issubset(b)
  



'''

# a={int,complex ,str,bool}
# this={a,"a",True,[1,2]}
# s={False,False,True}
# print(s)
# b={"a","b"}
# for item in b:
#     print(item)
# s={"a",1,1,True}
# print(s)
# print(len(s))


# s={"a","b","c"}
# print(s)
# s.pop()
# s.pop()
# print(s)
s={1,2,3}
t={2,3,4}
print(s.isdisjoint(t))
