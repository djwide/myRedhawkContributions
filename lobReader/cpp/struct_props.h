#ifndef STRUCTPROPS_H
#define STRUCTPROPS_H

/*******************************************************************************************

    AUTO-GENERATED CODE. DO NOT MODIFY

*******************************************************************************************/

#include <ossie/CorbaUtils.h>
#include <CF/cf.h>
#include <ossie/PropertyMap.h>

struct Compass_struct {
    Compass_struct ()
    {
    };

    static std::string getId() {
        return std::string("Compass");
    };

    float compass;
    float aoa;
};

inline bool operator>>= (const CORBA::Any& a, Compass_struct& s) {
    CF::Properties* temp;
    if (!(a >>= temp)) return false;
    const redhawk::PropertyMap& props = redhawk::PropertyMap::cast(*temp);
    if (props.contains("compass")) {
        if (!(props["compass"] >>= s.compass)) return false;
    }
    if (props.contains("aoa")) {
        if (!(props["aoa"] >>= s.aoa)) return false;
    }
    return true;
}

inline void operator<<= (CORBA::Any& a, const Compass_struct& s) {
    redhawk::PropertyMap props;
 
    props["compass"] = s.compass;
 
    props["aoa"] = s.aoa;
    a <<= props;
}

inline bool operator== (const Compass_struct& s1, const Compass_struct& s2) {
    if (s1.compass!=s2.compass)
        return false;
    if (s1.aoa!=s2.aoa)
        return false;
    return true;
}

inline bool operator!= (const Compass_struct& s1, const Compass_struct& s2) {
    return !(s1==s2);
}

#endif // STRUCTPROPS_H
