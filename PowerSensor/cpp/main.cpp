#include <iostream>
#include "ossie/ossieSupport.h"

#include "PowerSensor.h"
int main(int argc, char* argv[])
{
    PowerSensor_i* PowerSensor_servant;
    Component::start_component(PowerSensor_servant, argc, argv);
    return 0;
}

