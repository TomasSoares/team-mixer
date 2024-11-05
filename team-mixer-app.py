import random
import tkinter as tk
from tkinter import messagebox

# Function to add players to the list
def add_player():
    player = entry_player.get()
    if player:
        players.append(player)
        listbox_players.insert(tk.END, player)
        entry_player.delete(0, tk.END)
    if len(players) == total_players:
        btn_add_player.config(state=tk.DISABLED)
        messagebox.showinfo("Team Mixer", "10 is the maximum number of players. Ready to form teams!")

# Function to form teams and display the result
def form_teams():
    if len(players) < total_players:
        messagebox.showwarning("Team Mixer", "Add all players to form the teams.")
        return
    random.shuffle(players)
    team1, team2 = players[:5], players[5:]
    
    # Clear previous display
    text_team1.config(state=tk.NORMAL)
    text_team1.delete("1.0", tk.END)
    text_team2.config(state=tk.NORMAL)
    text_team2.delete("1.0", tk.END)
    
    # Display teams in separate text boxes
    for player in team1:
        text_team1.insert(tk.END, f"{player}\n")
    for player in team2:
        text_team2.insert(tk.END, f"{player}\n")
    
    # Disable editing
    text_team1.config(state=tk.DISABLED)
    text_team2.config(state=tk.DISABLED)

# Initial variables and parameters
total_players = 10
players = []

# Main window creation
root = tk.Tk()
root.title("Team Mixer")
root.geometry("450x600")  # Increased window size
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Team Mixer", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Input frame
frame_entry = tk.Frame(root, bg="#f0f0f0")
frame_entry.pack(pady=10)

label_instruction = tk.Label(frame_entry, text="Enter a player's name:", bg="#f0f0f0", fg="#555")
label_instruction.pack(side=tk.LEFT, padx=5)

entry_player = tk.Entry(frame_entry, width=20)
entry_player.pack(side=tk.LEFT, padx=5)

btn_add_player = tk.Button(frame_entry, text="Add Player", command=add_player, bg="#4CAF50", fg="white")
btn_add_player.pack(side=tk.LEFT, padx=5)

# List of added players
listbox_frame = tk.Frame(root, bg="#f0f0f0")
listbox_frame.pack(pady=10)

listbox_label = tk.Label(listbox_frame, text="Players List:", bg="#f0f0f0", fg="#333")
listbox_label.pack()

listbox_players = tk.Listbox(listbox_frame, width=30, height=10, font=("Courier New", 10), relief="sunken", borderwidth=2)
listbox_players.pack(pady=5)

# Button to form teams
btn_form_teams = tk.Button(root, text="Form Teams", command=form_teams, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
btn_form_teams.pack(pady=10)

# Frame for displaying teams
teams_frame = tk.Frame(root, bg="#f0f0f0")
teams_frame.pack(pady=10)

# Team 1 display
team1_label = tk.Label(teams_frame, text="Team 1", bg="#f0f0f0", fg="#333", font=("Helvetica", 12, "bold"))
team1_label.grid(row=0, column=0, padx=10)

text_team1 = tk.Text(teams_frame, width=20, height=10, font=("Courier New", 10), relief="groove", borderwidth=2, state=tk.DISABLED)
text_team1.grid(row=1, column=0, padx=10)

# Team 2 display
team2_label = tk.Label(teams_frame, text="Team 2", bg="#f0f0f0", fg="#333", font=("Helvetica", 12, "bold"))
team2_label.grid(row=0, column=1, padx=10)

text_team2 = tk.Text(teams_frame, width=20, height=10, font=("Courier New", 10), relief="groove", borderwidth=2, state=tk.DISABLED)
text_team2.grid(row=1, column=1, padx=10)

# Start the graphical interface loop
root.mainloop()
