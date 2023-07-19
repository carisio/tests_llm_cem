import numpy as np

eps_0 = 8.854e-12
mu_0 = 4 * np.pi * 1e-7
eps_r = 1.0
mu_r = 1.0

L_x = 1  # x-dimensions of resonant cavity in m
L_y = 0.5  # ditto y
L_z = 0.75  # ditto z

N_x = 8  # Number of Yee cells in x, y and z directions.
N_y = 4
N_z = 6
refine = int(input('Factor to refine mesh by? (default 2): ') or 2)
N_x *= refine
N_y *= refine
N_z *= refine

Delta_x = L_x / N_x  # Spatial cell size in x, y and z directions
Delta_y = L_y / N_y
Delta_z = L_z / N_z

Delta_s = min([Delta_x, Delta_y, Delta_z])  # Courant limit given by smallest spatial step
c = 1 / np.sqrt(eps_0 * mu_0)
CFL = Delta_s / (np.sqrt(3) * c)  # Courant limit

N_t = 2 ** 10 * refine  # power of 2
Delta_t = CFL * 1


# Dimension the field vectors - will be overwritten in place
E_x = np.zeros((N_x, N_y + 1, N_z + 1))
E_y = np.zeros((N_x + 1, N_y, N_z + 1))
E_z = np.zeros((N_x + 1, N_y + 1, N_z))
H_x = np.zeros((N_x + 1, N_y, N_z))
H_y = np.zeros((N_x, N_y + 1, N_z))
H_z = np.zeros((N_x, N_y, N_z + 1))

mu = mu_0 * mu_r  # In a general code, this could vary from cell to cell
epsilon = eps_0 * eps_r  # Ditto.

# Inject source - random noise with zero mean
# Only TE_z modes sought - only H_z excited.
H_z[:, :, :] = np.random.rand(N_x, N_y, N_z + 1) - 0.5

# Allocate storage for field samples
t = np.zeros(N_t)
t[0] = Delta_t
H_z_t = np.zeros(N_t)


import numpy as np

# Rest of the code...

for n in range(N_t):
    print(n+1)
    # Save Hz field in the centre of the box
    t[n] = (n+1) * Delta_t
    H_z_t[n] = H_z[N_x // 2, N_y // 2, N_z // 2]

    # Update H fields for t^n+1/2. Dimensions are conforming.
    H_x = H_x + Delta_t / mu * (np.diff(E_y, axis=2) / Delta_z - np.diff(E_z, axis=1) / Delta_y)
    H_y = H_y + Delta_t / mu * (np.diff(E_z, axis=0) / Delta_x - np.diff(E_x, axis=2) / Delta_z)
    H_z = H_z + Delta_t / mu * (np.diff(E_x, axis=1) / Delta_y - np.diff(E_y, axis=0) / Delta_x)

    # Update E fields for t^n+1. Dimensions require explicit specification to make conforming.
    E_x[:, 1:N_y, 1:N_z] = E_x[:, 1:N_y, 1:N_z] + Delta_t / epsilon * (np.diff(H_z[:, :, 1:N_z], axis=1) / Delta_y - np.diff(H_y[:, 1:N_y, :], axis=2) / Delta_z)
    E_y[1:N_x, :, 1:N_z] = E_y[1:N_x, :, 1:N_z] + Delta_t / epsilon * (np.diff(H_x[1:N_x, :, :], axis=2) / Delta_z - np.diff(H_z[:, :, 1:N_z], axis=0) / Delta_x)
    E_z[1:N_x, 1:N_y, :] = E_z[1:N_x, 1:N_y, :] + Delta_t / epsilon * (np.diff(H_y[:, 1:N_y, :], axis=0) / Delta_x - np.diff(H_x[1:N_x, :, :], axis=1) / Delta_y)

Delta_f = 1 / (N_t * Delta_t)
freq = np.zeros(N_t // 2)
for kk in range(1, N_t // 2 + 1):
    freq[kk - 1] = (kk - 1) * Delta_f

import matplotlib.pyplot as plt

k_exact = [5.2359878, 7.55154489, 8.1788743, 8.9472598]  # rad/m
f_exact = np.array(k_exact) * c / (2 * np.pi)  # Hz
H_z_f = np.fft.fft(H_z_t)
dummy = [0, 0, 0, 0]

plt.plot(freq, np.abs(H_z_f[:N_t // 2]), 'b', f_exact, dummy, 'rx')
plt.pause(0.01)

# Improve the plot - only plot up to 500 MHz. Also, don't include DC term;
# this can be quite significant, depending on initial conditions.
fig = plt.figure()
end_pt = int(5e8 / Delta_f)
norm = np.max(np.abs(H_z_f[1:end_pt]))
plt.plot(freq[2:end_pt] / 1e6, np.abs(H_z_f[2:end_pt]) / norm, 'b-')
f_exact /= 1e6
plt.axvline(x=f_exact[0], linestyle='--', color='k')
plt.axvline(x=f_exact[1], linestyle='--', color='k')
plt.axvline(x=f_exact[2], linestyle='--', color='k')
plt.axvline(x=f_exact[3], linestyle='--', color='k')
plt.xlabel('f (MHz)')
plt.ylabel('H_z (normalized)')

plt.show()
