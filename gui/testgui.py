import numpy as np
import matplotlib.pyplot as plt

x = np.arange(14)
y = np.sin(x / 2)

plt.step(x, y + 2, label='pre (default)')
# plt.plot(x, y + 2, 'C0o', alpha=0.5)

plt.legend(title='Parameter where:')
plt.show()