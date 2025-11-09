
from rplidar import RPLidar, RPLidarException
import time

PORT = 'COM3'   

def main():
    try:
        lidar = RPLidar(PORT)
        info = lidar.get_info()
        print("LIDAR Info:", info)

        health = lidar.get_health()
        print("LIDAR Health:", health)

        # start motor and begin scanning
        lidar.start_motor()
        time.sleep(1)

        print("Starting live scan... (press Ctrl+C to stop)")
        for i, scan in enumerate(lidar.iter_scans()):
            print(f"Scan {i}: {len(scan)} points")
            if i >= 4:   # show 5 scans, then stop
                break

        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
        print("LIDAR stopped successfully.")

    except RPLidarException as e:
        print("RPLIDAR error:", e)
    except Exception as e:
        print("General error:", e)

if __name__ == "__main__":
    main()
