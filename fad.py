#script used in pymol program in order to visualize and manipulate a protein structure 

PyMOL>fetch 2VLA
Display> sequence
PyMOL>set_name sele,ASP123
PyMOL>set_name sele,DNA
PyMOL>color yellow,DNA
PyMOL>set_name sele,protein
PyMOL>color greencyan, protein
PyMOL>show sticks, byres all within 5 of ASP123
PyMOL>hide cartoon
PyMOL>zoom visible
PyMOL>zoom ASP123
PyMOL>color magenta, ASP123
ASP123> action> find> polar contacts> to any atoms
ASP123> action > find> polar contacts> within selection
PyMOL> wizard> measurement
PyMOL> label sele, resn, resi, name
