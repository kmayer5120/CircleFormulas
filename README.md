# CircleFormulas
This was just some simple practice with creating Python command 
line programs that accept arguments.

To install as a script that can be run system wide:


    cat CircleFormulas.py > CircleFormulas

    chmod 774 CircleFormulas

    mv CircleFormulas /usr/local/bin


Then the script can be ran by calling it directly:


    CircleFormulas (formula arg) (radius)


Example commands are as follows:


    Volume:
        CircleFormulas -v 5

    

    Surface Area:
        CircleFormulas -sa 5


    Circumference:
        CircleFormulas -c 5



