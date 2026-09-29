import matplotlib
matplotlib.use("TkAgg")  
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1,2,3],[1,4,9])
axs[0, 1].bar([1,2,3],[3,2,5])
axs[1, 0].scatter([1,2,3],[9,5,1])
axs[1, 1].hist([1,2,2,3,3,3,4,4,5])
plt.show()
