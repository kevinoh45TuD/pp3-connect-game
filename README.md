# Connect 4

## Introduction

This project was created using the language 'Python'. It is based on the real life game of the same name 'Connect 4'.

It has been deployed on Heroku using Code Institute's template to allow users to play it within their browser.

![Start Screen](/docs-pictures/pp3-title.png)

[Link to Game](https://pp3-connect-four-b560fdff375f.herokuapp.com)

Below I will outline key aspects of the project and its creation.

## Table of Contents

## UX

### User Stories

Here I have outlined some user stories of things the user might want from using this program.
Below each I will mention how I attempted to implement this in the program.

- As a user, I want to learn about Connect 4 before playing.
  >The start menu has an option for users to see critical information about Connect 4 goal/loop

- As a user, I want more variation in the computer opponent.
  >The user will be able to choose between 'Easy' and 'Hard' difficulties for the computer.

- As a user, I want to play Connect 4.
  >After selecting a difficulty users will be instantly presented with the game.

- As a user, I want clear instructions throughtout the program.
  >The program uses a lot of validation steps to make sure wrong inputs are not accepted, 
  while informative messages will be printed to guide the user to the correct input.

- As a user, I want to quickly start a new match when I win/lose.
  >Once a successful connection is made the game will print a message informing the user of the winner,
  additionally they will have an option to restart/quit at this point.

- As a user, I want to quit the game/program at my own discretion.
  >At all times during the game and end screen the user will be able to exit to the start screen,
  here they will have the option to exit the program.

### Color / Design

Below I will outline some color / design choices relating specifically to the game section.

![Game Screen](/docs-pictures/pp3-gamescreen.png)

The main game board features 7 columns and 7 rows. This emulates the layout of a physical Connect 4 board.

The table is double-lined to make it stand out with tokens being represented by '#' to try closely emulate
a token shape from the original game.

Previously each token as a larger shape of 2x2 and 3x3 '#' symbols, this was changed as it made the board to big 
for the specified heroku template screen.

The color for the table is blue. The color for player tokens is red. The color for computer tokens is yellow.
This is once again to emulate the color scheme users are familiar with for the actual connect 4 game.

The row at the top featuring the numbers 1-7 was added to inform users their available options, 
if a column becomes filled completely the number above will become an 'X'.

Directly below the board any messages informing users of issues with their input will be shown.
This text will be in red to make it distinct from the text below it.

Directly below this will be the standard message asking the user to input 1-7 or Q to quit.
This text will be yellow as to fit with a red/yellow color scheme.

The color and design for this program is very minimal. This is to remain clear and understandable for users.

The table and colored text is possible due to the rich package used in this project.

### Flow-Charts

## Features

### Start Screen

The Start Screen is what the user will first see. It features the title of the game 'Connect 4' along with 3 options.

![Start Screen](/docs-pictures/pp3-startscreen.png)

### Game Info

If the user picks option 2 on the start screen they will be shown this info screen. It provides basic information about the goal of Connect 4.
They will have the option to select any of the 3 options once more.

![Game Info](/docs-pictures/pp3-gameinfo.png)

### Game

If the user picks option 1 a new game will start. The user will be show an empty connect board with the available options 1-7 above.
Selecting an option will drop a red token into this column, the computer will take a turn dropping a yellow token.

![Game Screen](/docs-pictures/pp3-gamescreen.png)

### End Game

Once a successful connection has been made the user will be brought to this end screen.
Selecting restart will start a fresh game, whereas quit will bring the user back to the start screen.

![Game Over Screen](/docs-pictures/pp3-gameover.png)

### Future Features

With a project like this many more features code be added, however the two main features I would focus on would be:
1. Game History: Some system to record previous matches the user has won or lost.
2. Player 2: It would be possible to allow the user to choose to play locally with a second player on the 1 computer, replacing the computer opponent.
    
## Testing

There were two main areas they required extensive testing and bug fixing for the duration of this project.

### Player Inputs

The player will be required to make inputs throughout the program. Previous testing identified different issues with this input, the main fix being extra
validation of inputs. All the inputs required by the player follow two similarities: Specified Inputs given, Single Character inputs expected.
All inputs the player will enter consist of: "Q", "1", "2", "3", "4", "5", "6" and "7".
The manual testing for each of these inputs and their associated validation will be outlined in a table below.

### Brain Class Functions

The Brain class featured two main functions requiring testing / fixing, gather_results() and check_results().

Once either the player or computer took their turn a function (gather_results) would be run to find neighbouring tiles for Vertical, Horizontal and both Diagonals.
These four lists would be passed to a different function (check_results) which would loop through the lists in order till it found a valid connection.
If a connection was found it would print a message specifying the orientation and whether player or computer had won, also providing the user with the options
of restarting or quiting.
If no connection was made it would pass the turn to the other player.
	
Both functions had various bugs and fixes, which will be outlined below.

### Manual Testing Table

Any outcome wrapped in "" indicates the result is program asking for the same input again,
with this additional informative message to guide the user.

| Feature Tested | User Input | Outcome   |
| -------------- | ---------- | --------- |
| 1. Start Menu  |          1 | Start Game|
| | 2 | Show Info |
| | 3 | Exit Program |
| | Anything else | "Please pick an available option! 1, 2 or 3 are valid inputs!" |
| 2. Difficulty | 1 or 2 | Game will start with selected difficulty |
| | Anything else | "Please pick either 1 or 2" |
| 3. Game | 1 - 7 | Drop a token in corresponding column |
| | Q/q | Return to the start screen |
| | Any number not 1-7 or any filled column number | "Please pick a column with available space! Available options [1-7]" |
| | Anything else | "Please keep your input to 1 character! Your choice must be a number or Q to quit!" |
| 4. Restart/Quit | 1 | Restart Game |
| | 2 | Return to the start screen |
| | Any other number | "Please pick 1 or 2!" |
| | Anything else | "Input must be one character and a number!" |

## Deployment

This project was created using Gitpod, with a template provided by Code Institute as a starting point.
- [Gitpod](https://www.gitpod.io)
- [Code Institute Template](https://github.com/Code-Institute-Org/p3-template)

Github was used for documentation and version control.
- [Github](https://github.com)

The finished product was deployed on Heroku to allow users to play it on their browser.
- [Heroku](https://www.heroku.com)

### Setting Up Repository

I took these steps to setup my Github repository:
- Open the link to the Code Institute template mentioned above.
- At the top right corner click the button 'Use this template'.
- Click first option 'Create a new repository.
- Give the repository a relevant name and description.
- Make sure the repository remains public.
- At the bottom right click 'Create repository'.
- Once the repository is created click 'Code' at the top and you will find the link for your repository, copy this.

### Setting Up Gitpod Workspace

I took these steps to setup my Gitpod workspace:
- 
## Credits