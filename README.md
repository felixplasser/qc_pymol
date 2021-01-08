# qc_pymol
Scripts for using pymol together with quantum chemistry programs. So far this includes utilities for plotting densities/electrostatic potentials and arrows for dipole moments.

Author: Felix Plasser

Note: these tools are still at a very rudimentary stage.

If you have any additions or improvements, please send me a pull request.

![](https://1.bp.blogspot.com/-lyJBdoH-K7Q/XYH95JlMtWI/AAAAAAAACPI/JzvrxxqmucQ4akhMy8hSy3FaNgtwQCiuQCLcBGAsYHQ/s320/esp20.png)
![](https://1.bp.blogspot.com/-HBb3eU868Uw/XYH92-wo-8I/AAAAAAAACOw/FsQeM-renh0Q4c75oQsw0SlogpuPVSfJwCLcBGAsYHQ/s320/esp02.png)

## Plotting of densities and electrostatic potentials

Load the script file from the PyMOL console
~~~~
run <qc_pymol>/dens_plot.py
~~~~

Plot a density given as cube file
~~~~
show_dens dens.cube
~~~~

Map the ESP onto the density
~~~~
map_esp dens.cube, esp.cube
~~~~

Information about all the contained functions and options
~~~~
dens_plot_help
~~~~
