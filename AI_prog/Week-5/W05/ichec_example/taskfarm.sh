# Each line is a shell command. If we need to run a few commands we
# can write this by hand. But if we are going to have many commands we
# might prefer to write a script to generate the lines.  Notice that
# we are using "> output_...dat" to *redirect the output* to that
# file.  Everything before ">" is a normal command.
python fruit_picking.py fruit_picking.dat 5 1 > output_5_1.dat
python fruit_picking.py fruit_picking.dat 5 2 > output_5_2.dat
python fruit_picking.py fruit_picking.dat 10 1 > output_10_1.dat
python fruit_picking.py fruit_picking.dat 10 2 > output_10_2.dat
