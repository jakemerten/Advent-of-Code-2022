# Ended up counting inside cells in two different ways. Better w/o inside cells

body = set(tuple(map(int,e.split(","))) for e in open("day18input.txt","rt"))

neighbors = lambda x,y,z: ((x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1))

p1 = len(body)*6 - sum((p,q,r) in body for x,y,z in body for p,q,r in neighbors(x,y,z))

min_x,max_x = min(x for x,y,z in body), max(x for x,y,z in body)
min_y,max_y = min(y for x,y,z in body), max(y for x,y,z in body)
min_z,max_z = min(z for x,y,z in body), max(z for x,y,z in body)

outside = set()
candidates = [(min_x-1,min_y-1,min_z-1)]
while candidates:
  x,y,z = candidates.pop()
  outside.add((x,y,z))
  for p,q,r in neighbors(x,y,z):
    if min_x-1<=p<=max_x+1 and min_y-1<=q<=max_y+1 and min_z-1<=r<=max_z+1:
      if (p,q,r) not in body and (p,q,r) not in outside:
        candidates.append((p,q,r))

p2 = sum((p,q,r) in outside for x,y,z in body for p,q,r in neighbors(x,y,z))

print( p1,p2 )