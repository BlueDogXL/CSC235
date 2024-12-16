# nomnomnami game-you-should-play-according-to-what-criteria-you-put-in-inator!! genius
import random
# list of criteria selected
selectedCriteria = []

replay = True

class NamiGame:
    def __init__(self, name, desc, link):
        self.name = name
        self.desc = desc
        self.link = link
    def printGame(self):
        print(f"{self.name}\n~~~~~~~~\n{self.desc}\n")
        explainThyself()
        print(f"\nGet it at: {self.link}")

# game objects
syrup = NamiGame("Syrup and the Ulitmate Sweet", "Syrup, the magic-hating Candy Alchemist of Atelier Sweets, finds a magical candy golem in her lab one day! Guide her through the misadventures that follow, and maybe help her grow as a person...?", "https://nomnomnami.itch.io/syrup-and-the-ultimate-sweet") # ID 0
treat = NamiGame("Lonely Wolf Treat: The Complete Series", "This ongoing saga of RPGMaker games follows Treat the wolf, Mochi the rabbit, and Moxie the fox as they become entangled in each others' lives. It's still a work-in-progress, but it's mostly finished aside from the last couple chapters.", "https://nomnomnami.itch.io/treat-complete") # ID 1
tears = NamiGame("her tears were my light", "Time awakens in a dark void, but soon finds the stars created by Space's tears... See what unfolds in this time-bending tale!", "https://nomnomnami.itch.io/her-tears-were-my-light \nor the deluxe Steam release at: https://store.steampowered.com/app/2112520/her_tears_were_my_light/") # ID 2
soiree = NamiGame("First Kiss at a Spooky Soir\u00E9e", "Marzipan and Jam go to a soir\u00E9e in the Netherworld with one goal \u0904 get Marz her first kiss! There are plenty of interesting characters to meet, so go out and get that smooch!", "https://nomnomnami.itch.io/first-kiss-at-a-spooky-soiree")# ID 3
contract = NamiGame("Contract Demon", "Eleni, an angel fascinated with all things occult, has made a contract with the demon Kamilla! ...to be her friend. See how their relationship develops, as Kamilla struggles between her relationship with Eleni and her job as a contract demon.", "https://nomnomnami.itch.io/contract-demon") # ID 4
starry = NamiGame("Starry Flowers", "Periwinkle, an elegant witch boy, goes out on a date with Pastille, shop assistant at Atelier Sweets and also a cute witch boy. Follow Periwinkle's journey as he falls head over heels for Pastille!", "https://nomnomnami.itch.io/starry-flowers") # ID 5
garden = NamiGame("Astra's Garden", "Astralagus has just opened her own apothecary far away from home. Grow plants in a relaxing idle game, and learn the stories of Astralagus and her customers.", "https://nomnomnami.itch.io/astras-garden") # ID 6
charm = NamiGame("Charm Studies", "Cassia, an airheaded witch-in=training, is failing charms class! She's gotten fellow witch Senna to tutor her, but can she really solve the picross puzzles and learn charms in time for finals? More importantly, will she become Senna's friend?", "https://nomnomnami.itch.io/charm-studies") # ID 7
date = NamiGame("DATE TREAT", "Released on April Fools, this game allows you to date Treat, Moxie, Trick, and Mochi from Lonely Wolf Treat! Well... maybe. It is April Fool's, after all...", "https://nomnomnami.itch.io/date-treat") # ID 8
poffin = NamiGame("Princess Poffin and the Spider Invasion", "Poffin, the light-loving princess of the Moth Kingdom, finds that there are spiderwebs all over her kingdom! At the behest of her parents, she arms herself with the kingdom's treasured stick and sets off to clear them out. Can she get to the bottom of the incident?","https://nomnomnami.itch.io/princess-poffin-and-the-spider-invasion") # ID 9
kaima = NamiGame("KAIMA", "The world of KAIMA is being consumed by Prince VIDO's monsters! It's up to SEARINA, an ever-cheerful demon, and ILLI, a rather gloomy one, to stop his nefarious plan before the world is completely consumed!", "https://nomnomnami.itch.io/kaima") # ID 10
drowning = NamiGame("drowning, drowning", "Maia is invited to visit an undersea kingdom! But was she invited just for fun, or for something deeper?", "https://nomnomnami.itch.io/drowning-drowning") # ID 11
bet = NamiGame("BAD END THEATER", "Welcome to the BAD END THEATER, a place where every ending's a tragedy! Will you stay strong against the branching paths of despair and find the TRUE END?", "https://badendtheater.com/") # ID 12

games = [syrup, treat, tears, soiree, contract, starry, garden, charm, date, poffin, kaima, drowning, bet]

def start():
    print("First off, would you just like to know where to begin playing in release order, pick a random game, or take the questionnaire to find a game you'd like?")
    choice = input("1. Start in release order!\n2. Just give me a random game!\n3. Questionnaire, please!\n")
    if choice == '1':
        selectedCriteria.append("to play games in release order.")
        releaseOrder() # there's only one right answer here
    if choice == '2':
        selectedCriteria.append("that we pick a game for you.")
        pickRandomGame()
    if choice == '3':
        amountOfGamingQuestion()

def releaseOrder():
    print(f"You should start with {syrup.name}!") # not doing printGame() because i want to explain it with the context of it being the first game
    explainThyself()
    print("It's the earliest game in the Nami-verse, and tells the story of, well, the candy alchemist Syrup and the legendary Ultimate Sweet. Among other things.")
    print("It introduces a good swathe of the residents of the witch town, and also introduces Treat the wolf, who stars in the immediate following game, Lonely Wolf Treat.")
    print("If you want to continue after Syrup in release order. you can find a list of Nami's games in release order (for the most part) on her website: https://nomnomnami.com/games/")
    print(f"You can get Syrup and the Ultimate Sweet at: {syrup.link}")

def pickRandomGame():
    print("Okay, random game it is! You should play...")
    games[random.randrange(0, games.__len__())].printGame()

def recommendGame(gameID):
    print("I've got it! You should play...")
    games[gameID].printGame()

def explainThyself():
    print("This game was picked because:")
    for i in selectedCriteria:
        print(f"\tYou prefer {i}")

def amountOfGamingQuestion():
    print("Do you prefer games that are more laid-back experiences or games that require a bit more active playing?")
    choice = input("1. Chill games!\n2. I want some gameplay in my games!\n")
    if choice == '1':
        selectedCriteria.append("laid-back games.")
        chillShortOrLongQuestion()
    if choice == '2':
        selectedCriteria.append("games that are more involved.")
        activeShortOrLongQuestion()

def chillShortOrLongQuestion():
    print("Would you rather play a short game or a long game?")
    choice = input("1. Short!\n2. Long!\n")
    if choice == '1':
        selectedCriteria.append("shorter games.")
        goofyOrSomberQuestion()
    if choice == '2':
        selectedCriteria.append("longer games.")
        complexityQuestion()

def complexityQuestion():
    print("How complex of a game do you want to play?")
    choice = input("1. Lots of endings that take a while to find!\n2. A handful of easier endings!\n3. Just one path!")
    if choice == '1':
        selectedCriteria.append("games with sprawling paths.")
        recommendGame(0)
    if choice == '2':
        selectedCriteria.append("games with a few paths.")
        recommendGame(3)
    if choice == '3':
        selectedCriteria.append("games with a linear path.")
        recommendGame(5)

def goofyOrSomberQuestion():
    print("Do you prefer a goofier tone or a more somber tone?")
    choice = input("1. Goofy!\n2. Somber.\n")
    if choice == '1':
        selectedCriteria.append("sillier games.")
        okButLikeHowGoofyQuestion()
    if choice == '2':
        selectedCriteria.append("somber games.")
        somberScopeQuestion()

def okButLikeHowGoofyQuestion():
    print("Alright, but like. Do you *mind* a little seriousness?")
    choice = input("1. I do mind! Only silliness!\n2. A little seriousness is okay!")
    if choice == '1':
        recommendGame(8)
    if choice == '2':
        selectedCriteria.append("games that also have a little seriousness.")
        recommendGame(4)

def somberScopeQuestion():
    print("Do you prefer games about grand things or just the little stuff in life?")
    choice = input("1. Grand stuff!\n2. The little things!\n")
    if choice == '1':
        selectedCriteria.append("games about grand topics.")
        recommendGame(2)
    if choice == '2':
        selectedCriteria.append("games about more personal topics.")
        recommendGame(6)

def activeShortOrLongQuestion():
    print("Would you rather play a short game or a long game?")
    choice = input("1. Short!\n2. Long!\n")
    if choice == '1':
        selectedCriteria.append("shorter games.")
        kindOfGamingQuestion()
    if choice == '2':
        selectedCriteria.append("longer games.")
        tragedromanceQuestion()

def kindOfGamingQuestion():
    print("Out of puzzles, battles, or stories, which do you like most in games?")
    choice = input("1. Puzzles!\n2.Battles!\n3. Story!\n")
    if choice == '1':
        selectedCriteria.append("puzzles.")
        recommendGame(7)
    if choice == '2':
        selectedCriteria.append("battles.")
        recommendGame(10)
    if choice == '3':
        selectedCriteria.append("stories.")

def tragedromanceQuestion():
    print("Do you prefer tragedy or romance?")
    choice = input("1. Tragedy!\n2. Romance!\n")
    if choice == '1':
        selectedCriteria.append("games about tragedy.")
        recommendGame(12)
    if choice == '2':
        selectedCriteria.append("games about romance.")
        recommendGame(1)

def sillyOrHeartfeltQuestion():
    print("Do you want to play a silly game or a serious game?")
    choice = input("1. Silly!\n2. Serious.\n")
    if choice == '1':
        selectedCriteria.append("silly games.")
        recommendGame()
    if choice == '2':
        selectedCriteria.append("serious games.")
        recommendGame()



def main():
    global replay
    while replay == True:
        global selectedCriteria 
        selectedCriteria = [] # clears the criteria list so it doesn't get weird on replays 
        print("Welcome to the NomNomNami Game Recommender\u2122!")
        start()
        print("Would you like to restart the program?")
        choice = input("1. Yes!\n2. No.\n")
        if choice == '1':
            replay = True
        else:
            replay = False

if __name__ == "__main__":
    main()