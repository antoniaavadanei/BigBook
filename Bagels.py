from random import randint

def generateRandomNo():
    number = randint(100, 999)
    return str(number)

def makeGuess(n:str):
    for i in range(11):
        guess=input("Your guess:")
        message = []
        for i in range(len(guess)):
            if guess == n:
                message.append('Congrats!')
                break
            if guess[i]==n[i]:
                message.append('Fermi')
            elif guess[i] in n:
                message.append('Pico')
        if len(message)==0:
            print('Bagels')
        print(message)
        if 'Congrats!' in message:
            break
print('The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.')
n = generateRandomNo()
print(n)
makeGuess(n)