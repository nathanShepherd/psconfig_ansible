#!/usr/bin/env python

# copied to usr/lib/python2.7/site-packages/ansible-2.9.0.dev0-py2.7.egg/ansible/modules/extras/pscheduler/
# put __init__.py at the above directory

from ansible.module_utils.basic import *

DOCUMENTATION = '''
---
module: psconfig
short_description: Get psconfig inventory
version_added: ""
description:
    - test

requirements: []
author: ""
'''

EXAMPLES = '''
- name: 
  psconfig:
    publish: "10.111.0.3"
    username: "admin"
'''

#def run_cmd(task, command):
#    return module.run_command("psconfig " + task +" "+ module.params[command])

def run_cmd(m, x, module_x, out):
    module_x = m.params[module_x]
    cmd = "psconfig "+ x +" "+ module_x
    res = m.run_command(cmd)

    if res[0] != 0:
        res = [res[0], "Error with " + cmd, res[2]]
        m.fail_json(stderr=out + res)

    res = [res[0], cmd, res[1]]
    out.append(res)

def main():
    #from ansible.module_utils.cisco_imc import ImcConnection
    #from imcsdk.apis.server.inventory import inventory_get
    module = AnsibleModule(
        no_log=False,
        argument_spec=dict(
            # Module parameters
            publish	= dict(required=False, type='str'),
            remote_add  = dict(required=False, type='str'),
            remote_delete  = dict(required=False, type='str'),
            #proxy	= dict(required=False, default=None)
        ),
        supports_check_mode=False
    )
    #print("MSg pnt console") #does nothing
    #module.debug("Debug msg")  #does nothing
    #module.log("Message here") #does nothing

    result = []

    if module.params["publish"] is not None:
        run_cmd(module, "publish", "publish", result)

    if module.params["remote_add"] is not None:
        run_cmd(module, "remote add", "remote_add", result)

    if module.params["remote_delete"] is not None:
        run_cmd(module, "remote delete", "remote_delete", result)

    #module.exit_json(ansible_facts=dict())
    #module.fail_json(msg="Something fatal happened") 




    module.exit_json(log=result, 
                     changed=(len(result) > 0), 
                     invocations=module.params,
                     published=module.run_command("psconfig published"),
                     remote_list=module.run_command("psconfig remote list"))

if __name__ == '__main__':
    main()

