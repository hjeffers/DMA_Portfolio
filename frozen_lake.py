#load the framework
import gym
import gym.spaces
import random
#load the environment
env = gym.make('FrozenLake-v0')

# observation space info -- shows how big the playing/observation space is (16 units)
print(env.observation_space)

# action space info -- shows how many actions you can take (4 -- 0:left, 1:down, 2:right, 3:up)
print(env.action_space)

# declare score
score = 0

# a bunch of episodes
for _ in range(10000):
    env.reset()  # reset the env to starting state
    # take 10 steps in each episode
    for t in range(100):
        action = random.randrange(1, 3)  # chooses a random sample action from the 4 we have
        observation, reward, done, info = env.step(action)  # take an action
        env.render()  # displays the environment
        if done:
            score += reward
            break
print(score)