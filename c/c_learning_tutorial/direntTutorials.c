
// Include Headers: Include dirent.h for directory operations and stdio.h for standard input/output functions.

// Open Directory: Use opendir() to open the directory. Here, "." denotes the current directory. You can replace it with any directory path.

// Read Directory Entries: Use readdir() in a loop to read each entry in the directory. readdir() returns a pointer to a struct dirent representing the next directory entry or NULL if there are no more entries.

// Handle Errors: Check if opendir() or closedir() fails. Use perror() to print an error message.

// Close Directory: Use closedir() to close the directory stream after you’re done.
#include <stdio.h>
#include<dirent.h>
#include<errno.h>
int main(int argc, char const *argv[])
{
    DIR *dir;
    struct dirent *entry;
    dir = opendir("../.");
    if (dir==NULL)
    {
        perror("opendir");
    }
    while ((entry = readdir(dir))!=NULL)
    {
        printf("%s\n",entry->d_name);
    }
    
    
    return 0;
}


