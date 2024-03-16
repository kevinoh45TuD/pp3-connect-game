# Connect 4

## Introduction

This project was created using the language 'Python'. It is based on the real life game of the same name 'Connect 4'.

It has been deployed on Heroku using Code Institute's template to allow users to play it within their browser.

![Start Screen](/docs-pictures/pp3-title.png)

[Link to Game](https://pp3-connect-four-b560fdff375f.herokuapp.com)

Below I will outline key aspects of the project and its creation.

## Table of Contents

1. [UX](#ux)
    - User Stories
    - Color / Design
    - Flow-Chart
2. [Features](#features)
    - Start Screen
    - Game Info
    - Game
    - End Game
    - Future Features
3. [Technologies Used](#technologies-used)
    - Language
    - Code
    - Packages
    - Modules
    - Testing
    - Flow Chart
4. [Testing](#testing-1)
    - Player Inputs
    - Brain Class Functions
        - Testing gather_results()
    - Manual Testing Table
    - Linter Testing
    - Bugs
        - Previously Fixed
        - Known / Current
5. [Deployment](#deployment)
    - Setting Up Repository
    - Setting Up Gitpod Workspace
    - Deploying on Heroku
    - Clone Repository
    - Fork Repository
6. [Credits](#credits)
    - Code Institute
    - Other

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

Previously each token was a larger shape of 2x2 and 3x3 '#' symbols, this was changed as it made the board too big 
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

### Flow-Chart

The flow-chart below will show the main steps of the program.

![Game FlowChart](/docs-pictures/pp3-flowchart.png)

- Once the program starts the user will be presented with 3 options.
- They may exit the program at this point.
- If they select the game info option they will be provided with text related to 'Connect 4'
- They will still have access to the 3 options at this stage.
- Starting the game will load the board.
- The player will take the first turn.
- After which it will check for a win.
- If not a win it will pass to the computer to take a turn.
- This loop will repeat till one player wins (making a connection).
- Once a win occurs the player will have the option to Restart or Quit.
- Choosing Restart will load a new board.
- Choosing Quit will return the player to the start screen.

[Back to top](#connect-4)

## Features

### Start Screen

The Start Screen is what the user will first see. It features the title of the game 'Connect 4' along with 3 options.

![Start Screen](/docs-pictures/pp3-startscreen.png)

### Game Info

If the user picks option 2 on the start screen they will be shown this info screen. It provides basic information about the goal of Connect 4.
They will have the option to select any of the 3 options once more.

![Game Info](/docs-pictures/pp3-gameinfo.png)

### Game

If the user picks option 1 a new game will start. The user will be shown an empty connect board with the available options 1-7 above.
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

[Back to top](#connect-4)

## Technologies Used

### Language

- The primary language used to create this project was 'Python'.

- W3schools was used to reference the documentation for Python. [W3schools](https://www.w3schools.com)

### Code

- GitHub was used for version control of my repository. [Github](https://github.com)

- Gitpod was used as a cloud-based IDE. [Gitpod](https://www.gitpod.io)

### Packages

The only package used in this project was 'Rich'.

[Rich](https://pypi.org/project/rich/)

The purpose of using this package was the table function and coloring of text.
Both features allowing me to create a convincing 'Connect 4' board.

Along with the package itself being used, I used the documentation for rich quite extensively to make sure things worked the way I wanted.

[Rich Docs](https://rich.readthedocs.io/en/latest/introduction.html)

### Modules

#### sys

This module was used for "sys.exit(0)" to allow the application to exit on the start menu.
Based on [freeCodeCamp](https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/)

#### os

This module was used for "os.system('cls' if os.name == 'nt' else 'clear')" to clear the terminal screen.
Based on [Stack Overflow](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)

#### random

This module was used for "choice = random.choice(brain.available)" for the computer to select a random choice from the remaining options.
Based on [W3Schools](https://www.w3schools.com/python/ref_random_choice.asp)

### Testing

A Code Institute Python Linter was used to validate the code. The results will be provided below.

[Linter](https://pep8ci.herokuapp.com)

### Flowchart

I used a website called 'SmartDraw' to create the flowchart featured in this ReadME.

[SmartDraw](https://www.smartdraw.com/flowchart/)

[Back to top](#connect-4)

## Testing

There were two main areas that required extensive testing and bug fixing for the duration of this project.

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

#### Testing gather_results()

The gather_results() function in the brain class was tested / fixed a lot during development to make sure things were correct.

The method of testing was to hardcode values for the tiles list.

![Tile List](/docs-pictures/pp3-screenshot-tiles32.png)

With this set the gather_results() was called directly with specified x/y co-ordinates.
When testing I had additional print statements to print each of the four directions: Vertical, Horizontal, Diagonal 1, Diagonal 2

With the x/y input of (3,2) the console result:

![Output 3,2](/docs-pictures/pp3-screenshot-output32.png)

With the x/y input of (5,4) the console result:

![Output 5,4](/docs-pictures/pp3-screenshot-tiles54.png)

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

### Linter Testing

I used a Code Institute provided Python Linter to validate the code.
[Python Linter](https://pep8ci.herokuapp.com/#)

No errors are currently present with any of the files.

Some reoccuring issues that were fixed include:
- No space after '#' for comments.
- Lines being over 79 characters.
- Whitespace
- Extra lines between functions

Screenshots of Linter results:

- [run.py result](/docs-pictures/pp3-linter-run.png)
- [start.py result](/docs-pictures/pp3-linter-start.png)
- [screen.py result](/docs-pictures/pp3-linter-screen.png)
- [rival.py result](/docs-pictures/pp3-linter-rival.png)
- [player.py result](/docs-pictures/pp3-linter-player.png)
- [game.py result](/docs-pictures/pp3-linter-game.png)
- [brain.py result](/docs-pictures/pp3-linter-brain.png)
- [board.py result](/docs-pictures/pp3-linter-board.png)

### Bugs

#### Previously Fixed

- When check_results looped through the different lists if it counted to 4 or greater (a connection) but the following tile was not a match it would reset the count to 0.
  This was fixed by adding a bool that would set 'True' if the count reached 4 at any point and only reset count if this bool is false.

- Frequent bug relating to user inputing numbers '1-7' while lists starting at 0, simple fixed my -1 to user input when it relates to lists.

- My method for getting diagonals in gather_result used the initial tile position (where the player's token landed) while incrementing / decrementing 
  both directions for both diagonals, this bug entered the initial tile twice.
  This was fixed by starting the count at 1 for the second half of each diagonal to skip over the initial tile the second time.

- This fix produced an additional bug where starting the count at 1 and adding/subtracting this count to the X/Y position of the initial tile would potentially
  send the number out of the bounds of the list. 
  To fix this I added a check to see if adding/subtracting the count at 1 with the X/Y position would make it go out of bounds before any other code.

#### Known/Current

- Hard difficulty does not work as originally invisioned. This may be due to the approach working correctly, but being a bad approach. 
Alternatively the approach not working.
- When win message is printed after the first time the formating is missing and it appears on the far left.

[Back to top](#connect-4)

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
- Select the option for automatic deployment, when you push to your repo Heroku will build your app again.
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

[Back to top](#connect-4)

## Credits

- A special thanks to my mentor Matt Boden for his assistance throughtout the project! [MattBCoding](https://github.com/MattBCoding)

### Code Institute

- Code Institute template used for repository [Template](https://github.com/Code-Institute-Org/p3-template)

- Code Institute learning modules used to learn different aspects of Python [Code Institute](https://codeinstitute.net/ie/)

### Other

- An article on GitHub was used to help with creating this README doc [Article](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

- I went with an approach in my 'run.py' recommended by my mentor. This allowed my 'run.py' to remain tidy and leave my other files in a contained folder.
[Post related to method](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

- I found a method to clear my terminal from a Stack Overflow post. [Stack Overflow](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)

- I found another post on Stack Overflow that helped with unpacking a list for rich table rows. [Stack Overflow](https://stackoverflow.com/questions/65216850/list-of-lists-into-a-python-rich-table)

- A specific section of W3schools helped with random implementation. [W3Schools](https://www.w3schools.com/python/ref_random_choice.asp)

- A specific freeCodeCamp article helped with using the exit() function [freeCodeCamp](https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/)

[Back to top](#connect-4)