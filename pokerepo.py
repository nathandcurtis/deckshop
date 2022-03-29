from pokemontcgsdk import Card


for i in range(0, 25):
    charizard = Card.find('swsh4-' + str(i + 1))
    print(charizard.name + " HP: " + charizard.hp)

#charizard = Card.find('swsh4-26')
#print(charizard.name + " HP: " + charizard.hp)
