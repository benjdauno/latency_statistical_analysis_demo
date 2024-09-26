# Latency Data Simulation

This project simulates latency data using three common distributions: **log-normal**, **Weibull**, and **Pareto**. The simulation mimics the latency patterns of a typical application and allows users to vary parameters such as the total number of data points and the sampling percentage to observe how these factors affect latency measurements.

## Distributions Used

- **Log-normal Distribution**: Models data that is positively skewed, with a long tail on the right.
- **Weibull Distribution**: Often used to model time-to-failure data, with adjustable scale and shape parameters.
- **Pareto Distribution**: Models long-tailed distributions where a small fraction of requests experience high latency.

## Project Structure

- `latency_simulation.py`: The main Python script that runs the simulation and generates reports.
- `Makefile`: A file to help set up the environment and run the simulation.
- `requirements.txt`: Lists the required Python libraries.
- `results/`: A folder where output plots for each iteration will be stored.

## Setup

To set up and run the project, you'll need Python 3 installed on your machine. Follow these steps to clone and execute it.


```bash
git clone git@github.com:benjdauno/latency_statistical_analysis_demo.git
cd latency_statistical_analysis_demo
make setup
make run
```

Visualizations of the generated data points are stored in the results folder.

You can vary the parameters n (the total number of data points), and m (The percent of data points sampled) to see how this affects the accuracy of the p99 calculation.