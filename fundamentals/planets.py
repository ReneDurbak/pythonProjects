import requests

rq = requests.get("https://api.le-systeme-solaire.net/rest/bodies/uranus").json()
planets = rq

def printMoonsOfUran():
    listOfMoons = planets.get('moons')
    print("//List of moons//")
    Number = 0

    for moon in listOfMoons:
        name = moon.get('moon')
        Number+=1
        print(f'{Number}.{name}')


printMoonsOfUran()