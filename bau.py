import numpy as np
import pandas as pd

a = np.linspace(0, 0.25, num=5)
plt.plot(a)
print(a)

b = pd.Series(a)
b.name = 'b'  # Add a name to the series
print(b)

c = np.linspace(2, 3, num=5)
plt.plot(c)
print(c)

c = pd.Series(c)
c.name = 'c'  # Add a name to the series
print(c)

# Now, merge the dataframes
bc = pd.merge(b.to_frame(), c.to_frame(), left_index=True, right_index=True)
print(bc)
