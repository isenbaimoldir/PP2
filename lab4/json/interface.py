import json

with open('file.json') as file:
    json_file = json.load(file)

print("Interface status \n", "=" * 80)
print("{:<50s}{:<22s}{:<8s}{:<6s}".format("DN", "Description", "Speed", "MTU"))

imdatalist =  json_file.get("imdata", [])

for item in imdatalist:
    l1_phys_if = item.get("l1PhysIf", {})

    attributes = l1_phys_if.get("attributes", {})

    d = attributes.get("dn")
    description = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
    print("{:<50s}{:<22s}{:<8s}{:<6s}".format(d, description, speed, mtu))