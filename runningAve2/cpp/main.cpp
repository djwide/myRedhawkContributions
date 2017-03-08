#include <iostream>
#include "ossie/ossieSupport.h"

#include "runningAve2.h"
int main(int argc, char* argv[])
{
    runningAve2_i* runningAve2_servant;
    Component::start_component(runningAve2_servant, argc, argv);
    return 0;
}

