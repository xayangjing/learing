import pyVim
from pyVmomi import vim
from pyVim import connect
from pyVim.connect import Disconnect
import datetime
import time
'''
Create vcenter server Authentication
'''
VCenter = 'xavc01.active.tan'
vC_user = 'tan\\vmadmin'
vC_password = 'G0Virtual!'
si = connect.ConnectNoSSL(host=VCenter, user=vC_user, pwd=vC_password)
Spec = vim.TaskFilterSpec.ByTime()
Spec.timeType= vim.TaskFilterSpec.TimeOption.startedTime
Spec.endTime = datetime.datetime.now()
Spec.beginTime=  Spec.endTime - datetime.timedelta(minutes=5)
Tfilter = vim.TaskFilterSpec()
Tfilter.time = Spec
content = si.RetrieveContent()
tasks = content.taskManager.CreateCollectorForTasks(Tfilter)
alltasks = tasks.ReadNextTasks(999)
history = []
#print alltasks
for i in alltasks:
    if 'userName' in dir(i.reason):
        print i.startTime,i.completeTime,i.reason.userName,(i.descriptionId.split("."))[-1:][0],i.entityName,  i.state, i.key

    else:
        pass

tasks.DestroyCollector

Disconnect(si)
