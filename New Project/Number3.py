# Atoms calculator
def num_atoms(element_mass, atomic_weight = 196.97):
    avogadro = 6.022 * 10**23
    return (element_mass / atomic_weight) * avogadro

print(num_atoms(10))
print(num_atoms(10, 12.001))
print(num_atoms(10, 1.008))