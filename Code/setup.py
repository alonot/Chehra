import subprocess
import os
import sys
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict


# dependencies can be any iterable with strings,
# e.g. file line-by-line iterator
print("done")


dependencies = [
    'cmake==3.26.3',
    'opencv-python==4.7.0.72'
    'face-recognition==1.3.0'
]

# here, if a dependency is not met, a DistributionNotFound or VersionConflict
# exception is thrown.
try:
    pkg_resources.require(dependencies)
except DistributionNotFound or VersionConflict:
    os.system(
        'cmd /c "pip install -r requirements.txt"')
except Exception as e:
    print(e)

if not os.path.exists("known_faces"):
    os.mkdir("known_faces")

print("folder checked...")
