def python():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/Google\ Drive/Software/Python'])

def terminal():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/'])

def same_terminal():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ./'])
