# Project 1: Weight Calculator Across the Solar System

#first version 

planet = str(input("Enter which planet, star, or moon you want to check: ")).lower()
weight = float(input("Enter your weight on planet Earth (in kg): "))

if planet == "sun":  
    weightonsun = weight * 27.9
    print(f"You must be hot, thats why you are heading to the Sun! On the Sun, your weight would be {weightonsun:} kg!!")

elif planet == "mercury":  
    weightonmercury = weight * 0.38
    print(f"Running from problems? Mercury is the fastest planet! On Mercury, your weight would be {weightonmercury:} kg!!")

elif planet == "venus":  
    weightonvenus = weight * 0.91
    print(f"Careful stepping on Venus, its hotter than your exs temper! Your weight there would be {weightonvenus:} kg!!")

elif planet == "earth":  
    print(f"Chill out blud... you are already on planet Earth unless you are an alien using my code!!")

elif planet == "moon":  
    weightonmoon = weight * 0.165
    print(f"The Moon is basically a cosmic trampoline! Bounce all day, cause your weight drops to just {weightonmoon:} kg!!")

elif planet == "mars":  
    weightonmars = weight * 0.376
    print(f"Mars is like a dusty playground, red sand everywhere! Your weight there shrinks to {weightonmars:} kg!!")

elif planet == "jupiter":  
    weightonjupiter = weight * 2.34
    print(f"Biggest boss in the Solar System, Jupiter will not let you move! Your weight there would be {weightonjupiter:} kg!!")

elif planet == "saturn":  
    weightonsaturn = weight * 1.06
    print(f"Thinking of proposing? Saturn is already flexing rings all around! Your weight there would be {weightonsaturn:} kg!!")

elif planet == "uranus":  
    weightonuranus = weight * 0.92
    print(f"Uranus spins sideways like it partied too hard last night! On Uranus, you would weigh {weightonuranus:} kg!!")

elif planet == "neptune":  
    weightonneptune = weight * 1.19
    print(f"Got anger issues? Neptunes might cool you down! Your weight there would be {weightonneptune:} kg!!")

elif planet == "pluto":  
    weightonpluto = weight * 0.06
    print(f"Feeling ghosted by Earth? Pluto knows the pain of being left out... Your weight there would be just {weightonpluto:} kg!!")

else:
    print("Blud... this aint even in our Solar System!! Stop making up planets!!")

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
