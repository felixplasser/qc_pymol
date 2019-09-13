from pymol import cmd, stored, colorramping

# Set some defaults for colorramp here
stored.ramp_vals = [-0.4,-0.08,-0.02, 0, 0.02, 0.08, 0.4]
stored.ramp_cols = ["red","orange","yellow", "white", "cyan", "blue", "purple"]

def show_dens(fname, isovals="-0.02 0.02", colors="cyan orange"):
    """
    Show a density as isosurface.
     fname - Name of the file containing the isosurface on a grid
     isovals - Space-separated string of iso Isovalues
     colors  - Space-separated string of colors
    Example:
     show_dens dens.cube, -0.03 0.03, red blue
    """
    dname = fname.split('.')[0]
    cmd.load(fname, dname, zoom=0)

    il = isovals.split()
    cl = colors.split()
    for i in range(len(il)):
        show_iso(dname, float(il[i]), cl[i])

def save_dens(fname, isovals="-0.02 0.02", colors="cyan orange"):
    """
    Plot and save the density (same options as show_dens).
    """
    dname = fname.split('.')[0]
    show_dens(fname, isovals, colors)
    cmd.ray()
    pname = dname + ".png"
    cmd.png(pname)
    cmd.delete(fname.split('.')[0]+"*")

def map_esp(dens, esp, iso=0.02):
    """
    Map the ESP onto the density.
    dens - File containing the density on a grid
    esp  - File containing the ESP on a grid
    iso  - isovalue for the density
    """
    ename = esp.split('.')[0]
    dname = "d_%s"%ename
    rname = "r_%s"%ename

    cmd.load(dens, dname, zoom=0)
    cmd.load(esp, ename, zoom=0)

    cmd.ramp_new(rname, ename, stored.ramp_vals, stored.ramp_cols)

    show_iso(dname, iso, rname)

# def set_iso_color(ic_string):
#     """
#     Set isovalues and colors, as specified by ic_string, e.g.
#       set_iso_color, 0.01 cyan -0.01 orange
#     """
#     stored.isocol = []
#     ic = ic_string.split()
#     while(len(ic)>0):
#         iso   = float(ic.pop(0))
#         color = ic.pop(0)
#         stored.isocol.append((iso, color))
#     print stored.isocol

def dens_plot_help():
    help(show_dens)
    help(save_dens)
    help(map_esp)

cmd.extend("dens_plot_help", dens_plot_help)
cmd.extend("show_dens", show_dens)
cmd.extend("save_dens", save_dens)
cmd.extend("map_esp", map_esp)
#cmd.extend("set_iso_color", set_iso_color)

# internal functions
def show_iso(dname, iso, color="white"):
    sname = "%s%.4f"%(dname, iso)
    cmd.isosurface(sname, dname, iso)
    cmd.set("surface_color", color, sname)
    cmd.rebuild()
