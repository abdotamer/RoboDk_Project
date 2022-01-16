from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox

data = LoadList("my name.csv") #Reading the points from the CSV file

#Defining the Robot
RDK = Robolink()
robot = RDK.Item('',ITEM_TYPE_ROBOT)

#Defining the Engraving Frame and the Starting Point and Moving te robot to the starting position
frame = RDK.Item('Starting Frame')
target = RDK.Item('Engraving Target')
TarPose = target.Pose()
robot.setPoseFrame(frame)

#Asking the user to Check the tracing style to Line
RDK.ShowMessage('''PLease change the tracing style to Line
                    Go to: Tools -> Trace -> Style -> Line''')

#Moving the robot through the obtained points from the csv
for i in range(len(data)):
    TarPose.setPos(data[i])
    target.setPose(TarPose)
    
    #Activating the Trace if the engraving on the XY plan and Deactiviting the Trace otherwise 
    if (data[i][2] == 0 )and (data[i-1][2] ==0):
        RDK.Command("Trace", "On")
        robot.MoveL(target)
    else:
        RDK.Command("Trace", "Off")
        robot.MoveJ(target)
    if i == 0:
        RDK.Command("Trace", "Reset")


#Notifying the user that the engraving is done
RDK.ShowMessage("Done Engraving")

