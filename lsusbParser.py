#!/bin/python3

# Dont want to use too many external libs if I can help it
import subprocess
import re
import urllib.request

# Simple parser class for the standard "lsusb" command

def getDevices():

    # Get all devices connected
    # Returns a list of devices with each having the following:
    #   BusNumber (eg. 001)
    #   DeviceNumber (eg. 002)
    #   VendorID:DeviceID  (eg. 1d6b:0002)

    # Run command lsusb and save output
    out = subprocess.Popen(['lsusb'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()

    # If there is an error, output error and return an empty list
    if stderr != None:
        print(stderr)
        return []

    # Save a long list for printing out
    formatDevices = stdout.split(b'\n')[:-1]

    # Clean up list of devices (minus last one as it is a false positive, just an empty \n from console)
    stdout = stdout.split(b'\n')[:-1]
    deviceDescriptions = []
    for dev in stdout:
        deviceDescriptions.append(dev.decode("utf-8"))

    # Example of a deviceDescriptions object - "Bus 002 Device 002: ID 80ee:0021 VirtualBox USB Tablet"
    # Example of a devices object - ['002', '002', '80ee:0021']

    # Split up list of devices into key information and return it
    devices = []
    reg = re.compile('([0-9a-f]{4}|(\d\d\d))')
    # First condition matches the vendorID by looking for 4 hex characters in a row
    # Second condition matches busNumber and the deviceNumber by looking for 3 digits in a row
    # It will only take the first 4 matches of each line, as the vendor name might match in rare occasions
    for dev in deviceDescriptions:
        matches = re.findall(reg, dev)
        deviceInfo = [matches[0][0], matches[1][0], matches[2][0], matches[3][0]]
        devices.append(deviceInfo)

    return devices, formatDevices

# Get specific information on one device
def getDeviceInfo(deviceNum, busNum):
    # Run command lsusb -s deviceNum:busNum and return output
    # Add the -v flag to return verbose, might change later on if more info about a device is needed
    out = subprocess.Popen(['lsusb', '-s', deviceNum+':'+busNum], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    return stdout.decode().split('\n')[:-1][0]

def unbindDevice(deviceNum, busNum):
    # Unbind device
    # Will be useful for isolating unkown devices while they are being checked / vetted / added to whitelist
    print("todo")

def bindDevice(deviceNum, busNum):
    # Bind device
    # Will be useful for after a device is determined to be safe for connection
    print("todo")

# NOT CURRENTLY USED, BUT USEFUL IF I END UP USING THAT DATABASE
# Update usb.ids database
def getUSB_IDs():
    print("Updating usb.ids database...")
    # Downloads usb.ids to local directory, replacing an already existing one
    urllib.request.urlretrieve("http://www.linux-usb.org/usb.ids", "usb.ids")
