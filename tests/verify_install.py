# verify_install.py: Solely to verify all modules and their respective versions
import sys
print("Python:", sys.version.splitlines()[0])

packages = ["numpy", "cv2", "torch", "ultralytics", "rplidar", "matplotlib", "pandas", "sklearn"]
for pkg in packages:
    try:
        module = __import__(pkg)
        print(f"{pkg}: OK (version: {getattr(module, '__version__', 'unknown')})")
    except Exception as e:
        print(f"{pkg}: FAILED -> {e}")
