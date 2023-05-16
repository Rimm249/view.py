# First name, last name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
### Important! If you are NOT using JupyterLab, comment the next line with #.
#%matplotlib inline

# a)

# b)

# Plot
L = [17,24,23,23,22,21,31,17,25,16,30,20,21,20,30,14,16,28,10,11,20,
     16,26,27,31,26,19,12,12,19,23,17,24,19,12,24,25,15,33,23,13,23,
     25,21,18,15,25,13,18,18,18,28,19,24,24,14,19,15,20,30,21,12,17,
     14,20,15,14,24,28,27,24,25,12,17,18,18,18,18,26,23,22,27,22,15,
     32,30,18,22,28,18,11,7,15,24,23,27,24,24,17,22]
plt.hist(L)             # !!! Swap this line with the next after completion of a) and b).
# plt.hist(df['sum'])
plt.title('Point distribution')
plt.xlabel('points')
plt.ylabel('number (of persons)');
plt.show()

# c)

# d)

# e)