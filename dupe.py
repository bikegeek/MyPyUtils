import re
import os
import shutil

'''Copies the nldas files from Feb 28 and renames them for
   files corresponding to Feb 29.
'''

def rename(fname,path):
    
    fname_end = "dist_params.nc"
    print ("fname: %s"%fname)
    print ("path: %s"%path)
    full_fname = path + "/" + fname

    #Obtain the list of files in the specified directory
    all_files = []
    new_name = "nldas2_0229" 

    #Walk the tree
    for root, directories, files in os.walk(path):
        for filename in files:
            #Consider this only if it corresponds to Feb28 data
            feb28 = re.match(r'nldas2_0228([0-9]{2}_dist_params.nc)',filename)
            if feb28:
                #copy and rename file to reflect Feb29
                new_fname = new_name + feb28.group(1)
                full_new = path + "/" + new_fname
                print ("new filename %s" % full_new)
                shutil.copy(full_fname, full_new)


   


fname = "nldas2_022820_dist_params.nc"
path = "/d8/hydro-dm/IOC/forcing_engine/weighting_files/bias_correction/nldas_climo"
rename(fname, path)

