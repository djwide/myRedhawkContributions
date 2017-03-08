#include "PowerSensor_base.h"

/*******************************************************************************************

    AUTO-GENERATED CODE. DO NOT MODIFY

    The following class functions are for the base class for the component class. To
    customize any of these functions, do not modify them here. Instead, overload them
    on the child class

******************************************************************************************/

PowerSensor_base::PowerSensor_base(const char *uuid, const char *label) :
    Component(uuid, label),
    ThreadedComponent()
{
    loadProperties();

    dataFloat = new bulkio::InFloatPort("dataFloat");
    addPort("dataFloat", dataFloat);
    dataFloat_1 = new bulkio::OutFloatPort("dataFloat_1");
    addPort("dataFloat_1", dataFloat_1);
}

PowerSensor_base::~PowerSensor_base()
{
    delete dataFloat;
    dataFloat = 0;
    delete dataFloat_1;
    dataFloat_1 = 0;
}

/*******************************************************************************************
    Framework-level functions
    These functions are generally called by the framework to perform housekeeping.
*******************************************************************************************/
void PowerSensor_base::start() throw (CORBA::SystemException, CF::Resource::StartError)
{
    Component::start();
    ThreadedComponent::startThread();
}

void PowerSensor_base::stop() throw (CORBA::SystemException, CF::Resource::StopError)
{
    Component::stop();
    if (!ThreadedComponent::stopThread()) {
        throw CF::Resource::StopError(CF::CF_NOTSET, "Processing thread did not die");
    }
}

void PowerSensor_base::releaseObject() throw (CORBA::SystemException, CF::LifeCycle::ReleaseError)
{
    // This function clears the component running condition so main shuts down everything
    try {
        stop();
    } catch (CF::Resource::StopError& ex) {
        // TODO - this should probably be logged instead of ignored
    }

    Component::releaseObject();
}

void PowerSensor_base::loadProperties()
{
    addProperty(gain,
                "gain",
                "gain",
                "readwrite",
                "",
                "external",
                "property");

}


