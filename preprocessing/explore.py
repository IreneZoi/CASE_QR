import h5py
import numpy as np
import sys



filename = sys.argv[1]


print(filename)

with h5py.File(filename, "r") as f:
        # List all groups
        #print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
    print(f['jet1_PFCands'][0])
