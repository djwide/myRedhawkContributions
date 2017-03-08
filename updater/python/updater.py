'''
Author: 
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
'''

from ossie.resource import start_component
import logging
import math

from updater_base import *
class updater_i(updater_base):
    def constructor(self):
        self.port_fromReceiver.registerMessage("fromCentToUpdate", updater_base.FromCentToUpdate, self.messageReceived)
        self.xsize, self.ysize= 6, 6 #we used 100x 100 for our final product.  No noticeable slowdown
        self.array= [[0 for x in range(self.xsize)] for y in range(self.ysize)]
        
        
        
        self.p1, self.p2, self.p3=.01,.04,.04
        self.aRead1, self.aRead2, self.aRead3= math.pi/4, -math.pi/2, math.pi/2
        #should have longitude and latitude should be overwriteen if data is read in.  This is jsut an initial value
        self.sens1long, self.sens1lat= 41.39147, -73.95479
        self.sens2long, self.sens2lat= 41.39411, -73.95943
        self.sens3long, self.sens3lat= 41.39568, -73.95592
        self.gpsxl=41.39147
        self.gpsyd= -73.95943
        self.gpsxr= 41.39568
        self.gpsyu= -73.95479
        self.sens1x, self.sens1y= self.gpsToArray(41.39568, -73.95592)
        self.sens2x, self.sens2y= self.gpsToArray(41.39147, -73.95479)
        self.sens3x, self.sens3y= self.gpsToArray(41.39411, -73.95943)
        #Map Area
        GPSLATBOTTOM= min(self.gpsyd, self.gpsyu)
        GPSLONGLEFT= min(self.gpsxl, self.gpsxr)
        GPSLATTOP= max(self.gpsyd, self.gpsyu)
        GPSLONGRIGHT= max(self.gpsxl, self.gpsxr)
        self.xIntSize=(GPSLONGRIGHT-GPSLONGLEFT)/self.xsize
        self.yIntSize=(GPSLATTOP-GPSLATBOTTOM)/self.xsize
        # TODO add customization here.
        
    def messageReceived(self, msgId, msgData):
        #update map function call
        #logging.info(str(self.p1) + " "+ str(self.sens1x) +" " + str(self.sens1y)+" "+ str(self.sens1long) +" " + str(self.sens1lat))
        #logging.info(str(self.p2) + " "+ str(self.sens2x) +" " + str(self.sens2y)+ " "+ str(self.sens2long) +" " + str(self.sens2lat))
        #logging.info(str(self.p3) + " "+ str(self.sens3x) +" " + str(self.sens3y)+ " "+ str(self.sens3long) +" " + str(self.sens3lat))
        
        #logging.info(msgData.aveUp1)
        self.p1, self.p2, self.p3= msgData.aveUp1, msgData.aveUp2, msgData.aveUp3 #
        self.aRead1, self.aRead2, self.aRead3= msgData.lobUp1, msgData.lobUp2, msgData.lobUp3
        self.sens1long, self.sens1lat= msgData.long1, msgData.lat1
        self.sens2long, self.sens2lat= msgData.long2, msgData.lat2
        self.sens3long, self.sens3lat= msgData.long3, msgData.lat3
        '''self.sens1x, self.sens1y= self.gpsToArray(self.sens1long, self.sens1lat)
        self.sens2x, self.sens2y= self.gpsToArray(self.sens2long, self.sens2lat)
        self.sens3x, self.sens3y= self.gpsToArray(self.sens3long, self.sens3lat)
        for when I get lob
        '''
        self.pdoa();
            
    def process(self):
        message= updater_base.FromUpToInsert()
        arrX, arrY= self.greatestLoc()
        logging.info(str(arrX)+ " " +str(arrY))
        temp= self.arrayToGPS(arrX, arrY)
        message.X= temp[0]
        message.Y= temp[1]
        logging.info(temp)
        self.port_toDB.sendMessage(message)
        return NOOP
    
    def gpsToArray(self, longi, lat):
        return int(self.xsize*(longi-self.gpsxl)/(self.gpsxr-self.gpsxl)+.5),int(self.ysize*(lat-self.gpsyd)/(self.gpsyu-self.gpsyd)+.5)
    
    def arrayToGPS(self, x,y):
        return (x*self.xIntSize+self.gpsxl,y*self.yIntSize+self.gpsyd)
        
    def pdoa(self):
        #http://cradpdf.drdc-rddc.gc.ca/PDFS/unc110/p534968_A1b.pdf
        #I used the method on pdf page 33
        alpha= .1 #2 to 4 where 2 is free space.  Iused .1 because it gave a good demonstrable result for projects day
        # distance ratios
        d12= pow(10, -(self.p1-self.p2)/(10*alpha))#p1 is unpacked power reading
        d23= pow(10, -(self.p2-self.p3)/(10*alpha))
        d31= pow(10, -(self.p3-self.p1)/(10*alpha))
        logging.info(str(self.p1)+ str(self.p2))
        x1, x2, x3, y1, y2, y3= self.sens1x, self.sens2x, self.sens3x, self.sens1y,self.sens2y, self.sens3y; 
        c1 = self.circleCenters(x1, y1, x2, y2, d12)
        c2 = self.circleCenters(x2, y2, x3, y3, d23)
        c3 = self.circleCenters(x3, y3, x1, y1, d31)
        
        rc1= self.radEqn(x1,y1,x2,y2,d12)
        rc2= self.radEqn(x2,y2, x3, y3, d23)
        rc3= self.radEqn(x3, y3,x1,y1,d31)
        totalSum=0
        for x in range(0, self.xsize):
            for y in range(0,self.ysize):
                temp= self.intensity((x,y), c1[0], c1[1],rc1)*self.intensity((x,y), c2[0], c2[1],rc2)*self.intensity((x,y), c3[0], c3[1],rc3)
                self.array[x][y]= temp
                totalSum= temp
        for x in self.array:
            logging.info(x)
        logging.info(" ")
        # you can normalize the heatmap or not.  Normalize make the total of all values 1 and can represnt a 
        # probability the enemy is in a location.  If you don't normalize the values will be relative to one another
        # so you can still fin the most likely location just by looking at greatestLoc 
        return self.normalize(totalSum)#self.array #
    
    #join methods for efficiency
    def radEqn(self,x1, y1, x2, y2, d):
        return pow(pow((x1-x2*d*d)/(d*d-1.001),2)+pow((y1-y2*d*d)/(d*d-1.001),2)-(d*d*x2*x2+d*d*y2*y2-x1*x1-y1*y1)/(d*d-1.001),.5)
    
    def circleCenters(self,x1, y1, x2, y2, d):
        return (x2*d*d-x1)/(d*d-1.001),(y2*d*d-y1)/(d*d-1.001)
    
    def distance(self, x0, y0, x1, y1): return math.sqrt((x0-x1)**2+(y0-y1)**2)
    

    def intensity(self,reading, x,y, distanceFromSource):
        return math.tanh(1/(.003+math.pow((distanceFromSource-self.distance(reading[0], reading[1],x,y)),2)))
    
    #merge with pdoa for efficiency
    def aoa(self):
        arraySum=0
        x1, x2, x3, y1, y2, y3= self.sens1x, self.sens2x, self.sens3x, self.sens1y,self.sens2y, self.sens3y; 
        for x in range(0, self.xsize):
            for y in range(0,self.ysize):
                aActual1= self.angleSignTrans(y,y1,x,x1)
                aActual2= self.angleSignTrans(y,y2,x,x2)
                aActual3= self.angleSignTrans(y,y3,x,x3)
                readingCloseness1= (math.pi- self.radialDistance(self.aRead1,aActual1))/math.pi
                readingCloseness2= (math.pi- self.radialDistance(self.aRead2,aActual2))/math.pi
                readingCloseness3= (math.pi- self.radialDistance(self.aRead3,aActual3))/math.pi
                self.array[x][y]= readingCloseness1*readingCloseness2*readingCloseness3    
                arraySum+= self.array[x][y]
        for x in self.array:
            logging.info(x)
        logging.info(" ")
        return self.array#normalize(arraySum, array)
    
    def angleSignTrans(self,y,yRead,x,xRead):
        if(y>yRead and x>xRead):
            return math.atan((y-yRead)/(x-xRead))
        elif(y>yRead and x<xRead):
            return math.pi+math.atan((y-yRead)/(x-xRead))
        elif(y<yRead and x>xRead):
            return math.atan((y-yRead)/(x-xRead))
        else:
            return -(math.pi-math.atan((y-yRead)/(x-xRead)))
        
    def radialDistance(self,x, y): #critical, accounts for discontinuities in arctan
        dist= math.fabs(x-y)%(2*math.pi)
        if(dist>math.pi): return 2*math.pi- dist
        return dist
    
    def normalize(self,totalP):
        for x in range(self.xsize):
            for y in range(self.ysize):
                self.array[x][y]=self.array[x][y]/totalP
        #self.maxHMVal= self.maxHMVal/totalP
        return self.array
    
    def greatestLoc(self):
        maxProb, maxX, maxY= -1,-1,-1
        for x in range(self.xsize):
            for y in range(self.ysize):
                if(self.array[x][y]>maxProb):
                    maxProb= self.array[x][y]
                    maxX= x
                    maxY= y
        return maxX, maxY
    
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(updater_i)

