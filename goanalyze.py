#!/usr/bin/python3
import os,sys

repos = {}
def makeRepos():
    with open("repo.lst","r") as f:
        for line in f.readlines():
            refined = line.strip("\n")
            items= refined.split()
            if len(items) < 2: continue
            repos[items[0]] = items[1]
    return repos

def runscript(script):
    if sys.version_info[0]<3:
        import commands
        result = commands.getstatusoutput(script).split("\n")
    else:
        import subprocess
        result = subprocess.getoutput(script).split("\n")
    return result

rootdir = "/home/frank/Code"#"/media/gustav/Investigation"
resultdir = os.path.abspath("results")
    
def generateMods():
    repos = makeRepos()
    if not os.path.exists(resultdir): return
    for key, value in repos.items():
        
        dirpath = os.path.join(rootdir,value)
        if not os.path.isdir(dirpath): continue
        modfile=os.path.join(dirpath,"go.mod")
        if not os.path.exists(modfile): continue
        print(modfile)
        script="cd {0};go list -mod=readonly -m all >> {1}/{2}.lst; cd -".format(dirpath,resultdir,key)
        print(script)
        runscript(script)

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
    # print(occurrences)
    max_cnt = len(os.listdir(resultdir))
    commons = []
    for key,value in occurrences:
        if value == max_cnt: commons.append(key)
    # Show its own modules
    for key, value in moduledict:
        for common in commons: value.remove()
        with open(os.path.join(resultdir,"%s.own.lst"%key), "wb") as fp:
             import pickle
             pickle.dump(value,fp)

if __name__ == "__main__":
    analyze()