import h5py
import numpy as np
#filename = "/eos/uscms/store/user/izoi/CASE/BB_UL_MC_small_v2_splitsm/sideband/qcd/test/BB_batch0_side_qcd.h5"
#filename = "/eos/uscms/store/user/izoi/CASE/BB_UL_MC_small_v2_akcluster_splitsm/sideband/qcd/test/BB_batch0_side_qcd.h5"
filename = "qcdSigMCOrigReco_WpToBpT_Wp3000_Bp400_Top170_ZbtReco.h5"
weights = {}

keys = []

#jet_features_key = 'jet_kinematics'
#jet1_constituents_key = 'jet1_PFCands'
#jet2_constituents_key = 'jet2_PFCands'
dtype='float32'
print(filename)
with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    print(f["tpr"][()])
    print(f["tpr"].shape)
    features = np.asarray(f.get("tpr"))

    print( len(features))
    '''
    features = np.asarray(f.get(jet_features_key), dtype=dtype)
    constituents1 = np.asarray(f.get(jet1_constituents_key), dtype=dtype)
    constituents2 = np.asarray(f.get(jet2_constituents_key), dtype=dtype)
    print("features ",features[0])
    print("constituents1 ",constituents1[0])
    print("constituents2 ",constituents2[0])
    #sort by pt

    new1 = np.argsort((np.asarray(constituents1)[...,0])*(-1), axis=1)
    c_j1 = np.take_along_axis(np.asarray(constituents1), new1[...,None], axis=1)        

    new2 = np.argsort((np.asarray(constituents2)[...,0])*(-1), axis=1)
    c_j2 = np.take_along_axis(np.asarray(constituents2), new2[...,None], axis=1)        

    print("pt sorted constituents1 ",c_j1[0])
    print("pt sorted constituents2 ",c_j2[0])
    
    a = f['jet_kinematics'][()]
    print(a.shape)
    '''




    '''
    f.visit(keys.append) # append all keys to list
    for key in keys:
        print("Key: %s" % key)
        
        print(f[key].name)
    '''
        #weights[f[key].name] = f[key].value
    #print(weights)

    # Get the data
    #data = list(f[a_group_key])
    
    #print("data ")
    #print(data)