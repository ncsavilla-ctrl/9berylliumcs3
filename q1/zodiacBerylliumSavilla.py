
year=int(input("Enter your birth year: ")) #This line asks the user to input their birth year


if year < 1900: #This line validates the year
    print("Invalid Year, it should not be earlier than 1900")
else:
    #The next lines shows the given Chinese Zodiac signs starting from year 1900
    zodiac_signs=[
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
     "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
     "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
     "Rooster (鸡 / Jī)",
     "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]


zodiac_index=(year-1900)%12 #This line determines the zodiac sign
zodiac=zodiac_signs[zodiac_index]

print("Your Chinese Zodiac Sign is:", zodiac)


                