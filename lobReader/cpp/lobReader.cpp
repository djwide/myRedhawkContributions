/*
Author:
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
*/
// This component is a shell for determining line of bearing.  This will interface with the pseudo doppler
#include "lobReader.h"
#include <math.h>

PREPARE_LOGGING(lobReader_i)

lobReader_i::lobReader_i(const char *uuid, const char *label) :
    lobReader_base(uuid, label)
{
    // Avoid placing constructor code here. Instead, use the "constructor" function.

}

lobReader_i::~lobReader_i()
{
}

void lobReader_i::constructor()
{
    /***********************************************************************************
     This is the RH constructor. All properties are properly initialized before this function is called 
    ***********************************************************************************/
}

        

int lobReader_i::serviceFunction()
{
	Compass_struct message;
	message.aoa= M_PI/2;//(-M_PI,M_PI)
	message.compass= 0;//direction of straight north
	this-> outMess-> sendMessage(message);
    return NOOP;
}

