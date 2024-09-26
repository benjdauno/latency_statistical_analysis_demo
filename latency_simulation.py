import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
from datetime import datetime
import os

class LatencyAnalyzer:
    def __init__(self, n, z, m, distribution_type="lognormal"):
        self.n = n
        self.z = z
        self.m = m
        self.distribution_type = distribution_type  # Determines the distribution used for data generation
        self.rng = default_rng()

    def generate_data(self):
        """Generate data using different distributions to account for uncertainty in latency patterns."""
        if self.distribution_type == "lognormal":
            mu, sigma = 0.5, 0.75  # mean and standard deviation of the log-normal distribution
            data = np.random.lognormal(mean=mu, sigma=sigma, size=self.n)
        elif self.distribution_type == "weibull":
            shape, scale = 2, 2  # Weibull distribution parameters
            data = np.random.weibull(shape, self.n) * scale
        elif self.distribution_type == "pareto":
            shape = 3  # Pareto distribution parameter
            data = (np.random.pareto(shape, self.n) + 1) * 1.5  # Adjust the scale
        else:
            modes = [1.5, 2.5, 3.5, 4.5]
            weights = [0.8, 0.1, 0.05, 0.05]
            data = self.rng.choice(modes, self.n, p=weights)
            data = data + np.random.normal(0, 0.2, self.n)

        return data

    def calculate_standard_error(self, values):
        """Calculate standard error from a list of values."""
        return np.std(values, ddof=1) / np.sqrt(len(values))
    
    def analyze_data(self, data):
        """Calculate percentiles for the full and sampled data."""
        data[data < 1] = 1

        # Calculate percentiles for the full dataset (without sampling)
        full_p90 = np.percentile(data, 90)
        full_p95 = np.percentile(data, 95)
        full_p99 = np.percentile(data, 99)

        # Sample m% of the data points
        sample_size = int(self.m / 100 * self.n)
        sampled_data = np.random.choice(data, sample_size, replace=False)

        # Calculate percentiles for the sampled data
        sampled_p90 = np.percentile(sampled_data, 90)
        sampled_p95 = np.percentile(sampled_data, 95)
        sampled_p99 = np.percentile(sampled_data, 99)

        return full_p90, full_p95, full_p99, sampled_p90, sampled_p95, sampled_p99

    def report_iteration_results(self, full_p90, full_p95, full_p99, sampled_p90, sampled_p95, sampled_p99, i):
        """Report percentile values for each iteration."""
        print(f"Iteration {i+1}:")
        print(f"  Full Data Percentiles: p90={full_p90:.2f} s, p95={full_p95:.2f} s, p99={full_p99:.2f} s")
        print(f"  Sampled Data Percentiles: p90={sampled_p90:.2f} s, p95={sampled_p95:.2f} s, p99={sampled_p99:.2f} s")

    def report_final_standard_error(self, results):
        """Calculate and report the standard error for percentiles across iterations."""
        full_p90s, full_p95s, full_p99s = [], [], []
        sampled_p90s, sampled_p95s, sampled_p99s = [], [], []

        for result in results:
            full_p90s.append(result[0])
            full_p95s.append(result[1])
            full_p99s.append(result[2])
            sampled_p90s.append(result[3])
            sampled_p95s.append(result[4])
            sampled_p99s.append(result[5])

        # Calculate standard errors

        se_sampled_p90 = self.calculate_standard_error(sampled_p90s)
        se_sampled_p95 = self.calculate_standard_error(sampled_p95s)
        se_sampled_p99 = self.calculate_standard_error(sampled_p99s)

        # Report standard error
        print(f'  Sampled Data p90 SE: {se_sampled_p90:.2f}')
        print(f'  Sampled Data p95 SE: {se_sampled_p95:.2f}')
        print(f'  Sampled Data p99 SE: {se_sampled_p99:.2f}')

    def plot_data(self, data, timestamp, i):
        """Plot the data distribution for each iteration."""
        plt.hist(data, bins=50, edgecolor='k')
        plt.xlabel(f'Latency (s)')
        plt.ylabel('Frequency')
        plt.title(f'Latency Distribution {timestamp}-{i+1} {self.distribution_type} Distribution')
        plt.savefig(f'results/latency_distribution_{timestamp}_{i+1}_{self.distribution_type}.png')
        plt.close()

    def run_iterations(self):
        """Run multiple iterations and calculate percentiles and SE for each iteration."""
        results = []
        for i in range(self.z):
            data = self.generate_data()
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            full_p90, full_p95, full_p99, sampled_p90, sampled_p95, sampled_p99 = self.analyze_data(data)
            
            # Store the results
            results.append((full_p90, full_p95, full_p99, sampled_p90, sampled_p95, sampled_p99))
            
            # Report results for this iteration
            self.report_iteration_results(full_p90, full_p95, full_p99, sampled_p90, sampled_p95, sampled_p99, i)
            
            # Plot data for this iteration
            self.plot_data(data=data, timestamp=timestamp, i=i)

        # Report the standard error across all iterations
        self.report_final_standard_error(results)

# Usage example
z = 5  # Number of iterations
n = 10000  # Number of data points per iteration
m = 20  # Percentage of data points to sample

# Create results directory if not exists
if not os.path.exists("results"):
    os.makedirs("results")

# You can switch between distributions
for dist_type in ["lognormal", "weibull", "pareto"]:
    print(f"\nRunning analysis with {dist_type} distribution:\n")
    analyzer = LatencyAnalyzer(n=n, z=z, m=m, distribution_type=dist_type)
    analyzer.run_iterations()
