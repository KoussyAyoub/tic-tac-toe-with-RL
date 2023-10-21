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

Tic-Tac-Toe Agent using Monte Carlo Methods
------------------------------------------------------

**Project Objective:**

The objective of this project is to train an agent to play the game of Tic-Tac-Toe using Monte Carlo methods. Monte Carlo methods are a class of reinforcement learning techniques that allow the agent to learn through trial and error. In this specific project, we have implemented three different Monte Carlo methods for training the agent:

1. **Monte Carlo Prediction (MCP)**: This method is used to estimate the value function for different states in the game. It helps the agent understand how good or bad a state is.

2. **On-Policy First-Visit Monte Carlo with Exploring Starts**: This method combines on-policy learning with exploration. It ensures that the agent explores different states by starting from random states, improving the learning process.

3. **On-Policy First-Visit Monte Carlo Control with Epsilon-Greedy Policy**: This method aims to find the optimal policy for the agent to maximize its rewards. It uses epsilon-greedy exploration, where the agent sometimes explores random actions.

**Project Components:**

The project consists of several Python files, each with specific responsibilities:

1. **Agent.py**:
   - Defines the `Agent` class responsible for the agent's behavior.
   - Reads a policy from an external file to make decisions.
   - Chooses actions based on the policy, with provisions for random exploration when no policy exists.

2. **Agent_epsilon_greedy.py**:
   - Similar to `Agent.py`, but with an added exploration strategy using epsilon-greedy. The agent explores random actions with a certain probability.
   
3. **Human.py**:
   - Defines the `Human` class for human players to participate in the game.
   - Allows human players to choose their moves and ensures the moves are valid.

4. **Env.py**:
   - Represents the game environment.
   - Keeps track of the game state, the current winner, and methods for checking the winner and calculating rewards.
   - Provides a method to play the game where human and agent take turns.

5. **MCP.py**:
   - Defines the `MCP` class, responsible for training the agent using the Monte Carlo methods.
   - Implements three specific methods: Monte Carlo Prediction, On-Policy First-Visit Monte Carlo with Exploring Starts, and On-Policy First-Visit Monte Carlo Control with Epsilon-Greedy Policy.
   - Each method is used to learn and improve the agent's behavior.

6. **Main.py**:
   - The main script that ties everything together.
   - Creates instances of the `MCP` class and trains the agent using the chosen Monte Carlo method.
   - Checks if the policy has changed during training and saves the learned policy to a file in a dictionary format.

**Using the Code:**

To use the code in this project, follow these steps:

1. Run the `Main.py` script to initiate the training of the agent using one of the Monte Carlo methods.
2. Ensure that the required classes (`Agent`, `Agent_epsilon_greedy`, `Human`, `Env`, and `MCP`) are correctly imported.
3. You may need to provide the path to an initial policy file to start the training.
4. The code will train the agent and save the learned policy to a file for future use.



## Tic-Tac-Toe using Temporal Difference Learning

### Project Overview

This project is a Python-based implementation of a Tic-Tac-Toe game where an agent learns to play using reinforcement learning techniques. The objective is to train the agent to make optimal moves and improve its performance over time.

### Project Components

The project consists of several Python classes that work together to achieve the learning objectives:

1. **Agent.py**: This class represents the agent, which learns to play Tic-Tac-Toe. It initializes with a policy and uses temporal difference learning methods to update its policy. The agent can choose actions based on its policy and explore or exploit its moves using epsilon-greedy exploration.

2. **Agent_epsilon_greedy.py**: Similar to the Agent class in Agent.py, but with an additional exploration-exploitation mechanism (epsilon-greedy) to balance the agent's actions between learning and exploiting its existing policy.

3. **Human.py**: This class represents a human player who can interact with the Tic-Tac-Toe game. The human player can choose positions to make moves on the game board.

4. **Env.py**: The Environment class, which simulates the Tic-Tac-Toe game. It keeps track of the game's status and handles the logic for checking a winner, printing the game board, and more.

5. **TDL.py**: The Temporal Difference Learning class, which focuses on training the agent using reinforcement learning techniques. It implements Sarsa and n-step Sarsa algorithms to update the agent's policy.

### How to Run

To run this project, follow these steps:

1. Clone the repository from GitHub to your local machine.

2. Make sure you have Python installed on your system.

3. Open a terminal and navigate to the project's directory.

4. Run the main script **TDL.py** to start the training process:

5. The agent will start learning to play Tic-Tac-Toe using the specified reinforcement learning method.

6. Once the training is complete, you can evaluate the agent's performance by running the game with a human player or other agents using **Env.py**.

### Project Output

The project's main output is the learned policy of the agent, which represents the optimal moves in different game states. This policy is saved to a file named `policy_TDL_Sarsa_n.txt`.

### Customization

You can customize various aspects of the project to fit your needs:

- Adjust the reinforcement learning parameters in `TDL.py` such as alpha (learning rate) and gamma (discount factor).
- Modify the exploration rate (epsilon) in `Agent.py` and `Agent_epsilon_greedy.py` to control the agent's exploration vs. exploitation balance.
- Adapt the reward function in `Env.py` to change the way the agent is rewarded based on the game's outcome.

## Contributing

If you want to contribute to this project, feel free to create a pull request with your changes or improvements. We welcome contributions to enhance the functionality or provide better documentation.








