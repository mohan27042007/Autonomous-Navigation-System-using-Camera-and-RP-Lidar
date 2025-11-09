
from rplidar import RPLidar
import matplotlib.pyplot as plt
import numpy as np
import time

PORT = 'COM3'   

def main():
    lidar = RPLidar(PORT)
    lidar.start_motor()
    time.sleep(1)

    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    print("Live visualization started. Close the plot window to stop.")
    try:
        for i, scan in enumerate(lidar.iter_scans()):
            ax.clear()
            angles = np.radians([x[1] for x in scan])
            distances = [x[2] for x in scan]
            ax.scatter(angles, distances, s=3)
            ax.set_title(f"RPLIDAR Live Scan #{i}")
            plt.pause(0.001)

            if i > 50:  # 50 iterations then stop automatically
                break

    except KeyboardInterrupt:
        print("Stopping visualization...")
    finally:
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
        plt.close()
        print("LIDAR disconnected.")

if __name__ == "__main__":
    main()
