import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

a = np.linspace(0, 4, 100)
expo = stats.expon
lambda_ = [0.5, 1]
colors = ["#348ABD", "#A60628"]

for l, c in zip(lambda_, colors):
    # 線を描く
    plt.plot(a, expo.pdf(a, scale=1. / l),\
             lw=3, color=c, label="$\lambda = %.1f$" % l)
    # 線とx軸の間を塗りつぶす
    plt.fill_between(a, expo.pdf(a, scale=1. / l),\
                     color=c, alpha=.33)

plt.legend()
plt.ylabel("Probability density function at $z$")
plt.xlabel("$z$")
plt.ylim(0, 1.2)
plt.title("Probabliity density function of an exponential "\
          "random value, differing $\lambda$ values")
plt.show()
