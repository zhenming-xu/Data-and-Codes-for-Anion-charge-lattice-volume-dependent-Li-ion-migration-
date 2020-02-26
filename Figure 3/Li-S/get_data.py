from plot import hm_barrier, hm_tet

with open("Li-S-barrier.txt") as data_file:
    lines = data_file.readlines()
with open("energy.csv", "a") as output_file:
    output_file.write("type  barrier  tet\n")

for i in range(196):
    line_name = lines[8*i].strip()
    energy = []
    for j in range(1, 8):
        energy_temp = lines[8*i+j].split()[3]
        energy.append(float(energy_temp))
    energy_max = max(energy)
    energy_min = min(energy)
    energy_bar = energy_max - energy_min
    energy_tet = energy[-1]
    with open("energy.csv", "a") as output_file:
        output = line_name + "  "
        output += str(energy_bar) + "  "
        output += str(energy_tet) + "\n"
        output_file.write(output)

hm_barrier()
hm_tet()

