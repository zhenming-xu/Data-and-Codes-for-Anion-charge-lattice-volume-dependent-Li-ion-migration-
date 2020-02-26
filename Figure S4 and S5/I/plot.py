import matplotlib.pyplot as plt
import matplotlib
import numpy as np

#charge_no = int(input("number of charge: "))
#vol_no = int(input("number of volume: "))
charge_no = 13
vol_no = 11
#volume_1 = float(input("volume: "))
volume_1 = 1145.21196159122
#atom_no = int(input("number of atoms: "))
atom_no = 48
#charge_min = int(input("start of charge: "))
#charge_max = int(input("final of charge: "))
charge_min = 25
charge_max = 85
vol_min = 128 #int(input("start of vol: "))
vol_max = 148 #int(input("final of vol: "))
element = "I" #input("element: ")

def hm_barrier():
    with open("energy.csv") as energy_file:
        lines = energy_file.readlines()
    lines.pop(0)
    barrier = []
    for line in lines:
        barrier_temp = float(line.split()[1])
        barrier.append(barrier_temp)
    barrier = np.array(barrier)
    barrier = barrier.reshape(15, 15) #charge, volume
    volume_factor = []
    volume = []
    for i in range(vol_min, vol_max+1, 2): #volume
        volume_factor.append(i/100)
    for vol in volume_factor:
        volume.append(round(vol**3*volume_1/atom_no, 2)) #volume
    charge = []
    for i in range(charge_min, charge_max+1, 5): #charge
        charge.append(i/100)

    fig, ax = plt.subplots()
    barrier = np.delete(barrier, [0,1,2,3], axis=1)
    barrier = np.delete(barrier, [0,1], axis=0)
    im = ax.imshow(barrier, cmap=plt.cm.Purples)

    ax.set_xticks(np.arange(len(volume)))
    ax.set_yticks(np.arange(len(charge)))
    ax.set_xticklabels(volume)
    ax.set_yticklabels(charge)
    ax.set_xlabel("Volume / " + r"$\AA ^ 3$")
    ax.set_ylabel("Charge / e")
    ax.set_title("charge-volume-energy barrier (Li-"+element+")")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Energy barrier / eV", rotation=-90, va="bottom")
    plt.savefig("energy_barrier_Li-"+element+".png", bbox_inches='tight')
    plt.show()


def hm_tet():
    with open("energy.csv") as energy_file:
        lines = energy_file.readlines()
    lines.pop(0)
    barrier = []
    for line in lines:
        barrier_temp = float(line.split()[2])
        barrier.append(barrier_temp)
    barrier = np.array(barrier)
    barrier = barrier.reshape(15,15)
    volume_factor = []
    volume = []
    for i in range(vol_min, vol_max+1, 2):
        volume_factor.append(i/100)
    for vol in volume_factor:
        volume.append(round(vol**3*volume_1/atom_no, 2))
    charge = []
    for i in range(charge_min, charge_max+1, 5):
        charge.append(i/100)

    fig, ax = plt.subplots()
    barrier = np.delete(barrier, [0,1,2,3], axis=1)
    barrier = np.delete(barrier, [0,1], axis=0)
    im = ax.imshow(barrier, cmap=plt.cm.bwr, vmin=-0.6, vmax=0.6) 

    ax.set_xticks(np.arange(len(volume)))
    ax.set_yticks(np.arange(len(charge)))
    ax.set_xticklabels(volume)
    ax.set_yticklabels(charge)
    ax.set_xlabel("Volume / " + r"$\AA ^ 3$")
    ax.set_ylabel("Charge / e")
    ax.set_title("charge-volume-energy of site_tet (Li-"+element+")")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Energy differences (Tet - Oct) / eV", rotation=-90, va="bottom")
    plt.savefig("tet_energy_Li-"+element+".png", bbox_inches='tight')
    plt.show()

