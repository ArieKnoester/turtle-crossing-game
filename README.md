# turtle-crossing-game
Work in progress. This program is for a Python course. The course
prompts the student to choose a difficulty level as defined below.

- Difficulty Normal 😎: Use all Steps to complete the project.
- Difficulty Hard 🤔: Use only Steps 1 and 2 to complete the project.
- Difficulty Expert 🤯: Only use Step 1 to complete the project.

Starting code was provided by the course (See 'Initial commit'). 
I chose 'Expert' difficulty. Step 1 contains the requirements for 
the game and a few gifs showing examples of the requirements. 

### Game requirements:
1. A turtle moves forwards when you press the "Up" key. 
It can only move forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move 
from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves 
back to the original position and the player levels up. On the 
next level, the car speed increases.
4. When the turtle collides with a car, it's game over and 
everything stops.

#### TODO
- ~~Detect if the turtle collides with any car.~~
- ~~If the turtle collides with any car. The game is over.~~
- When the game is over, Display 'GAME OVER' text.
- (Maybe) Tweak the logic that determines whether a car is 
spawned or use a different algorithm.
- (Maybe) Tweak the speed increase when a player levels up.
