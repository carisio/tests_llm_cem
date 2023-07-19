import numpy as np
import matplotlib.pyplot as plt

def dipole_radiation_pattern(length, frequency, theta):
    # Constants
    c = 3e8  # Speed of light

    # Calculate wavelength
    wavelength = c / frequency

    # Convert theta to radians
    theta_rad = np.radians(theta)

    # Calculate k (wave number)
    k = 2 * np.pi / wavelength

    # Calculate current distribution along the dipole
    x = np.linspace(-length/2, length/2, 100)
    I = np.sin(k * x)

    # Calculate electric field components
    r = np.sin(theta_rad)
    E_theta = np.sum(I * np.exp(-1j * k * x) * np.sin(theta_rad[:, np.newaxis]), axis=1)

    # Calculate radiation intensity
    U = 0.5 * np.real(np.conj(E_theta) * E_theta)

    # Normalize the radiation intensity
    U_norm = U / np.max(U)

    return U_norm

# Define the parameters of the dipole antenna
length = 0.5  # Length of the dipole in meters
frequency = 2e9  # Frequency in Hz
theta = np.arange(0, 181, 1)  # Theta angles from 0 to 180 degrees

# Calculate the radiation pattern
radiation_pattern = dipole_radiation_pattern(length, frequency, theta)

# Plot the radiation pattern
plt.figure()
plt.plot(theta, radiation_pattern)
plt.xlabel('Theta (degrees)')
plt.ylabel('Normalized Radiation Intensity')
plt.title('Radiation Pattern of Dipole Antenna')
plt.grid(True)
plt.savefig('fig_mom_dipole.png', dpi=600, bbox_inches='tight')
plt.show()

dipole_fdtd_mom = np.loadtxt("./dipole_fdtd_mom_0.5lambda_and_0.5meters.txt")
# Convert dB to linear
dipole_fdtd_mom[:, 1] = np.power(10, dipole_fdtd_mom[:, 1]/10)
dipole_fdtd_mom[:, 2] = np.power(10, dipole_fdtd_mom[:, 2]/10)
dipole_fdtd_mom[:, 3] = np.power(10, dipole_fdtd_mom[:, 3]/10)
dipole_fdtd_mom[:, 4] = np.power(10, dipole_fdtd_mom[:, 4]/10)
# Results from NEC should be normalized
dipole_fdtd_mom[:, 3] = dipole_fdtd_mom[:, 3] / np.max(dipole_fdtd_mom[:, 3])
dipole_fdtd_mom[:, 4] = dipole_fdtd_mom[:, 4] / np.max(dipole_fdtd_mom[:, 4])

# Consider only from 0 to 180 degrees
dipole_fdtd_mom = dipole_fdtd_mom[0:181, :]

theta_fdtd_mom = dipole_fdtd_mom[:, 0]
rp_fdtd_05_lambda = dipole_fdtd_mom[:, 1]
rp_fdtd_05_meters = dipole_fdtd_mom[:, 2]
rp_mom_05_lambda = dipole_fdtd_mom[:, 3]
rp_mom_05_meters = dipole_fdtd_mom[:, 4]

fig = plt.figure()
ax = plt.axes(xlim=(0, 180), ylim=(0, 1))
plt.xlabel('Angle (degree)')
plt.ylabel('Normalized radiattion pattern (linear)')

ax.plot(theta, radiation_pattern, c="royalblue", label="ChatGPT")
ax.scatter(theta_fdtd_mom[0:180:2], rp_fdtd_05_lambda[0:180:2], c="coral", label=r"EM Studio [FDTD], length = 0.5 $\lambda$", s=2)
ax.plot(theta_fdtd_mom, rp_fdtd_05_meters, c="coral", label=r"EM Studio [FDTD], length = 0.5 m")
ax.scatter(theta_fdtd_mom[1:180:2], rp_mom_05_lambda[1:180:2], c="mediumseagreen", label=r"NEC2, length = 0.5 $\lambda$", s=2)
ax.plot(theta_fdtd_mom, rp_mom_05_meters, c="mediumseagreen", label=r"NEC2, length = 0.5 m")

#ax.legend(loc="upper left")
ax.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)

plt.grid(True)
plt.savefig('fig_mom_dipole.png', dpi=600, bbox_inches='tight')
plt.show()
