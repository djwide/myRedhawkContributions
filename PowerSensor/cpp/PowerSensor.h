#ifndef POWERSENSOR_I_IMPL_H
#define POWERSENSOR_I_IMPL_H

#include "PowerSensor_base.h"

class PowerSensor_i : public PowerSensor_base
{
    ENABLE_LOGGING
    public:
        PowerSensor_i(const char *uuid, const char *label);
        ~PowerSensor_i();

        void constructor();

        int serviceFunction();
};

#endif // POWERSENSOR_I_IMPL_H
