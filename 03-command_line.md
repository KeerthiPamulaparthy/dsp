# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >
pwd - prints the current directory
mkdir - create a new directory
cd - changes the current directory
ls - lists the current directory
rmdir - removes the directory specified
pushd - pushes current directory into a later directory
popd - jumps back to the starting directory
cp - copies the specified file
less - to view a file
man - to get help
grep - search for specified string

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
`ls`  - lists directory contents
`ls -a`  - lists directory contents including those beginning with a dot (.)
`ls -l`  -  lists directory contents in long format, including the total file size content
`ls -lh`  - lists directory contents in long format, with size specified as byte, kilobyte, megabyte, gigabyte or terabyte
`ls -lah`  -  lists directory contents in long format, with size specified as byte, kilobyte, megabyte, gigabyte or terabyte and specifies directory contents beginning with a (.)
`ls -t`  -  lists directory contents sorted in time modified order followed by sorting in  lexicographical order
`ls -Glp` - lists directory contents, with colorized output, in long listing, and with directories ending with a slash ('/')

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -l, ls -1, ls -R, ls -u,ls -t


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
xargs expects input from stdin and echo’s the output back
example: 
$ xargs
hi
good morning
cntrl+d
hi good morning

 

