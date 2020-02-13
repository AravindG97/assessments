a=[(),("a","b","c"),("","")]
for x in a:
    if len(x)==0:
        print("empty tuple {}".format(x))
    else:
        print("non empty tuple {}".format(x))
