#ifndef LOBREADER_BASE_IMPL_BASE_H
#define LOBREADER_BASE_IMPL_BASE_H

#include <boost/thread.hpp>
#include <ossie/Component.h>
#include <ossie/ThreadedComponent.h>

#include <ossie/MessageInterface.h>
#include "struct_props.h"

class lobReader_base : public Component, protected ThreadedComponent
{
    public:
        lobReader_base(const char *uuid, const char *label);
        ~lobReader_base();

        void start() throw (CF::Resource::StartError, CORBA::SystemException);

        void stop() throw (CF::Resource::StopError, CORBA::SystemException);

        void releaseObject() throw (CF::LifeCycle::ReleaseError, CORBA::SystemException);

        void loadProperties();

    protected:
        // Member variables exposed as properties
        /// Message structure definition for Compass
        Compass_struct Compass;

        // Ports
        /// Port: outMess
        MessageSupplierPort *outMess;

    private:
};
#endif // LOBREADER_BASE_IMPL_BASE_H
