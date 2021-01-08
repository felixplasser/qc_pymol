'''
Collection of miscellaneous routines for analysing quantum chemical calcuations.

(c) 2019 Felix Plasser, Loughborough University

License: GPL-3.0
'''

from pymol import cmd
from qc_pymol.external import cgo_arrow

au2Ang = 0.529177249

def get_coord(v):
    if not isinstance(v, str):
        return v
    elif v.startswith('['):
        return cmd.safe_list_eval(v)
    else:
        return cmd.get_atom_coords(v)

def plot_dip(dipvec, scale=1, radius=0.15, color="tv_green"):
    """
    Plot a dipole moment.
    dipvec - dipole moment vector in a.u.
    scale=1 means that the error length is 2*mu/e
    """
    cmd.delete("arrow*")
    dv = get_coord(dipvec)
    p1 = [-val * scale * au2Ang for val in dv]
    p2 = [ val * scale * au2Ang for val in dv]

    length = sum(val*val for val in dv)
    hlength = min(length/2., radius*3.0)

    cgo_arrow.cgo_arrow(p1, p2, radius=radius, hlength=hlength, hradius=radius*2.0, color=color)

cmd.extend("plot_dip", plot_dip)
