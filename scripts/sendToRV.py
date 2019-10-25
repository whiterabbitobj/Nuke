import subprocess
import os

def sendToRV(nodelist, mode=''):
    cmd = os.environ['RV_VER']
    for node in nodelist:
        cmd.append(node['file'].value())
    if mode=='over':
        cmd.append('-over')
    ocmd = ' '.join(cmd)
    subprocess.Popen(ocmd, shell=True)
