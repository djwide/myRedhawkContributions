#ifndef LOBREADER_I_IMPL_H
#define LOBREADER_I_IMPL_H

#include "lobReader_base.h"

class lobReader_i : public lobReader_base
{
    ENABLE_LOGGING
    public:
        lobReader_i(const char *uuid, const char *label);
        ~lobReader_i();

        void constructor();

        int serviceFunction();
};

#endif // LOBREADER_I_IMPL_H
