games = {'rdr2','gta 5','mortal kombat','blood strike','battelfield5',"gta 5"}
games1 = {'gta 5','rdr1','cs2','mk1',"doom enternal"}
games = set(games)
print(type(games))
print(games.union(games1))
print(games1.difference(games))
#Add
games1.add("bs2040")
print(games1)
#remove
games1.remove()