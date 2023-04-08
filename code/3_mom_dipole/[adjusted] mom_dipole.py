import numpy as np
import matplotlib.pyplot as plt

# Define dipole geometry
L = 0.5     # length in meters
d = 0.1     # distance from reference point in meters

# Define number of elements and element length
nelem = 20
lelem = L / nelem

# Define impedance matrix
Z = np.zeros((nelem, nelem), dtype=np.complex128)

# Calculate mutual impedances
for i in range(nelem):
    for j in range(nelem):
        if i == j:
            Z[i,j] = 0.5j*np.pi
        else:
            r = np.sqrt((i-j)**2*lelem**2 + d**2)
            Z[i,j] = np.exp(-1j*2*np.pi*r/0.3)*1j/4/np.pi/r

# Define voltage vector
V = np.zeros((nelem,1), dtype=np.complex128)
V[0] = 1.

# Solve for current vector
I = np.linalg.solve(Z, V)

# Calculate radiated field in x-y plane
theta = np.linspace(0, np.pi, 361)
Etheta = np.zeros_like(theta)
for th in range(len(theta)):
    for i in range(nelem):
        r = np.sqrt(i**2*lelem**2 + d**2)
        Et = np.exp(-1j*2*np.pi*r/0.3)*I[i]*np.sin(theta[th])*lelem
        Etheta[th] += Et[0]

# Plot radiation pattern
plt.polar(theta, np.abs(Etheta))
plt.title("Radiation Pattern of Half-Wave Dipole Antenna")
plt.savefig('fig_mom_dipole.png', dpi=600, bbox_inches='tight')
plt.show()
