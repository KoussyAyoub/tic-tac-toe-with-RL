# Tic-Tac-Toe Agent Training Project

## Project Overview

This project aims to implement an AI agent capable of playing the game of tic-tac-toe. The agent's objective is to learn an optimal policy for making moves using the Markov decision process, Monte Carlo and Temporal Difference Learning methods. 

## Markov decision process (MDP)
A Markov Decision Process is a mathematical framework for modeling decision-making problems in the presence of uncertainty. In this project, we utilize an MDP to train an AI agent to play tic-tac-toe effectively. Here's a more detailed explanation of the key components and their roles:
1. **Agent.py**: Contains the implementation of the AI agent class. The agent uses a pre-trained policy to make decisions during the game. If a policy is not available for a particular game state, the agent makes a random move.

2. **Human.py**: Defines the human player class. It allows a human player to interact with the AI agent in a tic-tac-toe game, making moves manually.

3. **Env.py**: Represents the game environment. It keeps track of the game state, the current winner, and manages the game's logic, including checking for winning conditions and conducting the game.

4. **MDP.py**: Contains the Markov Decision Process (MDP) class, which handles the training of the AI agent. It implements value iteration to learn the optimal policy and reward structure for the game.

### Project Objective

The main objective of this project is to train an AI agent to play tic-tac-toe effectively against a human player. The agent's training is done through the use of the value iteration algorithm within an MDP framework. The project consists of two major parts:

1. **Training the Agent**: The MDP class in MDP.py is responsible for training the AI agent. Value iteration is used to calculate the optimal policy and rewards for different game states. The agent aims to maximize its rewards by learning which moves are more likely to lead to a win or a favorable outcome.

2. **Gameplay Interaction**: The Agent.py and Human.py files allow the AI agent and a human player to interact in a tic-tac-toe game. The human player can input moves manually, while the AI agent uses the learned policy to make decisions.

### Getting Started

Follow these steps to set up and run the project:

1. Clone the repository to your local machine.

2. Ensure you have Python installed, along with the required dependencies.

3. Run the `Main` class in MDP.py to train the AI agent and save the learned policy and value function to files.

4. Run the `Main` class in Env.py to initiate a game between the AI agent and a human player. The agent uses the learned policy to make decisions.

### Files and Directory Structure

The project directory is structured as follows:

- `Agent.py`: Contains the AI agent class.
- `Human.py`: Defines the human player class.
- `Env.py`: Manages the game environment and logic.
- `MDP.py`: Handles the training of the AI agent using the MDP framework.
- `policy.txt`: Stores the learned policy in a readable format.
- `V.txt`: Stores the value function (V) in a readable format.
- `Main.py`: Provides a script to run the project.




