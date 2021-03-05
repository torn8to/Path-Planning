import numpy as np
import matplotlib.pyplot as plt
import math
import cv2 as cv
'''
obstacles are only going to intitially going to be circular
'''
class Obstacles:
    def __init__(self,XPos,Ypos, radius):
        self.xPos = XPos
        self.yPos = YPos
        self.radius = radius

    def inObject(self, xCoor, yCoor):
        pass



class Node:
    def __init__(self, xPos,yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.preceding = []
        self.children = []

        '''
        adds the pass to the list of varibles attached to the preceding
        its use cases is to put the previous Nodes to
        '''
    def AttachPreceding(self, preceding):
        self.preceding+= [preceding]

    def AttachChildren(self, child):
        self.children += [child]

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def getPreceding(self):
        return self.preceding

    def getChildren(self):
        return self.children

    def printPreceding(self):
        print(self.preceding)

    def printInfo(self):
        print(self)
        print("(x,y):(" + str(self.xPos)+","+ str(self.yPos)+")")
        print("Preceding:"+ str(self.preceding))
        print("Children:"+ str(self.children))

'''
end of the Node class
'''



''' uses the node class to find the "shortest path"'''
class djikstraDriver:
    def __init__(self,startingX, startingY,endingX,endingY):
        ''' use Area constraints'''
        self.leftXConstraint = 0
        self.rightXConstraint = 964
        self.topYConstraint = 0
        self.bottomYConstraint = 824
        #variables for starting and ending positions
        self.destinationReached = False
        self.startingX = startingX
        self.startingY = startingY
        self.endingX = endingX
        self.endingY = endingY
        self.obstacleList = []
        self.nodeList =[Node(self.startingX,self.startingY)]
        self.outerLayerStartingIndex = 0
        self.outerLayerEndingIndex = len(self.nodeList)
        self.distanceParameter = 5 #is the difference between each node point on top iteration
        self.iteration = 0
        self.minObstacleSize = self.distanceParameter+1 # the minimum size of an obbstacle that can be created


    def setStartingX(self,x):
        self.startingX = x


    def setStartingY(self,y):
        self.startingY = y

    def getEndXPosition(self):
        return self.endingX

    def getEndYPosition(self):
        return self.endingY

    def getNodeList(self):
        return self.nodeList

    def returnDestinationReached(self):
        return self.destinationReached

    def getPath(self):
        current = self.nodeList[len(nodeList)-1]
        path = []
        while !(currnet.getXPos() == self.startingX and current.getYPos == self.startingY);
            path += current
            current = current.getPreceding()
        current = current.getPreceding()
        path+=current
        return path




        '''
        Method header for a future iteration of the project when obstacles are involved
        '''
    def generateObstacles(self):
        pass


    def inBounds(self,xCoordinate,yCoordinate):
        return xCoordinate < self.rightXConstraint and xCoordinate >= self.leftXConstraint and yCoordinate >= self.topYConstraint and yCoordinate < self.bottomYConstraint


        ''' checks if coordinate overlaps with any obstacles'''
    def unobstructed(self,xCoordinate, yCoordinate):
        return True


        ''' checks to see if the coordinates passed are already in the node List'''
    def alreadyInList(self, xCoordinate , yCoordinate):
        for i in self.nodeList:
            if xCoordinate == i.getXPos() and yCoordinate == i.getYPos():
                return True
        return False


        ''' checks if the coordinates passed is inbounds and not overlapping with anyobject '''
    def isValid(self, xCoordinate, yCoordinate):
        return self.unobstructed(xCoordinate,yCoordinate) and self.inBounds(xCoordinate,yCoordinate) and not self.alreadyInList(xCoordinate,yCoordinate)

    ''' determines if the coordinates passed are with distance Parameter'''

    def isInRange(self,xCoordinate,yCoordinate):
        xCoordinate = xCoordinate - self.endingX
        yCoordinate = yCoordinate - self.endingY
        return (pow(xCoordinate,2)+pow(yCoordinate,2))<=(pow(self.distanceParameter,2))

    ''' prints all out the list of nodes used as a debug tool'''
    def printNodeList(self):
        for i in self.nodeList:
            i.printInfo()


        ''' method for debugging'''
    def checkForRepeats(self):
        for i in self.nodeList:
            for j in self.nodeList:
                if i != j and i.getXPos() == j.getXPos() and j.getYPos() == i.getYPos():
                    i.printInfo()
                    j.printInfo()
                    return True
        print(None)



        ''' goes through all and adds all push all new titles out to the'''
    def nextIteration(self):
        for i in range(self.outerLayerStartingIndex,self.outerLayerEndingIndex):
            currXpos = self.nodeList[i].getXPos()
            currYpos = self.nodeList[i].getYPos()

            '''checks if the endingPoint is with in the distance of the distanceparameter'''
            if self.isInRange(currXpos,currYpos):
                self.nodeList+=[Node(self.endingX,self.endingY)]
                self.nodeList[len(self.nodeList)-1].AttachPreceding(self.nodeList[i])
                self.nodeList[i].attachChildren(self.nodeList[len(self.nodeList)-1])
                self.destinationReached = True
                break

            ''' is add in nodes in spaces that valid placements'''
            if self.isValid(currXpos-self.distanceParameter,currYpos):
                self.nodeList+=[Node(currXpos-self.distanceParameter,currYpos)]
                self.nodeList[len(self.nodeList)-1].AttachPreceding(self.nodeList[i])
                self.nodeList[i].AttachChildren(self.nodeList[len(self.nodeList)-1])
            if self.isValid(currXpos,currYpos-self.distanceParameter):
                self.nodeList+=[Node(currXpos,currYpos-self.distanceParameter)]
                self.nodeList[len(self.nodeList)-1].AttachPreceding(self.nodeList[i])
                self.nodeList[i].AttachChildren(self.nodeList[len(self.nodeList)-1])
            if self.isValid(currXpos+self.distanceParameter,currYpos):
                self.nodeList+=[Node(currXpos+self.distanceParameter,currYpos)]
                self.nodeList[len(self.nodeList)-1].AttachPreceding(self.nodeList[i])
                self.nodeList[i].AttachChildren(self.nodeList[len(self.nodeList)-1])
            if self.isValid(currXpos,currYpos+self.distanceParameter):
                self.nodeList+=[Node(currXpos,currYpos+self.distanceParameter)]
                self.nodeList[len(self.nodeList)-1].AttachPreceding(self.nodeList[i])
                self.nodeList[i].AttachChildren(self.nodeList[len(self.nodeList)-1])

        self.outerLayerStartingIndex = self.outerLayerEndingIndex
        self.outerLayerEndingIndex = len(self.nodeList)
        self.iteration+=1
        return False


'''
End of the djikstra driver class
'''
'''
Global variables
all colors are stored in BGR values because thats how opencv does it
'''
checkedSpotColor = (227,245,64)
endPointColor =(227,0,200)
returnedShortestPathColor = (255,42,0)
driver = djikstraDriver(10,10,25,10)
img=  np.fill((1024,1024,3),255,np.uint8)


'''
Functions
'''
    ''' draws all the nodes already checked'''
def drawNodeList():
    if not driver.destinationReached():
        list = driver.getNodeList()
        for i in list:
            cv.rectangle(img,(i.getXpos-1,i.getYPos-1),(cv.getXPos+1, cv.getYPos+1),checkedSpotColor)
    else:
        drawPath()


def drawPath():
    list = driver.getPath()
    for i in list:
        cv.rectangle(img,(i.getXpos-1,i.getYPos-1),(cv.getXPos+1, cv.getYPos+1),checkedSpotColor)


'''
draws the end point
'''
def drawEndPoint():
    endingX = driver.getEndXPosition()
    endingY = driver.geEndYPosition()
    cv.rectangle(img,(endingX-1,EndingY-1),(endingX+1,endingY+1),endPointColor)

if __name__ == '__main__':
    cv.namedWindow('image')
    drawEndPoint()
    drawNodeList()
    while True:
        key = cv.waitKey(20)& 0xFF
