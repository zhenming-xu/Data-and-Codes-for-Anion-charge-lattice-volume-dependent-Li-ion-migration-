from plot import hm_barrier, hm_tet

file_name = "lithium-chlroine-barrier.txt" #input("file to be open: ")
with open(file_name) as data_file:
    lines = data_file.readlines()
with open("energy.csv", "a") as output_file:
    output_file.write("type  barrier  tet\n")

#objects_no = int(input("number of objects: "))
objects_no = 15 * 15
for i in range(objects_no): #this is the number of the objects
    line_name = lines[8*i].strip()
    energy = []
    for j in range(1, 8):
        energy_temp = lines[8*i+j].split()[3]
        energy.append(float(energy_temp))
    energy_max = max(energy)
    energy_min = min(energy)
    energy_bar = energy_max - energy_min
    energy_tet = energy[-1]
    #if energy_bar > 1.4:
    #    with open("bad_point.csv", "a") as bad_file:
    #        output = line_name + "  "
    #        output += str(energy_bar) + "\n"
    #        bad_file.write(output)
    with open("energy.csv", "a") as output_file:
        output = line_name + "  "
        output += str(energy_bar) + "  "
        output += str(energy_tet) + "\n"
        output_file.write(output)

hm_barrier()
hm_tet()

