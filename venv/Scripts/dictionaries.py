stuff = {'food': 15, "energy": 100, 'enemis': 3}

print(stuff.get('food'))
print(stuff.items())
print(stuff.keys())
print(stuff.popitem())
print(stuff)

print(stuff.setdefault('food'))
print(stuff)
print(stuff.setdefault('friends', 123))
print(stuff)

new_items = {'rocks': 4, 'arrow': 18}
stuff.update(new_items)
print(stuff)

new_items = {'rocks': 2, 'arrow': 5}
stuff.update(new_items)
print(stuff)