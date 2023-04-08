import matplotlib.pyplot as plt

import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

munique_r0 = np.loadtxt("munich-r0.txt")
munique_r1 = np.loadtxt("munich-r1.txt")
munique_r2 = np.loadtxt("munich-r2.txt")
ottawa_albert = np.loadtxt("ottawa-albert.txt")
ottawa_laurier = np.loadtxt("ottawa-laurier.txt")
ottawa_queen = np.loadtxt("ottawa-queen.txt")
rosslyn_arlington = np.loadtxt("rosslyn-arlington.txt")
rosslyn_meyer = np.loadtxt("rosslyn-meyer.txt")
all = np.concatenate((munique_r0, munique_r1, munique_r2, ottawa_albert, ottawa_laurier, ottawa_queen, rosslyn_arlington, rosslyn_meyer), axis=0)
X_all = all[:, 0:2]
y_all = all[:, 2]

# generate some example data
X = munique_r0[:, 0:2]
y = munique_r0[:, 2]

# normalize the inputs
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# create an MLPRegressor with one hidden layer
mlp = MLPRegressor(hidden_layer_sizes=(100,), max_iter=10000, alpha=0.01)

# train the MLPRegressor on the normalized inputs
mlp.fit(X_normalized, y)

# make predictions on new inputs
X_new = X_all
X_new_normalized = scaler.transform(X_new)
path_loss_neural_network = mlp.predict(X_new_normalized)

path_loss_genetic_algorith = -1.36 + 52.06*np.log10(28.59 + 71.24 * X_all[:, 1]) + \
        (40.69 + 8.91*np.log10(30.11 - 28.95* X_all[:, 1]))*np.log10(X_all[:, 0]/100)


# Plot the results
plt.rc('axes', labelsize=10)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.style.use('default')

fig, ax = plt.subplots()

plt.plot(np.arange(1, len(y_all)+1), y_all, c='lightgray', label='Measured')
plt.plot(np.arange(1, len(path_loss_neural_network)+1), path_loss_neural_network, c='tab:orange', label=r'Neural network')
plt.plot(np.arange(1, len(path_loss_genetic_algorith)+1), path_loss_genetic_algorith, c='tab:blue', label='[15]')

plt.axvline(x=len(y), linestyle=':', color='black')

plt.text(50, 75, 'Training data')
plt.text(1500, 75, 'Test data')

plt.xlim(0, len(path_loss_genetic_algorith))
plt.ylim(70, 180)

ax.set_xlabel('Measurement point number')
ax.set_ylabel('Path loss (dB)')

ax.legend(loc='upper center', prop={'size': 10})

plt.savefig('fig_nn_pl_900_mhz', dpi=600, bbox_inches='tight')
plt.show()