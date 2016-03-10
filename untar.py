import os
import sys
import re
import errno


def mkdir_p(dir):
    """Provide mkdir -p funtionality
    Args:
        dir (string): Full directory path to create if it doesn't exist
    Returns:
        None
    """
    
    try:
       os.makedirs(dir)
    except OSError as ose:
       if ose.errno == errno.EEXIST and os.path.isdir(dir):
           pass
       else:
           raise



def untar(tar_dir,target_dir):

    tar_files = os.listdir(tar_dir)

    for file in tar_files:
        match = re.search(r'.*.tar',file)
        print "file: %s"%file
        if match:
            tar_cmds = ("tar ", "-xvf ", tar_dir,"/",file, " -C ", target_dir)
            cmd = "".join(tar_cmds)
            print ("cmd: %s")%(cmd)
            os.system(cmd)
           

def gunzip_files(dir):
    """Unzip all the files in a given directory
       
       Args:
          dir (string): the full directory where the gzip'd files reside.
       Returns:
          None

    """
    
    gz_files = os.listdir(dir)
    print "gz_files: %s"%gz_files
    for gz in gz_files:
        unzip_cmds = ("gunzip ", dir,"/", gz,"/*")
        cmd = "".join(unzip_cmds)
        os.system(cmd)







if __name__ == "__main__":
    #Define the source of the tar'd data
    tar_dir = "/home/minnawin/test"

    #Define the target directory for the untar'd data              
    target_subdir = "data"

    target = (tar_dir, "/", target_subdir)
    target_dir = "".join(target)
    mkdir_p(target_dir)
    untar(tar_dir,target_dir)
    gunzip_files(target_dir)
