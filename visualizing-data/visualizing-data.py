# import pandas as pd
import pandas as pd
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# read csv file
g1800s = pd.read_csv('../datasets/gapminder.csv')

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()
