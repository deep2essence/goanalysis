## 1. generate deps.lst
- run go list -m all in your target repo to get a list of dependencies.
```
[go]
cd $repopath
go list -m list >> deps.lst

[node]

```
## 2. generate path.lst from deps.lst
```

```
## 3. zip multiple directories
```
tar -c zip_file_name.tar.gz -C path1 path2 path3
```