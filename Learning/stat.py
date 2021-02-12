from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

A=np.random.normal(size=1000)

plt.hist(A,bins=100)
plt.show()
print(np.mean(A))
print(np.std(A))