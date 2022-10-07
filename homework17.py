seta={1,10,"hi",7}
setb={1,10,"hi",7,8,0}
print(seta.isdisjoint(setb))
print(seta.issubset(setb))
print(setb.issuperset(seta))

dictionary={
    1:"A",
    2:"B",
    3:"C",
    }
print(dictionary)
print(len(dictionary))
print(dictionary.keys())
print(dictionary.items())
print(dictionary.keys())
get=dictionary.get(1)
print(get)
dictionary.update({4:"a"})
print(dictionary)
dictionary.pop(1)
print(dictionary)
dictionary.popitem()
print(dictionary)

