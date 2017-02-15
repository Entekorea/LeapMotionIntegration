#This File Collects Data on Hand Movement and Prints it to the WebGUI

leap = Runtime.start("leap","LeapMotion")
 
leap.addLeapDataListener(python)
 
def onLeapData(data):
  print (data.rightHand.index)
 
leap.startTracking()
