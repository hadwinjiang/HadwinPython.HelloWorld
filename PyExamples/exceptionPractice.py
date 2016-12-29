Raise an exception to interrupt program flow
Handle an exception to resume control
Unhandled exceptions will terminate the program
Exception objects contain information about the exceptional event

from exceptional import convert
convert("33")

def convert(s)
    '''Convert to an integer '''
    try:
        x = int(s)
    except ValueError:
        x = -1
    except TypeError:
        x = -1
    except (ValueError, TypeError):
        x = -1
    return x

Exceptions for programmer errors
    IndentationError
    SyntaxError
    NameError
try:
    x = int(s)
except (ValueError, TypeError) as e:
    print(str(e))
    pass
return x

from math import log
raise // reraise 

import os
p = '/path/to/datafile.dat'
if os.path.exists(p):
    process_file(p)
else:
    print('No such file as {}'.format(p))

import os
import sys
def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)

