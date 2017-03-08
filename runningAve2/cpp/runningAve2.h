#ifndef RUNNINGAVE2_I_IMPL_H
#define RUNNINGAVE2_I_IMPL_H

#include "runningAve2_base.h"

class runningAve2_i : public runningAve2_base
{
    ENABLE_LOGGING
    public:
        runningAve2_i(const char *uuid, const char *label);
        ~runningAve2_i();

        void constructor();

        int serviceFunction();
};

#endif // RUNNINGAVE2_I_IMPL_H
