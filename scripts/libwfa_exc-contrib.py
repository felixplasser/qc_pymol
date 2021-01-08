"""
Example script.
This creates a plot representing the contributions to the energy in using files
created by Q-Chem.
Load molecular geometry first, then run save_all()
"""

from pymol import cmd, stored
from qc_pymol import dens_plot

###
# Global variables
geom  = "geom.mol" # File with molecular coordinates
iso_dens = "-0.003 0.003" # Isovalues for densities
#iso_orb  = "-0.05 0.05" # Isovalues for orbitals
#iso_dens = "-0.005 0.005" # Isovalues for densities
iso_orb  = "-0.06 0.06" # Isovalues for orbitals
iso_esp  = 0.06 # Isovalue for ESP map
###

cmd.load(geom)
dens_plot.dens_plot_init()

stored.ramp_vals = [-0.35,-0.08,-0.02, 0, 0.02, 0.08, 0.35]
stored.ramp_cols = ["green", "marine", "cyan", "white", "yellow", "tv_red", "magenta"]

def start_state(state):
    """
    This can be called before save_all
    """
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

    # Plot the transition, hole, and electron densities
    cmd.set("transparency", 0.2)
    dens_plot.save_dens("%s_trans.cube"%state, iso_dens, "tv_red tv_blue")
    dens_plot.save_dens("%s_hole.cube"%state, iso_dens, "tv_red tv_red")
    dens_plot.save_dens("%s_elec.cube"%state, iso_dens, "tv_blue tv_blue")

    # NTOs
    cmd.set("transparency", 0.2)
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

def save_gs(state):
    """
    Save graphics related to the ground state.
    """
    # Delete stuff left over from previous runs
    cmd.delete("esp*")

    # ESP maps
    cmd.set("transparency", 0.)
    dens_plot.save_dens("%s_dens.cube"%state, str(iso_esp), "white")
    dens_plot.map_esp("%s_dens.cube"%state, "%s_dens_esp.cube"%state, iso_esp)
    cmd.png("%s_dens_esp.png"%state, ray=1)

cmd.extend("start_state", start_state)
cmd.extend("save_all", save_all)
cmd.extend("save_gs", save_gs)
