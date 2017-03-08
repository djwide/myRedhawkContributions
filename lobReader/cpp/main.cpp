#include <iostream>
#include "ossie/ossieSupport.h"

#include "lobReader.h"
int main(int argc, char* argv[])
{
    lobReader_i* lobReader_servant;
    Component::start_component(lobReader_servant, argc, argv);
    return 0;
}

