# second version

gravity = {
    "Sun": 27.9,
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1,
    "Moon": 0.165,
    "Mars": 0.376,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06
}

replies = {
    "Sun": "You must be hot, thats why you are heading to the Sun!",
    "Mercury": "Running from problems? Mercury is the fastest planet!",
    "Venus": "Careful stepping on Venus, its hotter than your exs temper!",
    "Earth": "Chill out blud... you are already on planet Earth unless you are an alien using my code!!",
    "Moon": "The Moon is basically a cosmic trampoline! Bounce all day!",
    "Mars": "Mars is like a dusty playground, red sand everywhere!",
    "Jupiter": "Biggest boss in the Solar System, Jupiter will not let you move!",
    "Saturn": "Thinking of proposing? Saturn is already flexing rings all around!",
    "Uranus": "Uranus spins sideways like it partied too hard last night!",
    "Neptune": "Got anger issues? Neptune might cool you down!",
    "Pluto": "Feeling ghosted by Earth? Pluto knows the pain of being left out..."
}

weight = float(input("Enter your weight on Earth (kg): "))
planet = input("Enter a planet (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto): ")

if planet in gravity:
    if planet == "Earth":  
        print(replies[planet])
    else:
        new_weight = weight * gravity[planet]
        print(f"{replies[planet]} On {planet}, your weight would be {new_weight:.2f} kg!!")
else:
    print("Blud... this ains even in our Solar System!! Stop making up planets!! ")
