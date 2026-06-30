import flappy_bird_gymnasium
import gymnasium as gym
from dqn import DQN
from experence_replay import ReplayMemory
import itertools
import yaml
import torch.nn as nn
import torch.optim as optim

if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


class Agent:

    def __init__(self, params_set):
        with open("parameters.yaml", "r") as f:
            all_param_set = yaml.safe_load(f)
            params = all_param_set[params_set]

        self.alpha = params["alpha"]
        self.gamma = params["gamma"]

        self.epsilon_init = params["epsilon_init"]
        self.epsilon_min = params["epsilon_min"]
        self.epsilon_decay = params["epsilon_decay"]

        self.replay_memory_size = params["replay_memory_size"]
        self.mini_batch_size = params["mini_batch_size"]

        self.reward_threshold = params["reward_threshold"]
        self.network_sync_rate = params["network_sync_rate"]

        self.loss_fn= nn.MSELoss()
        self.optimizer = None

    def run(self, is_training=True, render = False): 

    
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None, use_lidar=True)

        num_states = env.observation_space.shape[0]  # input dim
        num_actions = env.action_space.n             # output dim

        policy_dqn = DQN(num_states, num_actions).to(device)



        if is_training:
            memory = ReplayMemory(self.replay_memory_size)
            epsilon = self.epsilon_init 

            target_dqn = DQN(num_states, num_actions).to(device)
            target_dqn.load_state_dict(policy_dqn.state_dict())

            steps = 0

            self.optimizer = optim.Adam(nn)

        for episode in itertools.count(policy_dqn.parameters(), lr= self.alpha):

            state, _ = env.reset()

            state = torch.tensor(state, dtype=torch.float, device= device)

            episode_rewards = 0

            while not terminated:

                if is_training and random.random() < epsilon:
                    action = env.action_space.sample()
                    action = torch.tensor(action, dtype=torch.long, device= device)
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(dim=0)).squeeze().argmax()

                # Processing:  We will use terminated as done variable
                next_state, reward, terminated, _, _ = env.step(action.item())

                reward = torch.tensor(reward, dtype=torch.float, device= device)
                next_state = torch.tensor(next_state, dtype=torch.float, device= device)

                if is_training:
                    memory.append((state, action, new_state, reward,  terminated))
                    steps += 1


                    state = new_state
                    episode_rewards += rewards

            print(f" for episode = {episode +1} with total reward = {episode_rewards} and epsilon = {epsilon}")
            if is_training:
                #epsilon decay
                epsilon = max(epsilon * self.epsilon_decay, self.epsilon_min)

            if is_training and len(memory) > self.mini_batch_size:
                # get samples
                mini_batch = memory.sample(self.mini_batch_size)

                optimize(mini_batch, policy_dqn, target_dqn)

                #sync the network
                if steps > self.network_sync_rate:
                    target_dqn.load_state_dict(policy_dqn.state_dict())
                    steps = 0

        # env.close() - we will stop manually