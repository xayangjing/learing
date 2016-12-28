import tablib
from pyVim.connect import SmartConnect
from pyVmomi import vim
import re


#  funcations

def folder_path(vm):
    if vm.parent.name == 'Datacenters':
        pass
    else:
        vm_folder_names.append(vm.parent.name)
    if vm.parent.name != 'Datacenters':
        folder_path(vm.parent)

def get_VM_full_path(vm):
    folder_path(vm)
    list.reverse(vm_folder_names)
    vm_folder_parent ="\\".join(vm_folder_names)
    vm_folder_list = vm_folder_parent
    return vm_folder_list


def vm_sdm_info(vm_folder_names):
    try:
        org_str = vm_folder_names[2]
        production_str = vm_folder_names[3]
        pid_str = re.search(r'(p\d+)', vm_folder_names[4]).group()
        pid = re.search('\d+', pid_str).group()
        return org_str, production_str, pid
    except:
        pass

def vm_org (vm_folder_names):
    try:
        return  vm_sdm_info(vm_folder_names).__getitem__(0)
    except:
        return None

def vm_production_str (vm_folder_names):
    try:
        return  vm_sdm_info(vm_folder_names).__getitem__(1)
    except:
        return None

def vm_pid (vm_folder_names):
    try:
        return  vm_sdm_info(vm_folder_names).__getitem__(2)
    except:
        return None

def get_vm_network_name(vm):
    if vm.network.__len__() ==0:
        return None
    else:
        return vm.network[0].name

def get_vm_network_info(vm):
    if vm.network.__len__() == 0:
        return None,None
    else:
        try:
                return vm.network[0].config.defaultPortConfig.vlan.vlanId,\
                       vm.network[0].config.distributedVirtualSwitch.name
        except AttributeError,e:
            vm_host_network_config = vm.runtime.host.config.network
            port_list = []
            for x in  vm_host_network_config.portgroup:
                port_list.append(x.spec.name)
                if x.spec.name == vm.network[0].name:
                    return x.spec.vlanId,x.spec.name
            if vm.network[0].name not in port_list:
                return None,vm.network[0].name

def get_vm_annotations(vm):
    try:
        del annotations[:]
        i = 0
        while i < vm.customValue.__len__():
            n = child.customValue[i].value
            annotations.append(n)
            i += 1
        return annotations
    except:
        pass

def vm_Atom_CreationTicket(vm):
    try:
        return get_vm_annotations(vm).__getitem__(1)
    except:
        return  None

def vm_Atom_Environment(vm):
    try:
        return get_vm_annotations(vm).__getitem__(2)
    except:
        return  None

def vm_Atom_Role(vm):
    try:
        return get_vm_annotations(vm).__getitem__(3)
    except:
        return  None

def vm_Atom_pid(vm):
    try:
        return get_vm_annotations(vm).__getitem__(0)
    except:
        return  None


def get_vnic_macAdress (vm):
    for x in vm.config.hardware.device:
        vnic_info = x
        try:
            return vnic_info.macAddress
        except:
            pass




def get_vm_vnic_type(vm):
    for x in vm.config.hardware.device:
        if isinstance(x,vim.vm.device.VirtualE1000e):
            vnic= 'E1000e'
            return  vnic
        if isinstance(x,vim.vm.device.VirtualE1000):
            vnic= 'E1000'
            return vnic
        if isinstance(x,vim.vm.device.VirtualPCNet32):
            vnic= 'PCNet32'
            return vnic
        if isinstance(x,vim.vm.device.VirtualVmxnet):
            vnic= 'Vmxnet'
            return vnic
        if isinstance(x,vim.vm.device.VirtualVmxnet3):
            vnic= 'Vmxnet3'
            return vnic
    else:
        return None

def get_disk_type(vm):
    if vm.summary.config.numVirtualDisks == None:
        return None
    else:
        return  'Standard'

VCenter = 'xavc01.active.tan'
vC_user = 'tan\\vmadmin'
vC_password = 'G0Virtual!'
si = SmartConnect(host=VCenter, user=vC_user, pwd=vC_password)
content = si.RetrieveContent()
container = content.rootFolder
DC_type = [vim.VirtualMachine]
contentView = content.viewManager.CreateContainerView(container, DC_type, True)
children = contentView.view

header = ('VM display name',
          'VM FQDN ',
          'PowerState',
          'cluster',
          'DataCenter',
          'Element_Manager',
          'OS verison',
          'OS Family',
          'VMware tools Version',
          'VMware tools Version Status',
          'VMware tools Status',
          'IP address',
          'Mac address',
          'Network Name',
          'VLAN ID',
          'DistributedVirtualSwitch',
          'NIC type',
          'CPU Number',
          'Memory Szie',
          'Provsion Disk',
          'used Disk',
          'Free Disk',
          'Disk Numbers',
          'RDM Disk',
          'Datastore',
          'VMx file',
          'folder',
          'Org',
          'Production',
          'Pid',
          'CreationTicket',
          'Environment',
          'Role',
          'pid'
          )
data = tablib.Dataset()
data.headers = header
for child in children:
    if child.summary.config.template is False:
        vm_folder_names = []
        annotations = []
        print child.name
        data.append([child.name,
                     child.summary.guest.hostName,
                     child.summary.runtime.powerState,
                     child.summary.runtime.host.parent.name,
                     child.summary.runtime.host.parent.parent.parent.name,
                     VCenter,
                     child.summary.guest.guestFullName,
                     child.guest.guestFamily,
                     child.guest.toolsVersion,
                     child.guest.toolsStatus,
                     child.guest.toolsRunningStatus,
                     child.guest.ipAddress,
                     get_vnic_macAdress(child),
                     child.network[0].name,
                     get_vm_network_info(child)[0],
                     get_vm_network_info(child)[1],
                     get_vm_vnic_type(child),
                     child.summary.config.numCpu,
                     child.summary.config.memorySizeMB,
                     int((child.summary.storage.committed+child.summary.storage.uncommitted)/1024/1024/1024),
                     int(child.summary.storage.committed/1024/1024/1024),
                     int(child.summary.storage.uncommitted/1024/1024/1024),
                     child.summary.config.numVirtualDisks,
                     get_disk_type(child),
                     child.config.datastoreUrl[0].name,
                     child.config.files.vmPathName,
                     get_VM_full_path(child),
                     vm_org(vm_folder_names),
                     vm_production_str(vm_folder_names),
                     vm_pid(vm_folder_names),
                     vm_Atom_CreationTicket(child),
                     vm_Atom_Environment(child),
                     vm_Atom_Role(child),
                     vm_Atom_pid(child)
                     ])
        # print vm_Atom_CreationTicket(child)

    else:
        pass
print data
data.json


