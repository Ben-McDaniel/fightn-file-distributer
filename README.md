# fightn-file-distributer
A file distribution menace 

Depedencies/Setup\
-GitPython\
-Store credentials (https://git-scm.com/docs/git-credential-store) to allow auto pulling\
-Fix all paths defined in distributer.py\
-pull 'dispenser' repo\
-Add privateData.py file to local clone of fightn-file-distributer\
\
\




final structure\
\
->Pi running fightn-file-distributer(code for this stored in its own repo)\
\
->RHIT RM uploads github repo\
\
->Individual places to put files, ie. website github, grabcad, email to rm mailing list\
\
\
Process - User side\
Upload files to github within folders with their specified location\
in a max of 10 min they are uploaded to the correct places\
*possibly* recieve an email confirming their upload\
\
Process - Script Side\
Every 10 min check to see if new files have been uploaded \
if they have clone the RM Uploads repo\
parse directories for specific names \
->"website"\
->"grabcad"\
->"email"\
