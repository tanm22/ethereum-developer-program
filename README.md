# Gaussian Sampler with Scaled Distribution

This Python script generates samples from a scaled Gaussian distribution within a specified interval and visualizes the distribution through a histogram overlaid with an ideal Gaussian distribution curve. It incorporates a custom the inverse error function (erfinv) for an accurate transformation of uniform samples to Gaussian samples. We also plot the ideal gaussian distribution between a and b to verify our histogram.

## How to Use

1. **Install Dependencies:**
   - Ensure you have Python installed on your system.
   - Install required dependencies using pip:
     ```
     pip install numpy matplotlib scipy
     ```

2. **Download the Code:**
   - Download the provided Python script (gaussian_sampler.py) to your local machine.

3. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the downloaded script.
   - Run the script using Python:
     ```
     python gaussian_sampler.py
     ```

4. **Follow Prompts:**
   - Enter the lower and upper bounds of the interval as prompted by the script.(Real Numbers)

5. **View Output:**
   - The script will generate a plot displaying the histogram of the sampled distribution along with the ideal Gaussian distribution curve.
   - The plot will also be saved as "Plots.png" in the same directory for future reference.

## Required Dependencies

- `numpy`: For numerical computations and array operations.
- `matplotlib.pyplot`: For data visualization and plotting.
- `scipy.special.erfinv`: Inverse error function for accurate transformation of uniform samples to Gaussian samples.
- `scipy.stats.norm`: Standard normal (Gaussian) continuous random variable.

## Note

- Ensure you have the necessary permissions to install Python packages and run scripts on your system.
- Adjust the script as needed for specific use cases or requirements.

## Team-members

- Apoorv Tandon (220192)
- Daksh Kumar Singh (220322)
- Himanshu Shekhar (220454)
- Swayamsidh Pradhan (221117)
- Tanishq Maheshwari (221128)
