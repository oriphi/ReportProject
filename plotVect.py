import matplotlib.pyplot as plt
import numpy as np

Data = [
    11619,
    10433,
    9240 ,
    8358 ,
    9333 ,
    8012 ,
    8442 ,
    9151 ,
    7376 ,
    7829 ,
    8049 ,
    10202,
    11387,
    12755,
    13894,
    15551,
    18007,
    18358
    ]

X = np.array(range(18))
Y = np.array(Data)

labels = [ str(2*i) for i in range(9)]
plt.scatter(X,Y)
plt.xticks(X[::2],labels)
plt.xlabel("Vectorization factor")
plt.ylabel("Execution time (Cycles)")
plt.show()
