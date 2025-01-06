import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', alpha=0.5)
    plt.xticks(range(1850, 2076, 25))
    plt.xlim(1850, 2075)

    # Create first line of best fit
    extrapolate = range(df['Year'].iloc[0], 2051)
    m = linregress(df['Year'], df['CSIRO Adjusted Sea Level']).slope
    c = linregress(df['Year'], df['CSIRO Adjusted Sea Level']).intercept  
    plt.plot(extrapolate, m*extrapolate + c, color='r')

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    extrapolate = range(2000, 2051)
    m = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level']).slope
    c = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level']).intercept
    plt.plot(extrapolate, m*extrapolate + c, 'r')
    
	# Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
