import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

plt.plot(p)

print(p)

p = pd.Series(p)

print(p.skew())
print(p.kurt())

print(p.std())