from math import prod
import re


width = 101
height = 103

class Robot:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.x < 0:
            self.x = width + self.x
        if self.y < 0:
            self.y = height + self.y
        
        if self.x >= width:
            self.x = self.x - width
        if self.y >= height:
            self.y = self.y - height


robots = []
with open("2024/D14/input.txt") as inFile:
    robotStrs = [line.strip() for line in inFile.readlines()]

    for robotStr in robotStrs:
        pos, vel = robotStr.split()
        posX, posY = pos.replace("p=", "").split(",")
        velX, velY = vel.replace("v=", "").split(",")
        
        robots.append(Robot(int(posX), int(posY), (int(velX), int(velY))))


def robotsToString(robots: list):
    endStr = ""
    for i in range(width):
        for j in range(height):
            robotCount = 0

            for robot in robots:
                if robot.x == i and robot.y == j:
                    robotCount += 1
            
            if robotCount != 0:
                endStr += str(robotCount)
            else:
                endStr += "."
        endStr += "\n"
    return endStr



seconds = 10000
i = 7000
while i <= seconds:
    # print("Second", i)
    for robot in robots:
        robot.move()
        # print(robot.x, robot.y)

    # Count robots
    # counts = [0] * 4
    # halfWidth = width // 2
    # halfHeight = height // 2
    # for robot in robots:
    #     # Top Left
    #     if 0 <= robot.x < halfWidth and 0 <= robot.y < halfHeight:
    #         counts[0] += 1
        
    #     # Top Right
    #     if halfWidth < robot.x < width and 0 <= robot.y < halfHeight:
    #         counts[1] += 1

    #     # Bottom RIght
    #     if halfWidth < robot.x < width and halfHeight < robot.y < height:
    #         counts[2] += 1

    #     # Bottom Left
    #     if 0 <= robot.x < halfWidth and halfHeight < robot.y < height:
    #         counts[3] += 1


    if 7840 < i < 7850:
        print(robotsToString(robots))
        hello = re.findall(r"(\d{5})", robotsToString(robots))
        print(hello)
        if len(hello) > 5:
            # print(i, counts)
            # print(robotsToString(robots))
            break

    i += 1
    # if counts[0] > 250 or counts[1] > 250 or counts[2] > 250 or counts[3] > 250:

    
# print("Safety Factor:", prod(counts))
