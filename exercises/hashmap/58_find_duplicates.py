
def find_duplicates(mylist):
    dups = set()
    found = {}
    for item in mylist:
        item = int(item)
        if item in found:
            dups.add(item)
        else:
            found[item] = True


    return list(dups)


print ( find_duplicates([1, 1, 2, 2, 3, 'a', 2]) )




