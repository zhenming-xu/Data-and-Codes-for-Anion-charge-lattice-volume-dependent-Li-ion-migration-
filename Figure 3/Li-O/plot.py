import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def hm_barrier():
    with open("energy.csv") as energy_file:
        lines = energy_file.readlines()
    lines.pop(0)
    barrier = []
    for line in lines:
        barrier_temp = float(line.split()[1])
        barrier.append(barrier_temp)
    barrier = np.array(barrier)
    barrier = barrier.reshape(14, 12)
    volume_factor = []
    volume = []
    for i in range(84, 108, 2):
        volume_factor.append(i/100)
    for vol in volume_factor:
        volume.append(round(vol**3*1145.211962/48, 2))
    charge = []
    for i in range(5, 19):
        charge.append(i/10)

    fig, ax = plt.subplots()
    im = ax.imshow(barrier, cmap=plt.cm.Reds)

    ax.set_xticks(np.arange(len(volume)))
    ax.set_yticks(np.arange(len(charge)))
    ax.set_xticklabels(volume)
    ax.set_yticklabels(charge)
    ax.set_xlabel("Volume / " + r"$\AA ^ 3$")
    ax.set_ylabel("Charge / e")
    ax.set_title("charge-volume-energy barrier (Li-O)")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Energy barrier / eV", rotation=-90, va="bottom")
    plt.savefig("energy_barrier_Li-O.png", bbox_inches='tight')
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
    barrier = barrier.reshape(14, 12)
    volume_factor = []
    volume = []
    for i in range(84, 108, 2):
        volume_factor.append(i/100)
    for vol in volume_factor:
        volume.append(round(vol**3*1145.211962/48, 2))
    charge = []
    for i in range(5, 19):
        charge.append(i/10)

    fig, ax = plt.subplots()
    im = ax.imshow(barrier, cmap=plt.cm.bwr, vmin=-1, vmax=1)

    ax.set_xticks(np.arange(len(volume)))
    ax.set_yticks(np.arange(len(charge)))
    ax.set_xticklabels(volume)
    ax.set_yticklabels(charge)
    ax.set_xlabel("Volume / " + r"$\AA ^ 3$")
    ax.set_ylabel("Charge / e")
    ax.set_title("charge-volume-energy of site_tet (Li-O)")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Energy of site_tet / eV", rotation=-90, va="bottom")
    
    plt.savefig("tet_energy_Li-O.png", bbox_inches='tight')
    plt.show()

