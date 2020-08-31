# Project description

This project is focused on creating a USB device monitoring and assessment system.
Will be expanded to whole network and mainly focusing around IoT devices

Intended final use will be some sort of cronjob that runs the script once every 15 minutes or something, example command below:
python3 main.py > logFile.txt

# Dependencies:

(All main python libs)

subprocess
re
wget
datetime
time


# Notes about project

Finding it difficult to fingerprint USB devices, some dont have serial numbers etc.
Going to have to rely on VendorID+ProductID, this will mean it can only identify products,
not induvidual devices (although this should acheive the same result)

Current approach is focusing on creating a cataloug of known "safe" devices on a network / computer.
Another approach could be to create a blacklist of devices to avoid, but that would be less
effective in my opinion.

Developing in a virtual environment on a windows machine, so sometimes the USB stack on linux acts a bit weird and different

# Future features

- From here, potentially checking more metadata than just vendorID and productID to get an idea of the type of device
- Moving down the USB stack and not having to use the lsusb command
- Automatically unbind unidenfied devices until they are vetted? (unbind not disconnect, apparently a lot easier and less buggy)
  - Couple ways to do this ^, either de-authorize it by changing the value of /sys/bus/usb/devices/DEVICE/authorized or unbinding it
  - via /bus/usb/drivers/usb/bind and binding via /bus/usb/drivers/usb/unbind.
