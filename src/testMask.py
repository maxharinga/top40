import numpy as np
import numpy.ma as ma
import analysis_allPositionsPeriod
import matplotlib.pyplot as plt

z = ma.masked_values([1, 10, 0, 22, 33, 0, 5], 0)
scores = analysis_allPositionsPeriod.getPositionScore(z, 1)
print ma.sum(scores)

plt.scatter(z, scores)
plt.show()

