import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (FormatStrFormatter, MultipleLocator)
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
      # Year,CSIRO Adjusted Sea Level,Lower Error Bound,Upper Error Bound,NOAA Adjusted Sea Level

    # Create scatter plot
    #print("\ndf")
    #print(df)
  
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')
    ax.set_xlim(1875.0, 2050.0)
    ax.xaxis.set_major_locator(MultipleLocator(25))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f')) 

    original_max = df['Year'].max()
    new_max = 2050

    # Create first line of best fit
    line_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    for year in range(df['Year'].max() + 1, new_max + 1):
      df.loc[len(df.index)] = [year, line_1.intercept + line_1.slope*year, np.nan, np.nan, np.nan]
    plt.plot(df['Year'], line_1.intercept + line_1.slope*df['Year'], 'y', label='Line 1')

    # Create second line of best fit
    small_df = df.loc[(df['Year'] >= 2000) & (df['Year'] <= original_max)]
    line_2 = linregress(small_df['Year'], small_df['CSIRO Adjusted Sea Level'])
    small_df.reset_index(inplace=True, drop=True)
    for year in range(original_max + 1, new_max + 1):
      small_df.loc[len(small_df.index)] = [year, line_2.intercept + line_2.slope*year, np.nan, np.nan, np.nan]
    plt.plot(small_df['Year'], line_2.intercept + line_2.slope*small_df['Year'], 'r', label='Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()