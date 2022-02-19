#!/usr/bin/python3
import os,sys

repos = {}
# In: github.com/filecoin-project/lotus
# Out: {"lotus":"github.com/filecoin-project/lotus"}
def makeRepos():
    with open("repo.lst","r") as f:
        for line in f.readlines():
            refined = line.strip("\n")
            items= refined.split("/")
            if len(items) != 3: continue
            repos[items[2]] = refined
    return repos

# Execute shell commands.
def runscript(script):
    if sys.version_info[0]<3:
        import commands
        result = commands.getstatusoutput(script).split("\n")
    else:
        import subprocess
        result = subprocess.getoutput(script).split("\n")
    return result

from config import rootdir
resultdir = os.path.abspath("results")
    
# Generate mod file by executing `git list -m all` in the corresponding directory.    
def generateMods():
    repos = makeRepos()
    if not os.path.exists(resultdir): return
    for key, value in repos.items():
        dirpath = os.path.join(rootdir,value)
        if not os.path.isdir(dirpath):
            approved=input("{0} not found. Do you want download it?(N/Y)".format(value))
            if 'Y' in approved:
                subpath=value[:-1*len(value.split("/")[2])]
                script="cd {0};git clone https://{1}; cd -".format(rootpath,value)
        modfile=os.path.join(dirpath,"go.mod")
        if not os.path.exists(modfile): continue
        #print(modfile)
        script="cd {0};go list -mod=readonly -m all >> {1}/{2}.lst; cd -".format(dirpath,resultdir,key)
        #print(script)
        runscript(script)

# Compare the dependencies of different repos, 
# then seek the common dependencies and,
# also find out the dependencies used by each repo respectively.
def analyze():
    if not os.listdir(resultdir): generateMods()
    if len(os.listdir(resultdir)) == 1: return
    modules_all = []
    moduledict={}
    for file in os.listdir(resultdir):
        if "own" in file: continue
        fullpath=os.path.join(resultdir,file)
        if not os.path.exists(fullpath): continue
        print(fullpath)
        modules = []
        with open(fullpath,"r") as f:
            for line in f.readlines():
                module = line.strip("\n").split()[0]
                modules.append(module)
                modules_all.append(module)
        moduledict[file.split(".")[0]] = modules
    # Counting module occurrences,
    # Show modules which are referenced by all.
    from collections import Counter
    occurrences = Counter(modules_all).most_common()
    print(occurrences)
    max_cnt = len(os.listdir(resultdir))
    commons = []
    for key,value in occurrences:
        if value == max_cnt: commons.append(key)
    list2file(os.path.join(resultdir,"common.lst"),commons) 
    # Show its own modules
    for key, value in moduledict.items():
        for common in commons: 
            value.remove(common)
        list2file(os.path.join(resultdir,"%s.own.lst"%key),value)

def list2file(filepath,values):
    with open(filepath, 'w') as output:
        for row in values:
            output.write(str(row) + '\n')

if __name__ == "__main__":
    analyze()
