```markdown
# Team Mixer

Team Mixer is a Python application that allows users to input player names and randomly form two teams. The application provides both a command-line interface and a graphical user interface (GUI) using Tkinter.

## Features

- Add player names to a list.
- Randomly shuffle and divide players into two teams.
- Display the teams in a user-friendly format.
- GUI with Tkinter for easy interaction.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Usage

### Command-Line Interface

To use the command-line interface, run the `team-mixer.py` script:

```sh
python 

team-mixer.py


```

Follow the prompts to enter player names and view the randomly generated teams.

### Graphical User Interface

To use the graphical user interface, run the `team-mixer-app.py` script:

```sh
python 

team-mixer-app.py


```

A window will appear where you can enter player names, add them to the list, and form teams.

## Project Structure

- `team-mixer.py`: Command-line interface for the Team Mixer application.
- `team-mixer-app.py`: Graphical user interface for the Team Mixer application using Tkinter.

## Example

### Command-Line Interface

```sh
Welcome to the Team Mixer. Press Enter to continue.
Please enter the name of a player: Alice
Please enter the name of a player: Bob
...
*****************************
    Team 1:   |   Team 2:
*****************************
| Alice       | Bob         |
| Charlie     | Dave        |
...
*****************************
Press Enter to exit.
```

### Graphical User Interface

1. Enter player names in the input field.
2. Click "Add Player" to add the player to the list.
3. Once 10 players are added, click "Form Teams" to randomly divide the players into two teams and display them.

## License

This project is licensed under the MIT License.
```
