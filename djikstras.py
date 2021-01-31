import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
'''

'''


class Node:
    def __init__(self, xPos,yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.preceding = []
        self.children = []


    def AttachPreceding(self, preceding):
        self.preceding+= [preceding]


    def AttachChildren(self, child):
        self.children += [child]

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def printPreceding(self):
        print(self.preceding)

    def printInfo(self):
        print(self)
        print("(x,y):(" + str(self.xPos)+","+ str(self.yPos)+")")
        print("Preceding:"+ str(self.preceding))
        print("Children:"+ str(self.children))



''' uses the node class to find the "shortest path"'''
class djikstraDriver:
    def __init__(self,startingX, startingY,endingX,endingY):
        ''' use Area constraints'''
        self.leftXConstraint = 0
        self.rightXConstraint = 500
        self.topYConstraint = 0
        self.bottomYConstraint = 500

        #variables for starting and ending positions
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
                return True
        

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




if __name__ == '__main__':
    driver = djikstraDriver(10,10,25,10)
    driver.nextIteration()
    driver.nextIteration()
    driver.nextIteration()
\
