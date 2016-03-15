import WRF_Hydro_forcing as whf
import os
import re


def insert_text(base_dir):
    ''' Insert the copyright text (approved by NCAR General Counsel) into every
        script (NCL, Python, bash, etc.) that is found in a base directory and
        below.
    '''    

    copyright_text = "; 2015,2016@ University Corporation for Atmospheric Research"
    horizontal_bar = "; ----------------------------------------------------------"

    # Go through the base directory and traverse each subdirectory and for
    # each file, append with the copyright text at the top

    full_file_paths = get_filepaths(base_dir)
    for file in full_file_paths:
        print "file:  %s"%file
        sed_exe = "/bin/sed"
        tokens = (sed_exe, " -i -e ", "'1i", copyright_text, "\\' " ,file)
        cmd = "".join(tokens)
#        os.system(cmd)
        #add newlines
        tokens_top = (sed_exe," -i -e ", "'1i ",horizontal_bar,"\\' ", file)
        cmd_newline = "".join(tokens_top)
#        os.system(cmd_newline)
        tokens_bottom = (sed_exe," -i -e ", "'2a ",horizontal_bar,"\\' ", file)
        cmd_newline = "".join(tokens_bottom)
#        os.system(cmd_newline)

    

def get_filepaths(dir):
    """Generates the file names in a directory tree
       by walking the tree either top-down or bottom-up.
       For each directory in the tree rooted at
       the directory top (including top itself), it
       produces a 3-tuple: (dirpath, dirnames, filenames).

    Args:
        dir (string): The base directory from which we
                      begin the search for filenames.
    Returns:
        file_paths (list): A list of the full filepaths
                           of the data to be processed.


    """

    # Create an empty list which will eventually store
    # all the full filenames
    file_paths = []

    # Walk the tree
    for root, directories, files in os.walk(dir):
        for filename in files:
            # add it to the list only if it is a Python (.py), NCL (.ncl), or bash (.bash) file
            match = re.match(r'.*(py|nc|ncl|bash)$',filename)
            if match:
                # Join the two strings to form the full
                # filepath.
                filepath = os.path.join(root,filename)
                file_paths.append(filepath)
            else:
                continue
    return file_paths
    


if __name__ == "__main__":
    base_dir = "/home/minnawin/testdir"
    insert_text(base_dir)
