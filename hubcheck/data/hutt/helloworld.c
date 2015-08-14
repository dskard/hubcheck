#include "rappture.h"
#include <stdio.h>

int main(int argc, char * argv[]) {

    RpLibrary* lib    = NULL;
    const char* data  = NULL;

    // create a rappture library from the file filePath
    lib = rpLibrary(argv[1]);

    if (lib == NULL) {
        // cannot open file or out of memory
        printf("FAILED creating Rappture Library\n");
        return(1);
    }

    rpGetString(lib,"input.string(name).current",&data);
    rpPutString(lib,"output.string(helloworld).current","hello ",RPLIB_APPEND);
    rpPutString(lib,"output.string(helloworld).current",data,RPLIB_APPEND);

    rpResult(lib);
    return 0;
}
