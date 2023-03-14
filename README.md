# RPG COMMod Game V2
These repository featuring an agent-based modeling that based this game made in Python.
This game is a simplification of an ARDI model created during the workshop that took place in January 2023, in Porto Alegre, RS, Brazil

# Folders
This repository contains these folders:
* Deprecated: Old versions/Inactive files/functions used in previous versions, not functional
* Development: Newer versions of the game, usually being tested in alpha/beta versions - used only by developers
* Game_run: Actual version of the game
* Images: Folder for storing images to be used in the front-end/app version of game (TBI)

## Requisites 
* Make sure you have [Python](https://www.python.org/downloads/) on your computer. 

## To Run
* Open the directory 'game_run/', this is where actual version of the game is located
* Run the python command: `python run_v2.py`
* The text RPG game will start.

## Game Mechanics:
  * The players will have to manage a pandemic scenario, and make the population survive for 12 rounds and keep public trust greater than 0
    * If you let all population die or Public Trust be 0 (on V3), you lost the game.

### Resources:
  * In the first round, players will choose a difficulty (EASY/NORMAL/HARD) that will define amount of resources per round.
  * "Greater difficulty, scarcer resources".
  * Each round, the Governor will receive an amount of resources proportional to population in the round.

### Players:
  * There are three players that you will name in the start:
    * Government - Gets Resources each round and distributes among other players and to primary care
    * Media - Uses resources to pay advertising and chooses to speak positively/negatively of Government responses, managing public opinion/adherence to isolation  
    * Hospital Manager - Uses resources given by governor to allocate to hospital beds and manage cases
      *  Prices:
         * Emergency Room Beds: 2$
         * Infirmary Beds: 2$
         * ICU Beds: 4$
      * Note: As you have to provide resources for these beds, these resources are non-renewable, i.e you must pay for the beds each round

### Public Trust/Isolation/Lockdown: (TBI)
  * Public Trust/Compliance: starts at 100%. It is a combination of Media speech (positive increases by 5% in the next round, and negative decreases 10% each round), and also by implantation of Lockdown, that reduces by 20% next round.
    * It is a multiplier for Social Isolation, i.e, lesser public trust/compliance, less adherence to social isolation
  * Social Isolation Level: [0-100%] is a multiplier to number of cases needing hospital aid, i.e each 10% social isolation, decreases 1% number of cases needing hospital aid.
  * Lockdown: When activated, decreases by 20% number of cases needing hospital admission in next round, however, also decreases in 20% public trust/compliance. 

### Pandemics Dynamics
  * It was initially choose that every round, a fraction (0-10%) of population will be affected by disease, and Primary care investiments will reduce the amount of cases needing hospital admission (each 10$ will reduce an amount of 2 cases)
  * Also, it was defined that a proportion of 4:2:2 cases distributed for ER,Infirmary and ICU, and that these units have a lethality of 10%,40% and 80%, respectively.
  * All cases needing Hospital admission that do not receive it, will count as a preventable/excess death
  * Deaths (preventable and expected) will be reduced from total population. If your population is 0, you lost the GAME!
 
 

