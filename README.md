# Instruction of data and codes


Anion charge and lattice volume dependent Li ion migration in compounds with the face-centered cubic anion frameworks


Zhenming Xu, Xin Chen, Ronghan Chen, Xin Li, Hong Zhu, 

a.	University of Michigan–Shanghai Jiao Tong University Joint Institute, Shanghai Jiao Tong University, 800, Dongchuan Road, Shanghai, 200240, China

b.	School of Materials Science and Engineering, Shanghai Jiao Tong University, 800, Dongchuan Road, Shanghai, 200240, China

c.	John. A. Paulson School of Engineering and Applied Sciences, Harvard University, 29 Oxford St, Cambridge, Massachusetts, 02138, USA
 
 
 
# AIMD movies of fcc-type sulfur anion framework 
 
 
 
# data and codes/Figure 1/

“oxide.csv”, “sulfide.csv” and “Materials_charge_volume.opj” are the data of the anion Bader charges, lattice volumes, and Li coordination number for some common lithium oxides with fcc-type oxygen anion frameworks from the MP database. 

Figure 1 show the scatter distributions of the anion charges and lattice volumes around the fitted straight lines for some common lithium oxides and sulfides in the MP database.



# data and codes/Figure 2/

1.	“schematic diagram of activation energy.opj” is a data file created by the Origin software, and “schematic diagram of activation energy.tif ” was exported from it. 
2.	“tet-oct.vesta” is a crystal structure created by the VESTA software, and “tet-oct.tif ” was exported from it. 

Figure 2 shows Li ion migration between the two adjacent Oct and Tet sites in the local structure from the fcc-type anion framework, and the schematic diagram of the energy variations of Li ion migration between the two adjacent Oct and Tet central sites with respect to different anion charges and lattice volumes. 



# data and codes/Figure 3/Li-O/

1.	“Li-O-barrier.txt” is the raw data from NEB calculations; “energy.csv” are the raw data of Em and Ediff with respect to anion charge and lattice volume, which are extracted from “Li-O-barrier.txt” by the Python script of “get_data.py”; “energy_barrier.csv” and “energy_difference.csv” are the data array for Em and Ediff, respectively. 
2.	Using the Python script of “plot.py”, the heat maps of Em and Ediff (“energy_barrier_Li-O.png” and “tet_energy_Li-O.png”) were obtained based on the relevant data, respectively.

Figure 3 show the heat maps of the calculated Em of Li ion migration between the two adjacent Oct and Tet central sites in the artificial fcc-type oxygen and sulfur anion frameworks, and the energy differences between the Tet Li site and Oct Li site in fcc-type oxygen and sulfur anion frameworks with respect to different anion charges and lattice volumes, respectively.



# data and codes/Figure 4/

“barrier-charge-volume.opj” is a data file created by Origin software, and “barrier-charge-volume.tif ” was exported from it. 

Figure 4 shows DFT calculations monitored energy variations and Em of Li ion migration between the two adjacent Oct and Tet central sites in the artificial fcc-type oxygen anion lattices with respect to different anion charges and constant lattice volumes, and energy variations of Li ion migration in the oxygen anion lattices with different lattice volumes.



# data and codes/Figure 5/

“Comparison of energy barriers.opj” is a data file created by Origin software, and “Comparison of energy barriers.tif ” was exported from it. 

Figure 5 shows the comparisons among the predicted Em from the anion framework model, and NEB calculated Em for Li ion migration by the Tet-Oct-Tet or Oct-Tet-Oct pathways, and Em from ab-initio molecular dynamics simulations for some real lithium compounds with fcc anion frameworks.



# data and codes/Figure 6/

1.	“plot_periodic_table.ipynb” is the script of jupyter lab (python) to show the periodic table with different marks. 
2.	“electronegativity difference dependent lithium ion diffusion.png” is exported from the revenant.pptx file 

Figure 6 shows schematic diagrams of the effects of the electronegativity differences between non-mobile cation elements B and anion elements C on A ion migration, and the recommended choices of the non-mobile cation element B in the periodic table of element for achieving fast A ion migration.



# data and codes/Figure S1

1.	“Getting stable Li-M-O materials from Material Project Database.ipynb” is the script of jupyter lab (python) to get the information (energy above hull, space group, element, mp-id, and composition) of stable lithium compounds (), and store them to the csv file to “stable_lithium_oxides_from_MP_database.csv”.
2.	“Getting stable Li-M-O materials from Material Project Database.ipynb” is the script of jupyter lab (python) to get the lithium coordination environment (“lithium_chemenv_coordination_environments_for_oxides.csv”) of the stable lithium compounds in “stable_lithium_oxides_from_MP_database.csv”, and plot the pie picture of lithium coordination environment (“Lithium chemenv coordination environments for oxides.png”). 

The relevant codes and data are also available in Github, https://github.com/zhenming-xu/Matching-anion-framework-and-Li-local-environments-from-MP-database

Figure S1 shows the distributions of lithium coordination environments for oxides and sulfides in the Materials Project (MP) database originating from the Inorganic Crystal Structure Database (ICSD). 



# data and codes/Figure S2/

“Matching anion framework of sulfides from MP database.ipynb” is the script of jupyter lab (python) to get the information of anion framework type for those stable lithium compounds (“stable_lithium_oxides_from_MP_database.csv”), store them to the csv file to “matching_anion_framework_for_oxides” and plot the pie picture of the distributions of anion framework type (“Matched anion frameworks of oxides from MP database.png”).

The relevant codes and data are also available in Github, https://github.com/zhenming-xu/Matching-anion-framework-and-Li-local-environments-from-MP-database

Figure S2 shows the distributions of the matched fcc, bcc and hcp anion frameworks for the slightly distorted oxides and sulfides in the MP database.



# data and codes/Figure S3/

“anion framework.vesta” is a crystal structure created by VESTA software, and “anion framework.tif ” was exported from it. 

Figure S3 shows the structural model of Li ion migration from one octahedral site to its adjacent tetrahedral site with respect to different anion charges and lattice volumes in an artificial fcc-type anion sublattice with 48 anions.



# data and codes/Figure S4 and S5/ 
similar to data and codes/Figure 3

Figure S4 and S5 show the heat maps of the calculated Em of Li ion migration between the two adjacent Oct and Tet central sites in the artificial fcc-type halogen anion frameworks, and the energy differences between the Tet Li site and Oct Li site in fcc-type halogen anion frameworks with respect to different anion charges and lattice volumes, respectively.


# AIMD movies of fcc-type sulfur anion framework with a single Li ion

anion_charge = -0.5 e and lattice_volume = 31.76 Å3/atom
anion_charge = -0.5 e and lattice_volume = 54.87 Å3/atom
anion_charge = -1.7 e and lattice_volume = 31.76 Å3/atom
anion_charge = -1.7 e and lattice_volume = 54.87 Å3/atom

