from sense_hat import SenseHat
import insertdatabase
import globals
import gyro3
import Arrows
sense=SenseHat()
sense.set_imu_config(False,False,True)
#globals.init()
while True:
    
    gyro3.gyro()
    insertdatabase.insert(globals.pitch,globals.roll,globals.yaw,globals.x,globals.y,globals.z)
    if (globals.pitch>90 and globals.pitch <270) or (globals.roll>90 and globals.roll <270):
        sense.set_pixels( Arrows.piros_x() )
    
    elif globals.pitch >40 and globals.pitch <90:
        sense.set_pixels( Arrows.nyil_balra())
       
    elif globals.pitch <320 and globals.pitch >270:
        sense.set_pixels( Arrows.nyil_jobbra())
        
    elif globals.roll >40 and globals.roll<90:
        sense.set_pixels( Arrows.nyil_felfele())
       
    elif globals.roll <320 and globals.roll >270:
        sense.set_pixels( Arrows.nyil_lefele())
    else:
        sense.set_pixels(Arrows.ures_matrix()) 
    print("p:{0},r:{1},y:{2},x:{3},y:{4},z:{5}".format(globals.pitch,globals.roll,globals.yaw,globals.x,globals.y,globals.z))
    