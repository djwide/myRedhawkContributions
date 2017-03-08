#ifndef PORT_H
#define PORT_H

#include <boost/thread/locks.hpp>
#include <ossie/Port_impl.h>
#include <FRONTEND/GPS.h>

class GPS_Receiver_base;
class GPS_Receiver_i;

#define CORBA_MAX_TRANSFER_BYTES omniORB::giopMaxMsgSize()

// ----------------------------------------------------------------------------------------
// FRONTEND_GPS_In_i declaration
// ----------------------------------------------------------------------------------------
class FRONTEND_GPS_In_i : public POA_FRONTEND::GPS, public Port_Provides_base_impl
{
    public:
        FRONTEND_GPS_In_i(std::string port_name, GPS_Receiver_base *_parent);
        ~FRONTEND_GPS_In_i();

        FRONTEND::GPSInfo* gps_info();
        void gps_info(const FRONTEND::GPSInfo& data);
        FRONTEND::GpsTimePos* gps_time_pos();
        void gps_time_pos(const FRONTEND::GpsTimePos& data);
        std::string getRepid() const;

    protected:
        GPS_Receiver_i *parent;
        boost::mutex portAccess;
};
#endif // PORT_H
