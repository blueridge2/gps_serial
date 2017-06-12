#!/usr/bin/python
import serial
import re
def main():
    """
    main program for reading the pyserial port
    """
    print 'hi there'    
                                #   time  1            Latitude  2          3        longitude 4          ew 5    fix 6   sat 7       hdop 8            altidude 9     10     gs 11 12    u13      
    prog = re.compile("^\$GPGGA,([0-9]{1,6}.[0-9]{3}),([0-9]{1,4}.[0-9]{4}),([NS]),([0-9]{1,5}.[0-9]{4}),([EW]),([012]),([0-9]{1,3}),(\d\.\d{1,2}),(\d{1,10}\.\d{1,2}),(M),(-?)(\d{1,10}\.\d{1,2}),(M)")
    gps_serial_port = serial.Serial('/dev/ttyUSB0',9600,timeout=1)  # open serial port
    print(gps_serial_port.name)         # check which port was really used
    
    while(True):
        gps_output = gps_serial_port.readline()
        gps_output = gps_output[:-1]
        match = prog.match(gps_output)
        if match:
            print gps_output
            gps_time = match.group(1)
            gps_latitude = match.group(2)
            gps_ns = match.group(3)
            gps_longitude = match.group(4)
            gps_ew = match.group(5)
            gps_fix = match.group(6)
            gps_number_of_satelites = match.group(7)
            gps_hdop = match.group(8)
            gps_altitude = match.group(9)
            gps_alittude_units = match.group(10)
            gps_gs_sign = match.group(11)
            gps_gs      = match.group(12)
            gps_gs_units = match.group(13)
            print gps_time
            print gps_latitude
            print gps_ns
            print gps_longitude
            print gps_ew
            print gps_fix 
            print 'Number of satelites = {}'.format(gps_number_of_satelites)
            print 'hdop = {}'.format(gps_hdop)
            print 'altitude = {} meters'.format(gps_altitude)
            print 'Geoidal Separation = {}{} {}'.format(gps_gs_sign,gps_gs,gps_gs_units)
            print 
            #gps_hours = gps_time[0:2]
            #gps_minutes = gps_time[2:4]
            #gps_seconds = gps_time[4:6]
            #print '{} {} {}'.format(gps_hours,gps_minutes,gps_seconds)
            
            
            
    
    
    gps_serial_port.close()             # close port
    pass

if (__name__ == '__main__' ):
    main()
