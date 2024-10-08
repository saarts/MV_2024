"""

<
>
>=
<=
==
!=




tingimuslausete näited
IF
IF ELSE
"""

a = 1
b = 3

if a>b:
    print("a on suurem b-st")
elif a>0:
    print("a on suurem nullist")
else:
    print("a on väiksem nullist")
    
if a>0 and a<b:
    print("a on väiksem b-st ja suurem nullist")
    
if a<b or a>0:
    print("a on väiksem b-st ja suurem nullist")