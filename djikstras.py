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
        self.startingX = startingX
        self.startingY = startingY
        self.endingX = endingX
        self.endingY = endingY
        self.obstacles = []
        self.nodeList =[node(self.startingX,self.startingY)]
        self.outerLayerStartingIndex = 0
        self.outerLayerEndingIndex = len(nodeList)
        self.distanceParameter = 5 #is the difference between each node point on top iteration
        self.iteration = 0
        self.minObstacleSize = self.distanceParameter+1 # the minimum size of an obbstacle that can be created


        '''
        Method header for a future iteration of the project when obstacles are involved
        '''
    def generateObstacles(self):
        pass


    def inBounds(self,xCoordinate,yCoordinate):
        return xCoordinate < rightXConstraint and xCoordinate >= leftXconstraint and yCoordinate >= topYConstraint and yCoordinate < bottomYConstraint


        ''' checks if coordinate overlaps with any obstacles'''
    def unobstructed(self,xCoordinate, yCoordinate):
        return True


        ''' checks to see if the coordinates passed are already in the node List'''
    def alreadyInList(self, xCoordinate , yCoordinate):
        for i in nodeList:
            if xCoordinate == i.getXPos and yCoordinate == i.getYPos:
                return True
        return False


        ''' checks if the coordinates passed is inbounds and not overlapping with anyobject '''
    def isValid(self, xCoordinate, yCoordinate):
        return unobstructed(xCoordinate,yCoordinate) and inBounds(xCoordinate,yCoordinate) and not alreadyInList(xCoordinate,yCoordinate)

    ''' determines if the coordinates passed are with distance Parameter'''

    def isInRange(self,xCoordinate,yCoordinate):
        xCoordinate = xCoordinate - self.endingX
        yCoordinate = yCoordinate - self.endingY
        return pow(xCoordinate,2)+pow(yCoordinate,2)<=pow(self.distanceParameter,2)



        ''' goes through all and adds all push all new titles out to the'''
    def nextIteration(self):
        for i in range(self.outerLayerStartingIndex,self.outerLayerEndingIndex):
            currXpos = nodeList[i].getXPos()
            currYpos = nodeList[i].getYPos()

            '''checks if the endingPoint is with in the distance of the distanceparameter'''
            if isInrange(currXpos,currYpos):
                nodeList+=[Node(self.endingX,self.endingY)]
                nodeList[len(nodeList)-1].AttachPreceding(nodeList[i])
                nodeList[i].attachChildren(nodeList[len(nodeList)-1])
                break

            ''' is add in nodes in spaces that valid placements'''
            if isValid(currXpos-self.distanceParameter,currYpos):
                nodeList+=[Node(currXPos-self.distanceParameter,currYpos).]
                nodeList[len(nodeList)-1].AttachPreceding(nodeList[i])
                nodeList[i].AttachChildren(nodeList[len(nodeList)-1])
            if isValid(currXpos,currYpos-self.distanceParameter):
                nodeList+=[Node(currXpos,currYpos-self.distanceParameter)]
                nodeList[len(nodeList)-1].AttachPreceding(nodeList[i])
                nodeList[i].AttachChildren(nodeList[len(nodeList)-1])
            if isValid(currXpos+self.distanceParameter,currYpos):
                nodeList+=[Node(currXpos+self.distanceParameter,currYpos)]
                nodeList[len(nodeList)-1].AttachPreceding(nodeList[i])
                nodeList[i].AttachChildren(nodeList[len(nodeList)-1])
            if isValid(currXpos,currYpos+self.distanceParameter):
                nodeList+=[Node(currXpos,currYpos+self.distanceParameter)]
                nodeList[len(nodeList)-1].AttachPreceding(nodeList[i])
                nodeList[i].attachChildren(nodeList[len(nodeList)-1])

        self.outerLayerStartingIndex = self.outerLayerEndingIndex
        self.outerLayerEndingIndex = len(nodeList)
        self.iteration++




if __name__ == '__main__':
 img = np.full((820,820,3),255,np.uint8)
