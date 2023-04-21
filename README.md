# Gymnasium Rendering for Colaboratory

[![PyPI download month](https://img.shields.io/pypi/dm/renderlab.svg)](https://pypi.python.org/pypi/renderlab/)
[![PyPI - Status](https://img.shields.io/pypi/status/renderlab)](https://pypi.python.org/pypi/renderlab/)
[![PyPI](https://img.shields.io/pypi/v/renderlab)](https://pypi.python.org/pypi/renderlab/)
![GitHub](https://img.shields.io/github/license/ryanrudes/renderlab)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ryanrudes/renderlab/blob/main/examples/demo.ipynb)

*For the archived repository for use alongside OpenAI Gym, see [colabgymrender](https://github.com/ryanrudes/colabgymrender)*
## Installation
```bash
pip install renderlab
```

## Example
```python
import gymnasium as gym
import renderlab as rl

env = gym.make("CartPole-v1", render_mode = "rgb_array")
env = rl.RenderFrame(env, "./output")

observation, info = env.reset()

while True:
  action = env.action_space.sample()
  observation, reward, terminated, truncated, info = env.step(action)
  
  if terminated or truncated:
    break

env.play()
```
