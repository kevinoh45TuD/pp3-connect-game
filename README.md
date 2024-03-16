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

![Game FlowChart](/docs-pictures/pp3-flowchart.png)

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

## Technologies Used

The primary language used to create this project was 'Python'.


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

### Bugs

#### Previously Fixed

- When check_results looped through the different lists if it counted to 4 or greater (a connection) but the following tile was not a match it would reset the count to 0.
  This was fixed by adding a bool that would set 'True' if the count reached 4 at any point and only reset count if this bool is false.

- Frequent bug relating to user inputing numbers '1-7' while lists starting at 0, simple fixed my -1 to user input when it relates to lists.

- My method for getting diagonals in gather_result used the initial tile position (where the player's token landed) while incrementing / decrementing 
  both directions for both diagonals, the bug produced entered the initial tile twice.
  This was fixed by starting the count at 1 for the second half of each diagonal to skip over the initial tile the second time.

- This fixed produced an additional bug where starting the count at 1 and adding/subtracting this count to the X/Y position of the initial tile would potentially
  send the number out of the bounds of the list. 
  To fix this I added a check to see if adding/subtracting the count at 1 with the X/Y position would make it go out of bounds before any other code.

#### Known/Current

- Hard difficulty does not work as originally invisioned. This may be due to the approach working correctly, but being a bad approach. 
Alternatively the approach not working.

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

It is recommended to sign into Gitpod with the Github account used in the above steps.
There are various methods to create a workspace with a specified repository, I will outline one these methods.

I took these steps to setup my Gitpod workspace:
- Sign into Gitpod with Github account.
- Navigate to 'Workspaces' section.
- At the top right of this section click 'New Workspace'.
- Here you can either paste the link copied from the final step of setting up the repository,
alternatively type in the name of the repository.
- I left the other two settings default.
- Click 'Continue'.
- Gitpod will now setup your workspace.

Once all changes are commited and pushed, at the top left of your screen you can click the burger icon to the left of 'EXPLORER' 
and click 'Gitpod: Stop Workspace' to return to the dashboard.

### Deploying on Heroku

These steps require having the 'requirements.txt' file up to date with anything the project needs.
Certain steps will be based on using the Code Institute Template.

- Sign into Heroku website.
- Navigate to your dashboard.
- At the top right click 'New'.
- Click 'Create new app'.
- The app will require a unique name, I used 'pp3-connect-four'.
- I selected 'Europe' for 'Choose a region'.
- Click 'Create app'.
- You will now be on the 'Deploy' tab for your new app.
- Select 'Settings' on the same row as 'Deploy'.
- Click 'Reveal Config Vars'.
- Set 'KEY' to 'PORT', set 'VALUE' to '8000'.
- Click 'Add' to the right of this.
- Scroll down and select 'Add buildpack'.
- Select the option for 'python', click 'Add Buildpack'
- Repeat this step with the 'nodejs' buildpack.
- Return to the 'Deploy' section.
- Next to 'Deployment method' select 'GitHub'.
- Sign into GitHub and connect account if required.
- Search for your repositories name.
- If you locate the correct one, click 'Connect'.
- Select the option for automatic deployment, when you push to your repo Heroku will build you app again.
- Click into 'Overview' section, here you can see recent activity and if the app is currently building.
- At the top right you will have the option to 'Open app'.

Your Heroku app should be correctly set up at this point.

Steps based on information gained from Code Institute course content.

### Clone Repository

Here I will outline the steps to clone a repository on GitHub.
This allows you to save a local copy.

Steps:
- Navigate to the GitHub page for the desired repository.
- Click on 'Code'
- Copy the link provided under HTTPS.
- Open Git Bash.
- Change the current working directory to the location where you want the cloned directory.
- Type 'git clone ' along with the copied link.
- Press Enter to create cloned repository.

Steps are based on GitHub documentation related to cloning repositories.

[GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui)

### Fork Repository

Here I will outline the steps to fork a repository on GitHub.
This allows you to have your own repository to make changes to based on an original repositories code/settings.
Additionally you may submit a pull request to the original repository owner.

Steps:
- Navigate to the GitHub page for the desired repository.
- At the top right, below the search box, click 'Fork'.
- Leaving all the settings will be fine, but here you may apply a new name or description.
- Click 'Create fork'.

Steps are based on GitHub documentation related to forking repositories.

[GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

## Credits