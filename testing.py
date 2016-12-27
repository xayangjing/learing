#coding=gbk
'''This is testing scrtips for learning ucsmsdk'''


import csv
import tablib
import codecs
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucscoreutils import search_class_id


handle = UcsHandle("172.16.199.131", "config", "config")

handle.login()

print "login successfully"
#blade_mo = handle.query_classid(class_id="computeBlade", filter_str='(uuid,"1b4e28ba-2fa1-11d2-0202-b9a761bde3fb")')
#blade_parent_chindren = handle.query_children(in_mo=blade_mo.dn, class_id="EquipmentIOCard")
#print blade_parent_chindren
#mo = 'sys'
#mo_sys = handle.query_classid(class_id='networkElement')
#print mo_sys[0].serial


#blade_dict = handle.query_dns("sys/chassis-1/blade-1/board")
#print blade_dict.keys()
#blade_by_dn_children = handle.query_children(in_mo="blade-1", class_id='ProcessorUnit')
#for blade_child_object in blade_by_dn_children:
#    print blade_child_object.model
#for i in blade_dict:
#    print i
'''
# secrch detail info
mo = 'sys'
filter_str = '(dn,"%s")' % mo
mo_obj = handle.query_classid(class_id='ComputeBlade', filter_str=filter_str)
component_CPU = "ProcessorUnit"
component_DIMM = "MemoryUnit"




for i in mo_obj:
    filter_str = '(dn,"%s")' % i.dn
    blade_dn = i.dn + "/board/cpu-1"
    filter_str2 = '(dn,"%s" )' % (i.dn + "/board/cpu-1")
    mo_cpu = handle.query_classid(class_id=component_CPU, filter_str=filter_str2)
    mo_adaptor = handle.query_classid(class_id="adaptorUnit",filter_str=filter_str)
    filter_str_DIMM = '(dn,"%s", type="eq")' % (i.dn +"/board/memarray-1/mem-1" )
    print filter_str_DIMM
    mo_dimm = handle.query_classid(class_id= "MemoryUnit", filter_str=filter_str_DIMM)

    print mo_cpu[0].dn,mo_cpu[0].model,mo_adaptor[-1].model,mo_adaptor[-1].serial,mo_dimm[0]
'''
Inventory_keys = ['ComputeBlade','ProcessorUnit','EquipmentIOCard']
Inventory_dict = handle.query_classids(Inventory_keys[0],Inventory_keys[1],Inventory_keys[2])
i = 0
MO_blades = []
MO_ProcessorUnit =[]
MO_IOM = []
#print Inventory_dict
#while i < len(Inventory_dict[Inventory_keys[0]])-1
#    i += 1
#    blade = Inventory_dict[Inventory_keys[0]][i]
for blade in Inventory_dict['ComputeBlade']:
    t = blade.__dict__
    blade_info=[]
    for k in t:
        blade_info.append(t[k])
    print tuple(blade_info)
    MO_blades.append(tuple(blade_info))
MO_blades_heads = (blade.__dict__).keys()


for Processor in Inventory_dict['ProcessorUnit']:
    t = Processor.__dict__
    cpu_info=[]
    for k in t:
        cpu_info.append(t[k])
    print tuple(cpu_info)
    MO_ProcessorUnit.append(tuple(cpu_info))
MO_ProcessorUnit_heads = (Processor.__dict__).keys()


for IOM in Inventory_dict['EquipmentIOCard']:
    t = IOM.__dict__
    IOM_info=[]
    for k in t:
        IOM_info.append(t[k])
    print tuple(IOM_info)
    MO_IOM.append(tuple(IOM_info))
MO_IOM_heads = (IOM.__dict__).keys()

data = tablib.Dataset(*MO_ProcessorUnit,headers=MO_ProcessorUnit_heads)
#data = tablib.Dataset(*MO_blades,headers=MO_blades_heads)
#print data.csv
with open('csv.csv','w') as csvfile:
    csvfile.write(codecs.BOM_UTF8)
    csvfile.write(data.csv)
handle.logout()


print "logout UCS manager"

#headers = ('姓名', '年龄', '电话')
#data = [
#        ('小河','25','1234567'),
#        ('小芳','18','789456')
#        ]
#data = tablib.Dataset(*data, headers=headers)
#data.csv
#print data.csv
#with open('csv.csv','w') as csvfile:
#    csvfile.write(codecs.BOM_UTF8)
#    csvfile.write(data.csv)



#query_dict = {}
#    query_dict['chassis'] = {}
#    query_dict['fi'] = {}
#    query_dict['blade'] = {}
#
#query_data = handle.query_classids('orgOrg', 'EquipmentChassis', 'NetworkElement', 'ComputeBlade')
#for chassis in query_data['EquipmentChassis']:
#    query_dict['chassis'][chassis.dn] = {}
#    query_dict['chassis'][chassis.dn]['model'] = chassis.model
#    query_dict['chassis'][chassis.dn]['serial'] = chassis.serial
#for fi in query_data['NetworkElement']:
#    query_dict['fi'][fi.dn] = {}
#    query_dict['fi'][fi.dn]['model'] = fi.model
#    query_dict['fi'][fi.dn]['serial'] = fi.serial
#for blade in query_data['ComputeBlade']:
#    query_dict['blade'][blade.dn] = {}
#    query_dict['blade'][blade.dn]['model'] = blade.model
#    query_dict['blade'][blade.dn]['serial'] = blade.serial
