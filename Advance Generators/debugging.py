# pdb: python debugger
# import pdb
import pdb
def add(a, b):
    # Set a trace point
    pdb.set_trace()
    return a + b
add(1, 2)
# pdb step
# pdb next
# pdb continue
# pdb list
# pdb print
# pdb where