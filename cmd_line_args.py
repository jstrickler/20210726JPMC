
# C: int argc, char **argv
# Perl: @ARGV
import sys
print(sys.argv)  # list of args, including script name
print(sys.argv[0])   # name of script (foo.py)
print(sys.argv[1])   # "first" argument
print(len(sys.argv))
