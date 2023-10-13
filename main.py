# je definer une fonction qui contient le jeu de devinette dans lequel le usager mets un nombre les bornes minimal et maximale, puis l'ordinateur choisi un nombre random et l'usgaer essaye de le devinir et l'ordinateur l'aide en le disant si c'est plus grand ou plus petit.


def jeu_de_devinettes():
  import random
  rejouer = "o"

  #Cet boucle while execute le jeux jusqu'a le usager veut plus jouer

  while rejouer == "o":
    borne_minimale = int(input("définisser les bornes, nombre minimal:"))
    borne_maximale = int(input("définisser les bornes, nombre maximal:"))
    n = random.randrange(borne_minimale, borne_maximale)
    essai = 0
    guess = None

    #L’ordinateur demande à l’usager d’entrer un nombre de façon à trouver celui que l'ordi a choisi.

    print(
        f"J'ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}"
    )
    print("À vous de le deviner...")

    while n != guess:
      guess = int(input("Entrer un nombre: "))
      essai += 1
      if guess > n:
        print("la reponse est plus petite que votre nombre!")

      elif guess < n:
        print("la reponse est plus grande que votre nombre!")

    print("C'est la bonne reponse, vous avez gagnez!!!\nCela vous a pris",
          essai, "essai(s).")

    rejouer = input("Voulez-vous faire une autre partie (o/n)? ").lower()

  print("Merci et au revoir...")


jeu_de_devinettes()
