#!/usr/bin/python2
import advertisement_pb2 as Ad
import json

"""
https://github.com/berezovskyi/protobuf-embedded-c
https://github.com/nanopb/nanopb
"""

eventList = Ad.ScanList()

js = open('input.json').read()

jlist = json.loads(js)

eventList.sourceID = jlist['sourceId']
eventList.timestamp = jlist['timestamp']
eventList.version = 3
eventList.sourceType = "GATEWAY"

for scan in jlist['events']:
    ad = eventList.ads.add()
    ad.connectable = scan['conn']
    ad.rssi = scan['rssi']
    ad.mac = scan['deviceAddress'].replace(':', '').decode('hex')
    if scan['srData']:
        ad.scan_response = scan['srData'].decode('base64')
    ad.data = scan['data'].decode('base64')
    ad.timestamp = scan['timestamp']
    ad.type = 0

length = len(eventList.SerializeToString())
print length, length / (len(jlist['events']) + 0.0)


f = open('proto.bin', 'w')
f.write(eventList.SerializeToString())
