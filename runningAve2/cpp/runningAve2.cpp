/*
Author:
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
*/
#include "runningAve2.h"

PREPARE_LOGGING(runningAve2_i)

runningAve2_i::runningAve2_i(const char *uuid, const char *label) :
    runningAve2_base(uuid, label)
{
    // Avoid placing constructor code here. Instead, use the "constructor" function.

}

runningAve2_i::~runningAve2_i()
{
}

void runningAve2_i::constructor()
{
    /***********************************************************************************
     This is the RH constructor. All properties are properly initialized before this function is called 
    ***********************************************************************************/
}

int runningAve2_i::serviceFunction()
{
	bulkio::InFloatPort::dataTransfer *tmp = input->getPacket(bulkio::Const::BLOCKING);

	if (not tmp) { // No data is available
		return NOOP;
	}
	float THRESHOLD= 0;//If you think that only power readings above a certain level should be taken into account
	float recentAve=0;
	float runningAverage=0;
	float poppedVal=0;
	float recentInpTotal=0;
	int runningAveSize=99;

	std::vector<float>* intermediate = (std::vector<float>*) &(tmp->dataBuffer);

	for (unsigned int i=0; i<tmp->dataBuffer.size()/2-1; i++) {
		recentInpTotal += (*intermediate)[i];//
	}
	//determine the average of the recently input string of power readings
	recentAve= recentInpTotal/(*intermediate).size();

	//use queue as baseline for the running average.  Values in one end and out the other
	std::queue<float> aveQueue;
	aveQueue.push(recentAve);
	int size= aveQueue.size();
	if(aveQueue.size() > runningAveSize){
		poppedVal= aveQueue.front();
		aveQueue.pop();
		runningAverage = (recentAve-poppedVal + (size-1)*runningAverage)/(size-1);
	}//alternate case until Queue is completely full below
	else{
		runningAverage = (recentAve + (size-1)*runningAverage)/(size);
	}
	if (runningAverage> THRESHOLD){
		runningAve_struct message;
		message.ave= runningAverage;
		message.wavelength= 462.52; //depends on what freq you are reading at
		this-> outMess-> sendMessage(message);
	}
	return NOOP;
}

