from IPython.core.pylabtools import figsize
#import numpy as np
from matplotlib import pyplot as plt

figsize(12.5, 4)

colors = ["#348ABD", "#A60628"]
prior = [1 / 21., 20 / 21.]
posterior = [0.087, 1 - 0.087]
bar_width = 0.25

plt.bar([0, .7], prior, alpha=0.4, width=bar_width,\
        color=colors[0], label="prior distribution", \
        lw="3", edgecolor="#348ABD")

plt.bar([0 + bar_width, .7 + bar_width], posterior, alpha=0.4, \
        width=bar_width, color=colors[1],\
        label="posterior distribution",\
        lw="3", edgecolor="#A60628")

plt.xticks([bar_width / 2.0, .7 + bar_width / 2.0], ["Librarian", "Farmer"])
plt.ylabel("Probability")
plt.legend(loc="upper left")
plt.title("Prior and posterior probabilities of Steve's occupation")
plt.show()
