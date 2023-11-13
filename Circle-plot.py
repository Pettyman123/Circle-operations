import matplotlib.pyplot as plt
plt.axes()
circle = plt.Circle((0,0),1.5, fc='#14F5CC',ec="red")
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.show()