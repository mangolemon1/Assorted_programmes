import random

opp_choices = ["Schere", "Stein", "Papier"]
opp = random.choice(opp_choices)

print("Schere - Stein - Papier")
print("-----------------------------------------------------")

player =  str(input(f"Wählen sie aus:\nA = Schere\nB = Stein\nC = Papier\nMeine Wahl - "))
player = player.lower()
if player == "a":
    player = "Schere"
    print("Spieler : " + str(player) + "\nBot : " + str(opp))
    if opp == "Schere":
        print("Unentschieden!")
    if opp == "Stein":
        print("Verloren!")
    if opp == "Papier":
        print("Gewonnen!")
if player == "b":
    player = "Stein"
    print("Spieler : " + str(player) + "\nBot : " + str(opp))
    if opp == "Schere":
        print("Gewonnen!")
    if opp == "Stein":
        print("Unentschieden!")
    if opp == "Papier":
        print("Verloren!")
if player == "c":
    player = "Papier"
    print("Spieler : " + str(player) + "\nBot : " + str(opp))
    if opp == "Schere":
        print("Verloren")
    if opp == "Stein":
        print("Gewonnen!")
    if opp == "Papier":
        print("Unentschieden!")


