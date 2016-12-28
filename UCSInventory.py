from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("172.16.199.131", "config", "config")

handle.login()

query_dict = {}
query_dict['chassis'] = {}
query_dict['fi'] = {}
query_dict['blade'] = {}
query_dict['IOM'] = {}

query_data = handle.query_classids('orgOrg', 'EquipmentChassis',
                                   'NetworkElement', 'ComputeBlade',
                                   'EquipmentIOCard')

for chassis in query_data['EquipmentChassis']:
    query_dict['chassis'][chassis.dn] = {}
    query_dict['chassis'][chassis.dn]['model'] = chassis.model
    query_dict['chassis'][chassis.dn]['serial'] = chassis.serial

for fi in query_data['NetworkElement']:
    query_dict['fi'][fi.dn] = {}
    query_dict['fi'][fi.dn]['model'] = fi.model
    query_dict['fi'][fi.dn]['serial'] = fi.serial

for IOM in query_data['EquipmentIOCard']:
    query_dict['IOM'][IOM.dn] = {}
    query_dict['IOM'][IOM.dn]['model'] = IOM.model
    query_dict['IOM'][IOM.dn]['serial'] = IOM.serial

for blade in query_data['ComputeBlade']:
    query_dict['blade'][blade.dn] = {}
    query_dict['blade'][blade.dn]['model'] = blade.model
    query_dict['blade'][blade.dn]['serial'] = blade.serial
    query_dict['blade'][blade.dn]['available_memory'] = blade.available_memory
    # print blade.dn
    blade_rn = blade.dn.split('/')
    blade_parent = blade_rn[0] + '/' + blade_rn[1]
    blade_parent_info = handle.query_dn(blade_parent)
    # print blade_parent_info.dn
    blade_parent_chindren = handle.query_children(
        in_dn=blade_parent_info.dn, class_id="EquipmentIOCard")

    # print blade_parent_chindren[0].model, blade_parent_chindren
    query_dict['blade'][blade.dn]['IOM'] = blade_parent_chindren[0].model
    # print query_dict['IOM']
    blade_info = handle.query_dn(blade.dn)
    blade_info_chindren = handle.query_children(
        in_mo=blade_info, class_id="adaptorUnit")
    # print blade_info_chindren
    for blade_child_object in blade_info_chindren:
        query_dict['blade'][blade.dn]['adaptor'] = blade_child_object.model

    # print blade_parent


# print query_dict.keys()
# print query_dict["IOM"]
print query_dict
# print blade


handle.logout()
