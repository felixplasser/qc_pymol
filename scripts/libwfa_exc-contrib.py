"""
Example script.
This creates a plot representing the contributions to the energy in using files
created by Q-Chem.
Load molecular geometry first, then run save_all()
"""

from pymol import cmd
from qc_pymol import dens_plot

###
# Global variables
geom  = "geom.mol" # File with molecular coordinates
#iso_dens = "-0.002 0.002" # Isovalues for densities
#iso_orb  = "-0.05 0.05" # Isovalues for orbitals
iso_dens = "-0.005 0.005" # Isovalues for densities
iso_orb  = "-0.05 0.05" # Isovalues for orbitals
iso_esp  = 0.05 # Isovalue for ESP map
###

cmd.load(geom)
dens_plot.dens_plot_init()

def start_state(state):
    """
    This can be called before save_all
    """
    cmd.set("transparency", 0.)
    dens_plot.map_esp("%s_dens.cube"%state, "%s_trans_esp.cube"%state, iso_esp)

def save_all(state, ihomo):
    """
    Save the required images.
    state - Prefix of the state
    ihomo - Index of HOMO
    """
    # Delete stuff left over from previous runs
    cmd.delete("esp*")
    cmd.delete(state + "*")

    cmd.set("transparency", 0.2)
    # Plot the transition, hole, and electron densities
    dens_plot.save_dens("%s_trans.cube"%state, iso_dens)
    dens_plot.save_dens("%s_hole.cube"%state, iso_dens)
    dens_plot.save_dens("%s_elec.cube"%state, iso_dens)

    # NTOs
    dens_plot.save_dens("%s_nto.%i.cube"%(state, int(ihomo)), iso_orb)
    dens_plot.save_dens("%s_nto.%i.cube"%(state, int(ihomo)+1), iso_orb)

    # ESP maps
    cmd.set("transparency", 0.)
    dens_plot.map_esp("%s_dens.cube"%state, "%s_trans_esp.cube"%state, iso_esp)
    cmd.png("%s_trans_esp.png"%state, ray=1)
    dens_plot.map_esp("%s_dens.cube"%state, "%s_hole_esp.cube"%state, iso_esp)
    cmd.png("%s_hole_esp.png"%state, ray=1)
    dens_plot.map_esp("%s_dens.cube"%state, "%s_elec_esp.cube"%state, iso_esp)
    cmd.png("%s_elec_esp.png"%state, ray=1)

cmd.extend("start_state", start_state)
cmd.extend("save_all", save_all)
