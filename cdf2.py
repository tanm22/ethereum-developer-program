import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv
from scipy.stats import norm

def gaussian_sampler(a, b, n_samples):
    """
    Generate samples from a scaled Gaussian distribution within the interval [a, b].

    Parameters:
        a (float): Lower bound of the interval.
        b (float): Upper bound of the interval.
        n_samples (int): Number of samples to generate.

    Returns:
        np.ndarray: Array of generated samples.
    """
    # Calculate mean and standard deviation
    mu = (a + b) / 2
    sigma = (b - a) / 6

    # Generate uniformly distributed random numbers
    uniform_samples = np.random.uniform(0, 1, n_samples)

    # Apply the inverse CDF to transform uniform samples to Gaussian samples
    inverse_cdf_samples = mu + sigma * np.sqrt(2) * erfinv(2 * uniform_samples - 1)

    # Filter samples to keep only those within the interval [a, b]
    filtered_samples = inverse_cdf_samples[(inverse_cdf_samples >= a) & (inverse_cdf_samples <= b)]

    return filtered_samples

# Input parameters
while True:
    try:
        a = float(input("Enter lower bound of the interval (a): "))
        b = float(input("Enter upper bound of the interval (b): "))
        if a < b:
            break
        else:
            print("Error: Lower bound must be less than upper bound. Please try again.")
    except ValueError:
        print("Error: Input must be a number. Please try again.")

n_samples = 10000

# Generate samples
samples = gaussian_sampler(a, b, n_samples)

# Set figure size to adjust height
plt.figure(figsize=(8, 6))  # Width: 8 inches, Height: 6 inches

# Plot ideal Gaussian distribution
x = np.linspace(a, b, 1000)
mu = (a + b) / 2
sigma = (b - a) / 6
plt.plot(x, norm.pdf(x, mu, sigma), color='r', label='Ideal Gaussian Distribution')

# Plot histogram
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Sample Distribution')

# Add legend with color labels positioned at the top right corner
plt.legend(loc='upper right')

plt.title('Histogram of Scaled Gaussian Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)

# Save the plot as PNG file
plt.savefig('Plots.png')

plt.show()
