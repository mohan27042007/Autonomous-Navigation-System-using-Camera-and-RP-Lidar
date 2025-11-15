from rplidar import RPLidar

PORT = 'COM3'  # use the new active port
lidar = RPLidar(PORT)
info = lidar.get_info()
print(info)
lidar.start_motor()  # Start scanning
for scan in lidar.iter_scans():
    print(scan)
    break  # Just get one scan for testing

lidar.stop()
lidar.disconnect()
