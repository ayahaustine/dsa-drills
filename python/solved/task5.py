"""
Using deep Q-learning to solve a Game
With graphical presentation of the training process
"""

import numpy as np
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential


class DeepQNetwork:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep Q-Learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        # Use 'learning_rate' instead of 'lr'
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))  
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state, invalid_moves):
        if np.random.rand() <= self.epsilon:
            valid_moves = np.where(invalid_moves == 0)[0]
            return np.random.choice(valid_moves)
        act_values = self.model.predict(state)
        # Mask invalid moves by setting their Q values to a large negative number
        act_values[0, invalid_moves == 1] = -np.inf
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def train(self, game, episodes, batch_size):
        scores = []
        for e in range(episodes):
            state = game.get_board().reshape(1, -1)
            for time in range(500):  # replace 500 with some suitable max timestep
                action = self.act(state, game.invalid_moves())
                next_state, reward, done = self._take_action(game, action)
                
                self.remember(state, action, reward, next_state, done)
                state = next_state
                if done:
                    scores.append(reward)
                    print(f"episode: {e+1}/{episodes}, score: {reward}, e: {self.epsilon:.2}")
                    break
                if len(self.memory) > batch_size:
                    self.replay(batch_size)
                    
            if (e + 1) % 10 == 0:
                self.plot_scores(scores)
        
        return scores
    
    def _take_action(self, game, action):
        game.make_move(action)
        next_state = game.get_board().reshape(1, -1)
        reward = game.get_score()
        done = (reward != 0)
        return next_state, reward, done

    def plot_scores(self, scores):
        plt.plot(scores)
        plt.ylabel('Score')
        plt.xlabel('Episode')
        plt.show()


# Example implementation of a simple game class (replace with your actual game)
class Game:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        self.game_over = False

    def get_board(self):
        return self.board

    def invalid_moves(self):
        return np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

    def make_move(self, action):
        row, col = divmod(action, 3)
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            self.current_player = -self.current_player

    def get_score(self):
        # Example score (replace with actual game logic)
        if np.all(self.board != 0):
            return 1
        return 0

G = Game()
G_board = G.get_board()
state_size = G_board.flatten().shape[0]
action_size = 9

dqn_agent = DeepQNetwork(state_size, action_size)
scores = dqn_agent.train(G, 100, 32)  # Example values for episodes, batch_size

class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate=0.001, gamma=0.99, epsilon=1.0, epsilon_decay=0.995, min_epsilon=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma  # future reward discount
        self.epsilon = epsilon  # exploration rate
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.memory = []  # memory for experience replay
        self.model = self._build_model()
        self.rewards = []  # to log rewards for plotting

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))  # output layer gives Q-values for each action
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)  # Explore
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])  # Exploit

    def replay(self, batch_size):
        batch = random.sample(self.memory, min(len(self.memory), batch_size))
        for state, action, reward, next_state, done in batch:
            target = reward
            if not done:
                target += self.gamma * np.amax(self.model.predict(next_state)[0])  # future reward
            target_f = self.model.predict(state)
            target_f[0][action] = target  # update target for the action taken
            self.model.fit(state, target_f, epochs=1, verbose=0)

        if self.epsilon > self.min_epsilon:
            self.epsilon *= self.epsilon_decay  # decaying epsilon

    def log_training(self, score):
        self.rewards.append(score)

    def plot_rewards(self):
        plt.plot(self.rewards)
        plt.xlabel('Episode')
        plt.ylabel('Reward')
        plt.title('Training Progress')
        plt.show()


def train_agent(G, episodes=1000, batch_size=32):
    action_size = 10  # Number of actions as per the problem statement
    state_size = G.get_board().size  # Size of the board, can be adjusted based on the shape of board