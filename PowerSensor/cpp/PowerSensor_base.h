#ifndef POWERSENSOR_BASE_IMPL_BASE_H
#define POWERSENSOR_BASE_IMPL_BASE_H

#include <boost/thread.hpp>
#include <ossie/Component.h>
#include <ossie/ThreadedComponent.h>

#include <bulkio/bulkio.h>

class PowerSensor_base : public Component, protected ThreadedComponent
{
    public:
        PowerSensor_base(const char *uuid, const char *label);
        ~PowerSensor_base();

        void start() throw (CF::Resource::StartError, CORBA::SystemException);

        void stop() throw (CF::Resource::StopError, CORBA::SystemException);

        void releaseObject() throw (CF::LifeCycle::ReleaseError, CORBA::SystemException);

        void loadProperties();

    protected:
        // Member variables exposed as properties
        /// Property: gain
        short gain;

        // Ports
        /// Port: dataFloat
        bulkio::InFloatPort *dataFloat;
        /// Port: dataFloat_1
        bulkio::OutFloatPort *dataFloat_1;

    private:
};
#endif // POWERSENSOR_BASE_IMPL_BASE_H
