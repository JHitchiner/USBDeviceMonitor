#!/bin/python3

# Dont want to use too many external libs if I can help it
import lsusbParser
import datetime as dt
import time as t


def compareKnown(devices):
    print("[*] Comparing to known devices\n")

    # Import list of known "safe" device fingerprints
    with open('knownDevices.ids') as f:
        knownFingerprints = f.read()

    # For each devices, compare its vendorID ([2]) + productID([3]) to a list of known "safe" devices
    allKnown = True
    for d in devices:
        fingerprint = d[2]+":"+d[3]
        if(fingerprint not in knownFingerprints):
            allKnown = False
            print("[!] Unknown device detected")
            deviceInformation = lsusbParser.getDeviceInfo(d[0], d[1])
            print("  [-] Device: %s" % deviceInformation)
            print("  [-] Fingerprint: %s" % fingerprint)

    if(allKnown):
        print("[*] All devices are known\n")

def main():
    # Begin script
    time = dt.datetime.fromtimestamp(t.time()).strftime('%H:%M:%S %Y-%m-%d')
    print("[!] Starting USB bus scan %s\n" % time)

    # Get all devices using lsbusbParser class
    print("[*] Getting connected devices\n")
    devices, formatDevices = lsusbParser.getDevices()

    # Print some information
    numConnectedDevices = len(devices)
    count = 1
    print("[*] Devices connected: %d" % numConnectedDevices)
    for d in formatDevices:
        print("  [#%d] - %s"% (count, d.decode()))
        count+=1
    print()

    # Compare returned devices to a list of known or "safe" devices
    compareKnown(devices)


if __name__ == "__main__":
    main()
