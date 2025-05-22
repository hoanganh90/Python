# pdb: python debugger
# import pdb
import pdb
def add(a, b):
    # Set a trace point
    pdb.set_trace()
    return a + b
add(1, 2)
# pdb step  - Step into the function
# pdb next - Execute the next line of code
# pdb continue - Continue execution until the next breakpoint
# pdb break - Set a breakpoint
# pdb list - List source code around the current line
# pdb print - Print the value of a variable
# pdb where - Print the current stack trace