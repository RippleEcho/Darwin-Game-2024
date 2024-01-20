# Darwin Game 2024

Cooperate or Defect

Modified Iterated Prisoner's Dilemma Game (**MIPD**)

  
Simple bots compete over limited resources, balancing competition and cooperation to survive and thrive   
  
The tournament will place all bots into a free-for-all contest to determine which comes out on top It's a modified version of a modified version of the iterated prisoner's dilemma  
  
  
MIPD basics:  
  
A Match is a 1-on-1 MIPD game between two bots, randomly chosen from the available pool.  
  
A Match consists of an indeterminate number of Turns (minimum 64).  
  
A Turn consists of a single input from each bot in the match.   
  
Each Turn, each bot is given the Match history, then chooses to Cooperate or Defect  
  
Match scoring is based on shares of a shared point resource.   
  
To Cooperate means adding 1 point to the shared resource (this costs nothing)  
  
If both bots Cooperate, an additional point (for a total of 3) is added to the shared resource  
  
To Defect means claiming 1 share of the shared resource (this costs 1 point)  
  
At the end of a Match, the shared point resource is divided between the bots, in proportion to the number of shares that bot has claimed in this Match.  
  
Each bot begins each Match with a single share of the shared resource.  
  
A Round of the MIPD game consists of every bot in the available pool playing a Match against a randomly selected bot from that pool.   
  
At the beginning of this game, the bot pool is filled with 256 copies of each bot. Random Match assignment means a bot will play against copies of itself, as well as other bots.   
  
Each Round, points will be summed across all copies of a bot. That point total determines the next step:  
  
Each Round after the first, the bot pool is adjusted to be proportional to the total score from the previous Round.   
  
Bots that accumulate more points will then have more copies next Round.  
  
The winner of the MIPD game is the bot with the largest number of copies after 256 Rounds   
  
Bots that finish with more than half of the number of copies of the winner are "Survivors"  
  
  
**HOW TO SUBMIT A BOT **   
All I need is a python file with a function with correct inputs and outputs.  
  
Inputs: Two lists (own\_moves, opp\_moves)   
Format of lists: either 0 or 1 where 0 is Cooperate, 1 is Defect  
  
Output: either 0 or 1 where 0 is Cooperate, 1 is Defect  
  
**SUBMISSION REQUIREMENTS**   
A bot must be contained in a single function. Lambdas are fine, but no defined functions  
  
A bot must have a reasonable execution time. If I think your bot is dragging things down, I'll ask you to modify.  
  
A bot is not permitted access to any information not contained within the input data. This means no access to Tournament code, or web access. Any attempts to circumvent will result in disqualification.   
  
See example bots for more clarity   
Send me your code over discord in either .txt or .py files   
Send this to me over discord preferably.  
  
If you need help putting your bot together, ask around or let me know!   
