MarbleLeague = {
    "Balls of Chaos",
    "Chocolatiers",
    "Jawbreakers",
    "Kobalts",
    "Limers",
    "Mellow Yellow",
    "Oceanics",
    "O'rangers",
    "Pinkies",
    "Rojo Rollers"
}
MarbleLeague2 = {
    "Savage Speeders",
    "Snowballs",
    "Team Galactic",
    "Team Momo",
    "Team Primary",
    "Limers",
    "Jungle Jumpers",
    "Midnight Wisps",
    "Quicksilvers",
    "Shining Swarm"
    }
MarbleLeague3 = {
    "Crazy Cat's Eyes",
    "Hazers",
    "Minty Maniacs",
    "Raspberry Racers",
    "Team Momary",
    "Green Ducks",
    "Indigo Stars",
    "Limers",
    "Hornets",
    "O'Rangers"
}
MarbleLeague4 = {
    "Raspberry Racers",
    "Rojo Rollers",
    "Savage Speeders",
    "Snowballs",
    "Team Galactic",
    "Limers",
    "Balls of Chaos",
    "Chocolatiers",
    "Jawbreakers",
    "Kobalts",
}
intersection = MarbleLeague.intersection(MarbleLeague2,MarbleLeague3,MarbleLeague4)
print("Intersection lul")
print(intersection)
difference = MarbleLeague.difference(MarbleLeague2,MarbleLeague3,MarbleLeague4)
print("Difference")
print(difference)
Onio = MarbleLeague.union(MarbleLeague2,MarbleLeague3,MarbleLeague4)
print("A GOOD ONIO IS A HEVI ONIO(union)")
print(Onio)
upperset1= MarbleLeague.issuperset(MarbleLeague2)
print(upperset1)
upperset2= MarbleLeague3.issuperset(MarbleLeague4)
print(upperset2)
#uppersetFINALLE = upperset1.issuperset(upperset2) Poprzednie zwracają FALSE
print("Issuperset")