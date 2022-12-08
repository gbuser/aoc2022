import re
data = [x.rstrip() for x in open('data.txt', 'r')]


class dir:
    def __init__(self, parent, path):
        self.parent = parent
        self.size = 0
        self.path = path

#returns dir given its name
def find_dir(path, dirs):
    for dir in dirs:
        if dir.path == path: 
            return dir
    

directories = set()
directories.add(dir(None, 'root'))
cd = find_dir('root', directories)

#main loop: track the dir which is currently active. 
#at cd .. activate the parent
#at cd xxxx, change the active directory to current active  + /xxxx
#at dir xxxx, add a dir with path = current active + /xxxx to thge set of dirs. set parent to current active dir
#at ####, add #### to size of current active and each of its parents
for line in data[1:]:
    if line == '$ cd ..':
        cd = cd.parent
    elif line[:5] == '$ cd ':
        
        make_current = cd.path + '/' + line[5:]
        
        cd = find_dir(make_current, directories)
        
    
    elif line[:3] == 'dir':
        dir_name = line[4:]
        dir_path = cd.path + '/' + dir_name
        directories.add(dir(cd, dir_path))
        
        
    elif line[0].isdigit():
        size = int(line.split()[0])
        cd.size += size
        chain = cd
        while chain.parent:
            chain = chain.parent
            chain.size += size

 

needed = find_dir('root', directories).size - 40000000
sizes = [x.size for x in directories if x.size > needed]
sizes.sort()
print(sizes[0])
