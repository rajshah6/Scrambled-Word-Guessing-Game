def scrambler(s):
    import random
    length = len(s)
    while length > 0:
        random_index = random.randrange(0, length)
        s = s[:random_index] + s[random_index+1:] + s[random_index]
        length -= 1
    return s

while True:
    def words():
        import random
        list = "storm", "left", "tidy", "obese", "lump", "pound", "touch", "mask", "block", "aid", "hand", "major", "clerk", "watch", "flu", "bag", "cool", "aware", "oral", "lamp", "fault", "huge", "sweat", "tooth", "quote", "lily", "road", "he", "pilot", "gift", "hover", "blade", "orgy", "elbow", "toll", "stand", "wage", "shift", "set", "dump", "shoot", "wagon", "deer", "fairy", "rate", "wait", "strap", "ego", "save", "grass"
        return random.choice(list)

    s = words()
    scrambled = scrambler(s)
    while s == scrambled:
        scrambled = scrambler(s)
    guess = 0
    print(scrambled)

    while scrambled != s:
        position1, position2 = eval(input("Enter two index to swap (index1, index2): "))
        while position1 < 0 or position2 < 0 or position1 >= len(scrambled) or position2 >= len(scrambled) or position1 >= position2:
            position1, position2 = eval(input("Invalid input. Enter index in range and ensure index1 < index2: "))
        scrambled = scrambled[:position1] + scrambled[position2] + scrambled[position1 + 1:position2] + scrambled[position1] + scrambled[position2 + 1:]
        guess += 1
        print(scrambled, "\n")

        if guess == 4:
            hint = input("Would you like a hint? (y/n): ")
            if hint == "y":
                print("The first letter of the word is:", s[0], "\n")

        if guess == 8:
            hint = input("Would you like a hint? (y/n): ")
            if hint == "y":
                print("The first 2 letters of the word are:", s[0] + s[1], "\n")

    print("Congrats! The word was '", s, "'. It took you ", guess, " guesses.\n", sep = "")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break