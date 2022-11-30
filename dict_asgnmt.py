# Write a Python script to add a key to a dictionary.
'''
d={}
while True:
    n=input()
    n1=input()
    if n!="":
        d[n]=n1
    else:
        break
print(d)
'''


# Write a Python script to concatenate the following dictionaries to create a new one.
'''
d={}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d4={**dic1,**dic2,**dic3}
print(d4)
'''


#Write a Python script to check whether a given key already exists in a dictionary.
'''
d={}
while True:
    n=input()
    n1=input()
    if n!="":
        d[n]=n1
    else:
        break
print(d)
p=d.keys()
k=input("what key u want to check: ")
if k in p:
    print("yes")
else:
    print("no")
'''


# Write a Python program to iterate over dictionaries using for loops
'''
d={}
while True:
    n=input()
    n1=input()
    if n!="":
        d[n]=n1
    else:
        break
print(d)

d={"hope":1,"honye":3}

for i in d.items():
    print(i)
'''

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''
d={}
p=int(input())
i=1
while i<=p:
    n=i
    if n!="":
        d[n]=i*i
    else:
        break
    i+=1
print(d)
'''

# Write a Python program to remove a key from a dictionary
'''
d={}
p=int(input())
i=0
while i<p:
    n=input()
    n1=input()
    if n!="":
        d[n]=n1
    else:
        break
    i+=1
print(d)
a=input()
d.pop(a)
print(d)
'''

# Write a Python program to map two lists into a dictionary.
'''
a=["Name","age","weight","hobby","Bf"]
b=["Aarti Thakur",19,39,"Mandala art","Vaishali and Honey"]
d={}
for i in range(len(a)):
    d[a[i]]=b[i]
print(d)
'''

# Write a Python program to get the maximum and minimum value in a dictionary.
'''
d={}
p=int(input())
i=0
while i<p:
    n=input()
    n1=int(input())
    if n!="":
        d[n]=n1
    else:
        break
    i+=1
print(d)
k=(d.values())
print(max(k),"is min")
print(min(k),"is min")
'''

# Write a Python program to check if a dictionary is empty or not.
'''
d={}
p=int(input())
i=0
while i<p:
    n=input()
    n1=int(input())
    if n!="":
        d[n]=n1
    else:
        break
    i+=1
print(d)
if len(d)>=1:
    print("non-empty")
else:
    print("empty")
'''


# Write a Python program to combine two dictionary adding values for common keys.
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
p=list(d1.keys())
p1=list(d2.keys())
l=list(d1.values())
l1=list(d2.values())
d={}
for i in range(len(d1)):
    if p[i]==p1[i]:
        d[p[i]]=l[i]+l1[i]
    d[p[i]]=l[i]
    d[p1[i]]=l1[i]
print(d)
'''

# 13 Write a Python program to create a dictionary that stores the count of the occurrences of a letter from a string.

'''
d={}
s="This is a string"
for ch in s:
    d.setdefault(ch,0)
    d[ch]+=1
print(d)


for i in s:
    if i not in d.keys():
        d[i]=0
    d[i]+=1
print(d)
'''

# 14 Write a Python program to remove spaces from dictionary keys.
# INCOMPLETE



# 15 Write a Python program to get the key, value and item in a dictionary.
'''
d={}
p=int(input())
i=0
while i<p:
    n=input()
    n1=int(input())
    if n!="":
        d[n]=n1
    else:
        break
    i+=1
print(d)

s=d.keys()
s1=d.values()
s2=d.items()
'''


# 16 DOUBT:

# 17 Write a Python program to filter a dictionary based on values
'''
d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
p=int(input())
i=0
while i<p:
    n=input()
    n1=int(input())
    if n!="":
        d[n]=n1
    else:
        break
    i+=1
print(d)
j=0
l=list(d.values())
l1=list(d.keys())
k={}
s=int(input())
while j<len(l):
    if l[j]>s:
        k[l1[j]]=l[j]
    j+=1
print(k)
'''

#18 Write a Python program to filter the students based on their height and weight, which are stored in a dictionary.
'''

DOUBT

d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
i=0
d1=list((d.values()))
s={}
while len(d1)>i:
    j=0
    while j<i:
        print(d[j])
        if d1[0]>6 and d1[1]>70:
            s[d[i]]=d1[i]
        j+=1
    i+=1
print(s)


# COMPLETE
i=0
d2=list(d.keys())
d1=list((d.values()))
s={}
for i in range(len(d1)):
    a=list(d1[i])
    if a[0]>=6 and a[1]>=70:
        s[d2[i]]=d1[i]
        # print(a)
print(s)
'''

#20 Write a Python program to sort a given dictionary by key.
'''
# d={}
# p=int(input())
# i=0
# while i<p:
#     n=input()
#     n1=int(input())
#     if n!="":
#         d[n]=n1
#     else:
#         break
#     i+=1
# print(d)

d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}


l=list(d.keys())
l.sort()
p={}
for i in l:
    p[i]=d[i]
print(p)
'''


#21 Write a Python script to sort (ascending and descending) a dictionary by value

'''
d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
ASCENDING
l=list(d.keys())
l1=list(d.values())
p=l1.copy()
l1.sort()
s={}
i=0
while i<len(l1):
    k=p.index(l1[i])
    s[l[k]]=l1[i]
    i+=1
print(s)

# DESCENDING
l=list(d.keys())
l1=list(d.values())
p=l1.copy()
l1.sort()
l1.reverse()
s={}
i=0
while i<len(l1):
    k=p.index(l1[i])
    s[l[k]]=l1[i]
    i+=1
print(s)
'''

# 22 Write a Python program to split a given dictionary of lists into a list of dictionaries.
    # Original dictionary of lists:
    # d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
    # Split said dictionary of lists into list of dictionaries:
    # [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
'''
i=0
d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
i=0
a=list(d.keys())
b=list(d.values())
p=[]
while i<len(b)-1:
    j=0
    s={}
    while j<len(b[0]):
        s[a[i]]=b[i][j]
        s[a[i+1]]=b[i+1][j]
        p.append(s)
        j+=1
        s={}
    i+=1 
print(p)
'''


# 23 Write a Python program to extract a list of values from a given list of dictionaries.
'''
d=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
d1=[]
i=0
sub=input()
while len(d)>i:
    k=0
    while k<len(d[i]):
        s=list(d[i].keys())
        s1=list(d[i].values())
        if s[k]==sub:
            d1.append(s1[k])
        k+=1
    i+=1
print(d1)
'''


#24 Write a Python program to filter even numbers from a given dictionary values.
d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
k=list(d.values())
p=list(d.keys())
j=0
print(k)
print(p)
while j<len(k):
    i=0
    s={}
    while i<len(p[j]):
        if k[i][j]%2==0:
            s[p[j]]=k[j]
        i+=1
    j+=1
print(s)

# s={}
# while j<len(d):
#     if k[j]%2==0:
#         s[p[j]]=k[j]
#     j+=1
# print(s)
