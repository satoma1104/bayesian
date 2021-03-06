import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

poi = stats.poisson
lambda_ = [1.5, 4.25]
colors = ["#348ABD", "#A60628"]

a = np.arange(16)
plt.bar(a, poi.pmf(a, lambda_[0]), color=colors[0],\
        label="$\lambda = %.2f$" % lambda_[0],\
        alpha=0.6, edgecolor=colors[0], lw="3")
plt.bar(a, poi.pmf(a, lambda_[1]), color=colors[1],\
        label="$\lambda = %.2f$" % lambda_[1],\
        alpha=0.6, edgecolor=colors[1], lw="3")

plt.xticks(a + 0.4, a)
plt.legend()
plt.ylabel("Probability of $k$")
plt.xlabel("$k$")
plt.title("Probability mass function of a Poisson random variable, "\
          "differing $\lambda$ values")
plt.show()
