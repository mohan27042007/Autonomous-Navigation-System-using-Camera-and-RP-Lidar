from rplidar import RPLidar
import time

lidar = RPLidar('COM3')
lidar.start_motor()

time.sleep(3)   # let it spin up

for i in range(10):
    try:
        info = lidar.get_info()
        health = lidar.get_health()
        print(info, health)
        break
    except Exception as e:
        print("Read failed:", e)

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
