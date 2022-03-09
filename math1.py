import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 10.0, 30) 
# массив координат - 30 точек, равнораспределенных 
# в диапозоне от 0 до 30 

y = np.sin(x)

# рисование графики функции с помощью функции plot

plt.plot(x, y)

plt.show()

