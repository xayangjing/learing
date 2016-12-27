import csv
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucscoreutils import search_class_id

handle = UcsHandle("172.16.199.131", "config", "config")

data =[]
handle.login()
print "login successfully"
mo = 'sys'
FI = handle.query_dn(mo)
mo_sys = handle.query_classid(class_id='networkElement')
component_Adaptor = "adaptorUnit"
component_CPU = "ProcessorUnit"
component_IOM = "EquipmentIOCard"
component_DIMM = "MemoryUnit"
filter_str = '(dn,"%s")' % mo

mo_obj = handle.query_classid(class_id='ComputeBlade', filter_str=filter_str)


for i in mo_obj:
    filter_str = '(dn,"%s")' % i.dn
    #print filter_str
    mo_adaptor = handle.query_classid(class_id=component_Adaptor,filter_str= filter_str)

    filter_str_cpu = '(dn,"%s")' % (i.dn +"/board/cpu-1")
    filter_str_DIMM = '(dn,"%s",type="eq")' % (i.dn +"/board/memarray-1/mem-1")
    #print filter_str_cpu

    mo_chassis_dn = i.dn.split("/")[0]+"/"+i.dn.split("/")[1]
    mo_chassis = handle.query_dn(mo_chassis_dn)
    mo_cpu = handle.query_classid(class_id=component_CPU,filter_str=filter_str_cpu)
    mo_IOM = handle.query_children(in_dn=mo_chassis_dn,class_id=component_IOM)
    mo_dimm = handle.query_classid(class_id= "MemoryUnit", filter_str=filter_str_DIMM)
    result=( \
        FI.name,mo_sys[0].serial,mo_sys[1].serial,\
        i.chassis_id,mo_chassis.serial,
        i.slot_id,i.serial,i.descr,i.name,i.assigned_to_dn,i.model,\
        mo_adaptor[0].model,mo_adaptor[0].serial,\
        mo_cpu[0].model, i.num_of_cpus,i.num_of_cores,\
        int(i.available_memory)/1024,int(mo_dimm[0].capacity)/1024,mo_dimm[0].clock,\
        mo_IOM[0].model,mo_IOM[0].serial,mo_IOM[1].serial)
    print result
    data.append(result)
#print data

    #print mo_IOM[0]

handle.logout()
print "logout UCS manager"
