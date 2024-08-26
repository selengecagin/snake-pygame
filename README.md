# Snake Game AI

## Overview

This project implements an AI agent that learns to play the classic Snake game using reinforcement learning techniques. The AI uses a Q-learning approach with a neural network (Deep Q-Network) to make decisions.

## How It Works
------------
1. Game Environment (game.py):
   - Creates the Snake game using Pygame.
   - Manages game state and provides rewards.

2. Agent (agent.py):
   - Implements the AI player using Q-learning.
   - Uses an epsilon-greedy strategy for exploration vs. exploitation.
   - Stores and learns from game experiences.


3. Neural Network (model.py):
   - A simple feedforward network that predicts Q-values for actions.
   - Trained to improve decision-making over time.


4. Training Process:
- Agent interacts with the game, collecting experiences.
- Experiences are used to train the neural network.
- Q-values are updated using the Bellman equation. This equation allows the agent to learn from its experiences, balancing immediate rewards with a long-term strategy
      ```
      Q_new = Q + α * (reward + γ * max(Q_next) - Q)
      ```
      - α (alpha) is the learning rate
      - γ (gamma) is the discount factor
      - reward is the immediate reward for taking the action
      - max(Q(next_state, all actions)) is the maximum predicted Q-value for the next stage
  
5. Visualization (helper.py):
   - Plots score in real-time to show learning progress.

## Usage
-----
To install the Snake Game AI, please follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install pygame torch matplotlib numpy
   ```
3. Run the `agent.py` file, execute the following command:
     ```
   python agent.py
   ```












