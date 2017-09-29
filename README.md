# Nimmtsix_simulations
The simulation of "6 Nimmt" game. We want to find the best strategy based on lots of simulations.

# Requirements:
- Python 3
- random
- [bisect](https://docs.python.org/2/library/bisect.html)

# Run the Program:
- Run the program with 4 players with below command
```bash
python Game -n 4
```

# Edit the strategy:
- In `Player.py` you can edit the strategy of playing game for computers. Default is `random.randint`.
- In `Player_user.py` you can edit the strategy of playing game for yourself (`p01`). Default is inserting by your hands.

# Future:
- Make main function `Game.py` prettier with self-defined user name.
- find good strategy for players.
- implement reinforcement learning.
