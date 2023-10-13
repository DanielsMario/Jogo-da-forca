import random

palavras = ["abelha","cobra","babuino"]

palavra = random.choice(palavras)

letras_certas = []
letras_erradas = []
tentativas = 6

boneco = ["  O", " /|\\", " / \\", " |", " /"," \\"]

print("!!Sejam Bem Vindos ao Jogo da FORCA!!")

while True:
    palavra_secreta = ""
    for letra in palavra:
        if letra in letras_certas:
           palavra_secreta += letra
        else:
            palavra_secreta += "_"

    print("\npalavra: " + palavra_secreta)
    print("Tentativas restantes: " + str(tentativas))

    for i in range (tentativas, 7):
        if i > 0:
            print(boneco[i - 1])

    if palavra_secreta == palavra:
        print(f"Parabéns!!! Você ganhou. A palavra era: {palavra}")
        break
    if tentativas == 0:
        print(f"Que pena!! Infelizmente você perdeu, a palavra era: {palavra}")
        break

    letra = input("Digite uma letra: ").lower()

    if letra in letras_certas or letra in letras_erradas:
        print("Você já utilizou essa letr. Tente outra letra novamente. ")
        continue

    if letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1