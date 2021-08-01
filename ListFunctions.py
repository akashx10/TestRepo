
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ross", "Chandler", "Joey", "Rachel", "Monica", "Phoebe"]
friends.extend(lucky_numbers)  # order change does not work
lucky_numbers.append(52)   # does not work
friends.append("john cena")
friends.insert(1,"Ant Man")   # friends.remove("Ant Man"), friends.clear(), friends.pop()

print(friends)  # friends.sort() for alphabetical order, friends.reverse()

print(friends.index("Joey"))  # print(friends.count("Joey))

friends2 = friends.copy()

print(friends2)
