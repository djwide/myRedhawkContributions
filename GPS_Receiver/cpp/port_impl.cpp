/*******************************************************************************************

    AUTO-GENERATED CODE. DO NOT MODIFY

    Source: GPS_Receiver.spd.xml

*******************************************************************************************/

#include "GPS_Receiver.h"

// ----------------------------------------------------------------------------------------
// FRONTEND_GPS_In_i definition
// ----------------------------------------------------------------------------------------
FRONTEND_GPS_In_i::FRONTEND_GPS_In_i(std::string port_name, GPS_Receiver_base *_parent) : 
Port_Provides_base_impl(port_name)
{
    parent = static_cast<GPS_Receiver_i *> (_parent);
}

FRONTEND_GPS_In_i::~FRONTEND_GPS_In_i()
{
}

FRONTEND::GPSInfo* FRONTEND_GPS_In_i::gps_info()
{
    boost::mutex::scoped_lock lock(portAccess);
    FRONTEND::GPSInfo_var retval = new FRONTEND::GPSInfo();
    // TODO: Fill in this function
    return retval._retn();
}

void FRONTEND_GPS_In_i::gps_info(const FRONTEND::GPSInfo& data)
{
    boost::mutex::scoped_lock lock(portAccess);
    // TODO: Fill in this function
}

FRONTEND::GpsTimePos* FRONTEND_GPS_In_i::gps_time_pos()
{
    boost::mutex::scoped_lock lock(portAccess);
    FRONTEND::GpsTimePos_var retval = new FRONTEND::GpsTimePos();
    // TODO: Fill in this function
    return retval._retn();
}

void FRONTEND_GPS_In_i::gps_time_pos(const FRONTEND::GpsTimePos& data)
{
    boost::mutex::scoped_lock lock(portAccess);
    // TODO: Fill in this function
}

std::string FRONTEND_GPS_In_i::getRepid() const
{
    return "IDL:FRONTEND/GPS:1.0";
}


