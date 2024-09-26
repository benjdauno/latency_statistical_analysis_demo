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

A sample of the results looks like this, using 10 000 data points, sampling 20%, and using 5 iterations

```
benjamin.daunoravicius@BDaunor-M-2WH0G latency_statistical_analysis_demo % make run                                                           
./venv/bin/python latency_simulation.py

Running analysis with lognormal distribution:

Iteration 1:
  Full Data Percentiles: p90=4.27 s, p95=5.59 s, p99=9.19 s
  Sampled Data Percentiles: p90=4.28 s, p95=5.82 s, p99=9.26 s
Iteration 2:
  Full Data Percentiles: p90=4.26 s, p95=5.60 s, p99=9.60 s
  Sampled Data Percentiles: p90=4.33 s, p95=5.85 s, p99=10.56 s
Iteration 3:
  Full Data Percentiles: p90=4.28 s, p95=5.51 s, p99=9.14 s
  Sampled Data Percentiles: p90=4.29 s, p95=5.51 s, p99=9.28 s
Iteration 4:
  Full Data Percentiles: p90=4.46 s, p95=5.84 s, p99=9.71 s
  Sampled Data Percentiles: p90=4.37 s, p95=5.92 s, p99=9.59 s
Iteration 5:
  Full Data Percentiles: p90=4.28 s, p95=5.64 s, p99=9.31 s
  Sampled Data Percentiles: p90=4.20 s, p95=5.64 s, p99=9.89 s
  Sampled Data p90 SE: 0.03
  Sampled Data p95 SE: 0.08
  Sampled Data p99 SE: 0.24

Running analysis with weibull distribution:

Iteration 1:
  Full Data Percentiles: p90=3.01 s, p95=3.43 s, p99=4.26 s
  Sampled Data Percentiles: p90=3.02 s, p95=3.44 s, p99=4.41 s
Iteration 2:
  Full Data Percentiles: p90=3.08 s, p95=3.50 s, p99=4.34 s
  Sampled Data Percentiles: p90=3.06 s, p95=3.48 s, p99=4.26 s
Iteration 3:
  Full Data Percentiles: p90=3.04 s, p95=3.48 s, p99=4.30 s
  Sampled Data Percentiles: p90=3.02 s, p95=3.45 s, p99=4.19 s
Iteration 4:
  Full Data Percentiles: p90=3.02 s, p95=3.44 s, p99=4.36 s
  Sampled Data Percentiles: p90=3.02 s, p95=3.44 s, p99=4.44 s
Iteration 5:
  Full Data Percentiles: p90=3.03 s, p95=3.48 s, p99=4.36 s
  Sampled Data Percentiles: p90=3.02 s, p95=3.44 s, p99=4.33 s
  Sampled Data p90 SE: 0.01
  Sampled Data p95 SE: 0.01
  Sampled Data p99 SE: 0.05

Running analysis with pareto distribution:

Iteration 1:
  Full Data Percentiles: p90=3.20 s, p95=4.03 s, p99=6.87 s
  Sampled Data Percentiles: p90=3.11 s, p95=3.87 s, p99=6.49 s
Iteration 2:
  Full Data Percentiles: p90=3.23 s, p95=4.11 s, p99=6.75 s
  Sampled Data Percentiles: p90=3.21 s, p95=3.93 s, p99=7.01 s
Iteration 3:
  Full Data Percentiles: p90=3.17 s, p95=3.93 s, p99=6.65 s
  Sampled Data Percentiles: p90=3.25 s, p95=3.95 s, p99=5.91 s
Iteration 4:
  Full Data Percentiles: p90=3.21 s, p95=4.05 s, p99=7.12 s
  Sampled Data Percentiles: p90=3.22 s, p95=4.07 s, p99=6.96 s
Iteration 5:
  Full Data Percentiles: p90=3.23 s, p95=4.08 s, p99=6.98 s
  Sampled Data Percentiles: p90=3.27 s, p95=4.17 s, p99=7.02 s
  Sampled Data p90 SE: 0.03
  Sampled Data p95 SE: 0.05
  Sampled Data p99 SE: 0.22
```