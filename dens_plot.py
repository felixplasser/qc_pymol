from pymol import cmd, stored, colorramping

# Set some defaults here
# Isovalues and colors for density plotting
stored.isocol = [(-0.03, "red"), (0.03, "blue")]
# For colorramp
stored.ramp_vals = [-0.4,-0.08,-0.02, 0, 0.02, 0.08, 0.4]
stored.ramp_cols = ["red","orange","yellow", "white", "cyan", "blue", "purple"]

def show_dens(fname):
    """
    Show a density as isosurface.
    fname - Name of the file containing the isosurface on a grid
    """
    dname = fname.split('.')[0]
    cmd.load(fname, dname)

    for iso, color in stored.isocol:
        print iso, color
        show_iso(dname, iso, color)

def map_esp(dens, esp, iso=0.02):
    """
    Map the ESP onto the density.
    dens - File containing the density on a grid
    esp  - File containing the ESP on a grid
    iso  - isovalue for the density
    """
    dname = dens.split('.')[0]
    cmd.load(dens, dname)

    ename = esp.split('.')[0]
    cmd.load(esp, ename)
    rname = "%s_r"%ename

    cmd.ramp_new(rname, ename, stored.ramp_vals, stored.ramp_cols)

    show_iso(dname, iso, rname)

def set_iso_color(ic_string):
    """
    Set isovalues and colors, as specified by ic_string, e.g.
    set_iso_color, 0.01 cyan -0.01 orange
    """
    stored.isocol = []
    ic = ic_string.split()
    while(len(ic)>0):
        iso   = float(ic.pop(0))
        color = ic.pop(0)
        stored.isocol.append((iso, color))
    print stored.isocol

cmd.extend("show_dens", show_dens)
cmd.extend("map_esp", map_esp)
cmd.extend("set_iso_color", set_iso_color)

# internal functions
def show_iso(dname, iso, color="white"):
    sname = "%s%.4f"%(dname, iso)
    cmd.isosurface(sname, dname, iso)
    cmd.set("surface_color", color, sname)
    cmd.rebuild()
