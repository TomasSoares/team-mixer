import random
import os

input("Welcome to the Team Mixer. Press Enter to continue.")

team1 = []
team2 = []
total_players = 10
players = []

while len(players) < total_players:
    player = input("Please enter the name of a player: ")
    players.append(player)

for i in range(total_players):
    print(players[i])

random.shuffle(players)

team1 = players[:5]
team2 = players[5:]

if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Mac and Linux
    os.system('clear')

print("*****************************")
print("    Team 1:   |   Team 2:")
print("*****************************")

for i in range(len(team1)):
    print("| " + team1[i].ljust(12) + "| " + team2[i].ljust(12) + "|")

print("*****************************")
input("\nPress Enter to exit.")

