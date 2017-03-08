#ifndef RUNNINGAVE2_BASE_IMPL_BASE_H
#define RUNNINGAVE2_BASE_IMPL_BASE_H

#include <boost/thread.hpp>
#include <ossie/Component.h>
#include <ossie/ThreadedComponent.h>

#include <bulkio/bulkio.h>
#include <ossie/MessageInterface.h>
#include "struct_props.h"

class runningAve2_base : public Component, protected ThreadedComponent
{
    public:
        runningAve2_base(const char *uuid, const char *label);
        ~runningAve2_base();

        void start() throw (CF::Resource::StartError, CORBA::SystemException);

        void stop() throw (CF::Resource::StopError, CORBA::SystemException);

        void releaseObject() throw (CF::LifeCycle::ReleaseError, CORBA::SystemException);

        void loadProperties();

    protected:
        // Member variables exposed as properties
        /// Message structure definition for runningAve
        runningAve_struct runningAve;

        // Ports
        /// Port: input
        bulkio::InFloatPort *input;
        /// Port: outMess
        MessageSupplierPort *outMess;

    private:
};
#endif // RUNNINGAVE2_BASE_IMPL_BASE_H
