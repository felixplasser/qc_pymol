'''
Collection of routines for plotting densities and ESPs.

(c) 2019 Felix Plasser, Loughborough University

License: GPL-3.0
'''

import glob
from os import path
from pymol import cmd, stored, colorramping

# Set some defaults for colorramp here
stored.ramp_vals = [-0.4,-0.08,-0.02, 0, 0.02, 0.08, 0.4]
#stored.ramp_cols = ["red", "orange", "yellow", "white", "cyan", "blue", "purple"]
stored.ramp_cols = ["purple", "blue", "cyan", "white", "yellow", "orange", "red"]

def dens_plot_init():
    """
    Initialise some settings for density export.
    """
    print("Initialising settings for dens_plot ...")
    cmd.set("ray_opaque_background", 0)
    cmd.set("specular_intensity", 0.)
    cmd.set("depth_cue", "off")
    cmd.set("transparency", 0.2)

    cmd.set("stick_radius", 0.1)
    cmd.show("sticks")
    cmd.color("gray30", "ele c")

def show_dens(fname, isovals="-0.02 0.02", colors="cyan orange", delete=True):
    """
    Show a density as isosurface.
     fname - Name of the file containing the isosurface on a grid
     isovals - Space-separated string of iso Isovalues
     colors  - Space-separated string of colors
    Example:
     show_dens dens.cube, -0.03 0.03, red blue
    """
    dname = path.splitext(fname)[0] #.replace('singlet', 'S').replace('triplet', 'T')
    if delete:
        cmd.delete(dname + "*")
    cmd.load(fname, dname, zoom=0)

    il = isovals.split()
    cl = colors.split()
    for i in range(len(il)):
        show_iso(dname, float(il[i]), cl[i])

    return dname

def save_dens(fname, isovals="-0.02 0.02", colors="cyan orange", delete=True):
    """
    Plot and save the density (same options as show_dens).
    """
    dname = show_dens(fname, isovals, colors)
    pname = dname + ".png"
    cmd.png(pname, ray=1)
    print("Image saved as %s."%pname)
    if delete:
        cmd.delete(dname + "*")

def save_dens_multi(regex, isovals="-0.02 0.02", colors="cyan orange"):
    """
    Plot and save multiple densities.
    regex - Regular expressions for specifying files.
    """
    fnames = glob.glob(regex)
    print("fnames:", fnames)
    for fname in fnames:
        save_dens(fname, isovals, colors)

def map_esp(dens, esp, iso=0.02):
    """
    Map the ESP onto the density.
    dens - File containing the density on a grid
    esp  - File containing the ESP on a grid
    iso  - isovalue for the density
    """
    ename = path.splitext(esp)[0]
    dname = "esp_map" #"d_%s"%ename
    rname = "esp_ramp" #"r_%s"%ename

    cmd.load(dens, dname, zoom=0)
    cmd.load(esp, ename, zoom=0)

    cmd.ramp_new(rname, ename, stored.ramp_vals, stored.ramp_cols)

    show_iso(dname, float(iso), rname)

cmd.extend("dens_plot_init", dens_plot_init)
cmd.extend("show_dens", show_dens)
cmd.extend("save_dens", save_dens)
cmd.extend("save_dens_multi", save_dens_multi)
cmd.extend("map_esp", map_esp)

def dens_plot_help():
    help(dens_plot_init)
    help(show_dens)
    help(save_dens)
    help(map_esp)

cmd.extend("dens_plot_help", dens_plot_help)

# internal functions
def show_iso(dname, iso, color="white"):
    sname = "%s%.4f"%(dname, iso)
    cmd.isosurface(sname, dname, iso)
    cmd.set("surface_color", color, sname)
    cmd.rebuild()
