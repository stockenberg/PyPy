p = {6, 23, 34, 76, 98, 8}

# dict
d = {}
# set
e = set()

# remove dup
# qlicates from list
s = set([1,2,3,4,5,6, 8, 5, 3, 5])

print(s)

for x in s:
    print(x)

if 3 in s:
    pass

if 5 not in s:
    pass

s.add(12)
s.update([5,4,3,2])

s.remove(3)
# no effect if item is no member
s.discard(6)

s.copy()

m = set(s)

'''Powerfull features'''

blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

blue_eyes.union(blond_hair)
blue_eyes.intersection(blond_hair)
blond_hair.difference(blue_eyes)
blond_hair.symmetric_difference(blue_eyes)
smell_hcn.issubset(blond_hair) # true
taste_ptc.issuperset(smell_hcn)
a_blood.isdisjoint(o_blood)

if blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes):
    pass

if blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair):
    pass  # FALSE

