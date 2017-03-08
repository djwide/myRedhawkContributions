#ifndef GPS_RECEIVER_BASE_IMPL_BASE_H
#define GPS_RECEIVER_BASE_IMPL_BASE_H

#include <boost/thread.hpp>
#include <ossie/Device_impl.h>
#include <ossie/ThreadedComponent.h>

#include "port_impl.h"
#include <bulkio/bulkio.h>

class GPS_Receiver_base : public Device_impl, protected ThreadedComponent
{
    friend class FRONTEND_GPS_In_i;

    public:
        GPS_Receiver_base(char *devMgr_ior, char *id, char *lbl, char *sftwrPrfl);
        GPS_Receiver_base(char *devMgr_ior, char *id, char *lbl, char *sftwrPrfl, char *compDev);
        GPS_Receiver_base(char *devMgr_ior, char *id, char *lbl, char *sftwrPrfl, CF::Properties capacities);
        GPS_Receiver_base(char *devMgr_ior, char *id, char *lbl, char *sftwrPrfl, CF::Properties capacities, char *compDev);
        ~GPS_Receiver_base();

        void start() throw (CF::Resource::StartError, CORBA::SystemException);

        void stop() throw (CF::Resource::StopError, CORBA::SystemException);

        void releaseObject() throw (CF::LifeCycle::ReleaseError, CORBA::SystemException);

        void loadProperties();

    protected:
        // Member variables exposed as properties
        /// Property: device_kind
        std::string device_kind;
        /// Property: device_model
        std::string device_model;
        /// Property: serial_port
        std::string serial_port;

        // Ports
        /// Port: gps
        FRONTEND_GPS_In_i *gps;
        /// Port: dataFloat
        bulkio::InFloatPort *dataFloat;

    private:
        void construct();
};
#endif // GPS_RECEIVER_BASE_IMPL_BASE_H
