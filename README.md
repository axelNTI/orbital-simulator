# Oribtal Simulator

## Requirements

The following needs to be installed:
- [Python](https://www.python.org/downloads/)

Run the following to install the necessary dependencies:

```pip install -r requirements.txt```

## Configuration

The initial configuration of the celestial bodies can be edited in the `data.json` file.

## Arguments

`-f` or `--file` is used if you want to use other json files than the standard one. Useful if you're frequently switching between different datas.

`-c` or `--concurrent` is used if you want to calculate the movement of the celestial bodies concurrently. Useful if a lot of celestial bodies are used.

`-l` or `--labels` is used to show the name of the planets on the visualization.

`-dv` or `--disable-visualization` is used to disable to pygame rendering of the simulation.

`-dg` or `--disable-graph` is used to disable the velocity plottign of the simulation.

---
> Developed by Felix Svensson and Axel Thornberg