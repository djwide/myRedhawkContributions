#ifndef STRUCTPROPS_H
#define STRUCTPROPS_H

/*******************************************************************************************

    AUTO-GENERATED CODE. DO NOT MODIFY

*******************************************************************************************/

#include <ossie/CorbaUtils.h>
#include <CF/cf.h>
#include <ossie/PropertyMap.h>

struct runningAve_struct {
    runningAve_struct ()
    {
    };

    static std::string getId() {
        return std::string("runningAve");
    };

    float wavelength;
    float ave;
};

inline bool operator>>= (const CORBA::Any& a, runningAve_struct& s) {
    CF::Properties* temp;
    if (!(a >>= temp)) return false;
    const redhawk::PropertyMap& props = redhawk::PropertyMap::cast(*temp);
    if (props.contains("wavelength")) {
        if (!(props["wavelength"] >>= s.wavelength)) return false;
    }
    if (props.contains("ave")) {
        if (!(props["ave"] >>= s.ave)) return false;
    }
    return true;
}

inline void operator<<= (CORBA::Any& a, const runningAve_struct& s) {
    redhawk::PropertyMap props;
 
    props["wavelength"] = s.wavelength;
 
    props["ave"] = s.ave;
    a <<= props;
}

inline bool operator== (const runningAve_struct& s1, const runningAve_struct& s2) {
    if (s1.wavelength!=s2.wavelength)
        return false;
    if (s1.ave!=s2.ave)
        return false;
    return true;
}

inline bool operator!= (const runningAve_struct& s1, const runningAve_struct& s2) {
    return !(s1==s2);
}

#endif // STRUCTPROPS_H
