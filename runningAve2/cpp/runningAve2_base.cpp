#include "runningAve2_base.h"

/*******************************************************************************************

    AUTO-GENERATED CODE. DO NOT MODIFY

    The following class functions are for the base class for the component class. To
    customize any of these functions, do not modify them here. Instead, overload them
    on the child class

******************************************************************************************/

runningAve2_base::runningAve2_base(const char *uuid, const char *label) :
    Component(uuid, label),
    ThreadedComponent()
{
    loadProperties();

    input = new bulkio::InFloatPort("input");
    addPort("input", input);
    outMess = new MessageSupplierPort("outMess");
    addPort("outMess", outMess);
}

runningAve2_base::~runningAve2_base()
{
    delete input;
    input = 0;
    delete outMess;
    outMess = 0;
}

/*******************************************************************************************
    Framework-level functions
    These functions are generally called by the framework to perform housekeeping.
*******************************************************************************************/
void runningAve2_base::start() throw (CORBA::SystemException, CF::Resource::StartError)
{
    Component::start();
    ThreadedComponent::startThread();
}

void runningAve2_base::stop() throw (CORBA::SystemException, CF::Resource::StopError)
{
    Component::stop();
    if (!ThreadedComponent::stopThread()) {
        throw CF::Resource::StopError(CF::CF_NOTSET, "Processing thread did not die");
    }
}

void runningAve2_base::releaseObject() throw (CORBA::SystemException, CF::LifeCycle::ReleaseError)
{
    // This function clears the component running condition so main shuts down everything
    try {
        stop();
    } catch (CF::Resource::StopError& ex) {
        // TODO - this should probably be logged instead of ignored
    }

    Component::releaseObject();
}

void runningAve2_base::loadProperties()
{
    addProperty(runningAve,
                runningAve_struct(),
                "runningAve",
                "",
                "readwrite",
                "",
                "external",
                "message");

}


