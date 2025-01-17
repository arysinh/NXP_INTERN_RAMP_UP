import os
import shutil
from sys import argv


def copy_rec(dirname, cpdirname):
    for name in os.listdir(dirname):
        nme = name.split('.', 1)
        if os.path.isfile(dirname+'/'+name):
            shutil.copy(dirname+'/'+name, cpdirname+"/Copy_"+nme[0]+"_2"+
                        ("."+ nme[1] if len(nme)>1 else ""))
        else:
            os.mkdir(cpdirname+'/Copy_'+name+'_2')
            copy_rec(dirname+'/'+name, cpdirname+'/Copy_'+name+'_2')


if __name__ == "__main__":
    script, inp_dir, out_dir = argv
    copy_rec(inp_dir, out_dir)
