import requests

res = requests.get("https://pastebin.com/raw/8vqQ8U4x")
pokemons = res.text.split('\n')


def printFirePokemons():
    Number_Of_Fire_Pokemons = 0

    for line in pokemons[1:]:
        fields = line.split(",")

        if len(fields) > 2 and fields[2] == 'Fire':
            Number_Of_Fire_Pokemons += 1

    print("Pocet ohnivych pokemonov je:",Number_Of_Fire_Pokemons)      

def printWaterFlyingPokemons():
    Number_Of_Water_Flying_Pokemons = 0

    for line in pokemons[1:]:
        fields = line.split(",")

        if len(fields) > 2 and fields[2] == 'Water' and fields[3] == 'Flying':
            Number_Of_Water_Flying_Pokemons += 1
    
    print("Pocet Vodnych a zaroven lietajucich pokemonov je: ", Number_Of_Water_Flying_Pokemons)


def printLastTen():
    print("Last 10 pokemons are: ")
    for i in range(len(pokemons) - 10, len(pokemons)):
        print(pokemons[i])


def AvgAttackOfAllPokemons():
    NumberOfAllPokemons = 0
    AttackValue = 0

    for line in pokemons[1:]:
        NumberOfAllPokemons += 1
        fields = line.split(",")

        if len(fields) > 6:
            AttackValue += int(fields[5])
        
    
    avgAttack = AttackValue/NumberOfAllPokemons
    print(avgAttack)







        
printLastTen()
printFirePokemons()
printWaterFlyingPokemons()
AvgAttackOfAllPokemons()
