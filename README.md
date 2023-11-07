# qc_pymol
Scripts for using [PyMOL](https://pymol.org) together with quantum chemistry programs. So far this includes utilities for plotting densities and ESPs, and drawing arrows for dipole moments.

*Author*: Felix Plasser

Please use [github Issues](https://github.com/felixplasser/qc_pymol/issues) if you have any questions or suggestions.
Contributions to the code are very welcome (for example via a pull request).

![](https://1.bp.blogspot.com/-lyJBdoH-K7Q/XYH95JlMtWI/AAAAAAAACPI/JzvrxxqmucQ4akhMy8hSy3FaNgtwQCiuQCLcBGAsYHQ/s320/esp20.png)
![](https://1.bp.blogspot.com/-HBb3eU868Uw/XYH92-wo-8I/AAAAAAAACOw/FsQeM-renh0Q4c75oQsw0SlogpuPVSfJwCLcBGAsYHQ/s320/esp02.png)

## Plotting of densities and electrostatic potentials

Load the script file from the PyMOL console and initialize some settings
~~~~
run <qc_pymol>/dens_plot.py
dens_plot_init
~~~~

Plot a density given as cube file
~~~~
show_dens dens.cube
~~~~

Map the ESP onto the density
~~~~
map_esp dens.cube, esp.cube
~~~~

Plot all file with suffix `cube` using isovalues of `+/-0.005`

~~~~
save_dens_multi cube, -0.005 0.005
~~~~

Information about all the contained functions and options
~~~~
dens_plot_help
~~~~
