from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
from os import makedirs
makedirs("data", exist_ok=True)

from urllib.request import urlretrieve
urlretrieve("https://git.io/vXTVC", "data/txtdata.csv")

figsize(12.5, 3.5)

count_data = np.loadtxt("data/txtdata.csv")
n_count_data = len(count_data)
plt.bar(np.arange(n_count_data), count_data, color="#348ABD")

plt.xlabel("Time (days)")
plt.ylabel("Text messages recieved")
plt.title("Did the user's texting habits change over time?")
plt.xlim(0, n_count_data)
plt.show()

