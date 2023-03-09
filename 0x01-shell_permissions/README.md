#0am_betty# script change the current user to betty

#1-who_am_i# script prints the effective username of the current user.

#2-groups# script prints all the groups the current user is part of.

#3-new_owner# script changes the owner of the file hello to the user betty

#4-empty# script  creates an empty file called hello

5-execute script adds execute permission to the owner of the file hello

6-multiple_permissions script adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody script adds execution permission to the owner, the group owner and the other users, to the file hello

8-James_Bond script ets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions

9-John_Doe script sets the mode of the file hello to this:

-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

10-mirror_permissions script sets the mode of the file hello the same as olleh’s mode.

The file hello will be in the working directory
The file olleh will be in the working directory

11-directories_permissions script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.


12-directory_permissions script creates a directory called my_dir with permissions 751 in the working directory.


13-change_group script changes the group owner to school for the file hello
