from rplidar import RPLidar

PORT = 'COM3'  # use the new active port
lidar = RPLidar(PORT)
for i, scan in enumerate(lidar.iter_scans()):
    print(f"Scan {i}: {len(scan)} points")
    if i > 2:
        break
lidar.stop()
lidar.disconnect()
