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
    E_theta = (1j * k * np.exp(-1j * k * r)) / (4 * np.pi * r) * np.sum(I * np.exp(-1j * k * x))

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
plt.show()