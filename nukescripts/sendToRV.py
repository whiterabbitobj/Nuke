def rvFinalCheck(nodelist):
    cmd = ['/Applications/RV64.app/Contents/MacOS/RV64']
    for node in nodelist:
        cmd.append(node['file'].value())
    cmd.append('-over')
    ocmd = ' '.join(cmd)
    subprocess.Popen(ocmd, shell=True)
