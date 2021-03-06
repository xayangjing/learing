# coding=gbk
'''This is testing scrtips for learning ucsmsdk'''


import csv
import tablib
import codecs
import time 
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucscoreutils import search_class_id
import csv2mysql

handle = UcsHandle("10.107.123.220", "config", "config")

handle.login()

print "login successfully"
Inventory_keys = ['ComputeBlade', 'ProcessorUnit', 'EquipmentIOCard',
                  'EquipmentFanModule', 'EquipmentPsu', 'EquipmentManufacturingDef',
                  'EquipmentChassis', 'NetworkElement', 'MgmtEntity', 'FabricVlan',
                  'MemoryUnit', 'StorageLocalDisk',
                  'LsServer', 'FaultInst', 'AaaModLR']
i = 0
for i in range(len(Inventory_keys)):
    Inventory_dict = handle.query_classids(Inventory_keys[i])
    collected_date = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
    MO_obj = []
    for blade in Inventory_dict[Inventory_keys[i]]:
        t = blade.__dict__
        t['collected_date']=collected_date
        MO_obj.append(tuple(t.values()))
    MO_obj_heads = t.keys()
    print 'collecting %s finished' % Inventory_keys[i]
    data = tablib.Dataset(*MO_obj, headers=MO_obj_heads)
    data.csv
    file_name = Inventory_keys[i] + '.csv'
    with open(file_name, 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8)
        csvfile.write(data.csv)
    print '%s data file created' % Inventory_keys[i]
    print 'Starting duemp files to DB'
handle.logout()


print "logout UCS manager"
