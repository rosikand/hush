# 🔑 Hush: CLI Password Manager

Hush is a simple password manager powered through the command line. The password database itself is stored locally in `./passwords.csv`. The python script that powers the program is `hush.py`. 

## Example 

```
$ python3 hush.py
    1. make pasta
    Number of items: 1
$ python3 hush.py delete 3
$ python3 hush.py add

```

## Installation 

Clone/download this repo. `cd` into the directory whenever you want to use hush. Then run the python script, specifying your desired arguments (see below for the choices). A more advanced setup would be to set up a shell command shortcut that runs the program from anywhere on your computer (i.e. run from the root directory). That way, you can do things like `h`, `h add`, `h delete 3` no matter where you are. 

## Reference 

```
$ python3 hush.py 
	prints database 
$ python3 hush.py add
	for adding an entry to the db. Sets up an interpreter where you
	can type/paste the information for each field in the db.  
$ python3 hush.py show
	same functionality as python3 hush.py 
$ python3 hush.py len
	prints the total number of entries in the db 
$ python3 hush.py delete <query (int)>
	deletes the entry at index <query (int)> in the db. 
```

The following argument abreviations are supported: 

- `add` --> `a`
- `len` --> `l`
- `delete` --> `d`

## Roadmap 

- Implement `hush.search`. 
- Implement encryption on the `passwords.csv` database. 
