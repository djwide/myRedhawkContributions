/*
Author:
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
*/
#include "PowerSensor.h"
#include <complex>
#include <cmath>
PREPARE_LOGGING(PowerSensor_i)

PowerSensor_i::PowerSensor_i(const char *uuid, const char *label) :
    PowerSensor_base(uuid, label)
{
    // Avoid placing constructor code here. Instead, use the "constructor" function.

}

PowerSensor_i::~PowerSensor_i()
{
}

void PowerSensor_i::constructor()
{
    /***********************************************************************************
     This is the RH constructor. All properties are properly initialized before this function is called
    ***********************************************************************************/
}


int PowerSensor_i::serviceFunction()
{
	//treat bulkio data type like an c vector.  The documentation is pretty lacking
    bulkio::InFloatPort::dataTransfer *tmp = dataFloat->getPacket(bulkio::Const::BLOCKING);
    tmp -> SRI.mode=1;
    if (not tmp) { // No data is available
    	return NOOP;
    }
	std::vector<float> output;

	output.resize(tmp->dataBuffer.size()/2);

	std::vector<float>* intermediate = (std::vector<float>*) &(tmp->dataBuffer);
	for (unsigned int i=0; i<tmp->dataBuffer.size()/2; i++) {
		output[i]= (float) sqrt(pow((*intermediate)[2*i],2)+ pow((*intermediate)[2*i+1],2));
		LOG_INFO(PowerSensor_i, output[i]);
	}

	tmp -> SRI.mode=0;
	if (tmp->sriChanged) {
		dataFloat_1->pushSRI(tmp->SRI);
	}

	dataFloat_1->pushPacket(output, tmp->T, tmp->EOS, tmp->streamID);


	delete tmp; // IMPORTANT: MUST RELEASE THE RECEIVED DATA BLOCK
    return NORMAL;

}

