import flappy_bird_gymnasium
import gymnasium as gym
from dqn import DQN
from experence_replay import ReplayMemory
import itertools

if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


def run(self, is_training=True, render = False): 
    env = gym.make("FlappyBird-v0", render_mode="human" if render else None, use_lidar=True)

    num_states = env.observation_space.shape[0]  # input dim
    num_actions = env.action_space.n             # output dim

    policy_dqn = DQN(num_states, num_actions).to(device)



    if is_training:
        memory = ReplayMemory(10000)

    for episode in itertools.count():

        state, _ = env.reset()
        episode_rewards = 0

        while not terminated:
            # Next action:
            # (feed the observation to your agent here)
            action = env.action_space.sample()

            # Processing:  We will use terminated as done variable
            next_state, reward, terminated, _, _ = env.step(action)

            if is_training:
                memory.append((state, action, new_state, reward,  terminated))


                state = new_state
                episode_rewards += rewards

        print(f" for episode = {episode +1} with total reward = {episode_rewards}")

        

    # env.close() - we will stop manually