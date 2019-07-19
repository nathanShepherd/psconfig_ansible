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
    cmd = "psconfig "+ x +" "+ module_x
    res = m.run_command(cmd)

    if res[0] != 0:
        res = [res[0], "Error with " + cmd, res[2]]
        m.fail_json(msg=out + res)

    res = [res[0], cmd, res[1]]
    out.append(res)

def main():
    #from ansible.module_utils.cisco_imc import ImcConnection
    #from imcsdk.apis.server.inventory import inventory_get
    module = AnsibleModule(
        no_log=False,
        argument_spec=dict(
            # Module parameters
            # TODO change (publish and remote) --> command: {p:, r:}          
            remote	= dict(required=False, type='dict'),
            publish	= dict(required=False, type='dict'),
            #proxy	= dict(required=False, default=None)
        ),
        supports_check_mode=False
    )
    #print("MSg pnt console") #does nothing
    #module.debug("Debug msg")  #does nothing
    #module.log("Message here") #does nothing

    result = []
    param = module.params

    if param["publish"] is not None:
        run_cmd(module, "publish", param["publish"]["file"], result)
        _url = result[0][2].split("\"")[-2]

    if param["remote"] is not None:
        if "add" in param["remote"]:
            run_cmd(module, "remote add", param["remote"]["add"], result)
        if "delete" in param["remote"]:                                           
            run_cmd(module, "remote delete", param["remote"]["delete"], result)

    #module.exit_json(ansible_facts=dict())
    #module.fail_json(msg="Something fatal happened") 


    module.exit_json(log=result,
                     changed=(len(result) > 0), 
                     invocations=module.params,
                     ansible_facts=dict(url=_url))

if __name__ == '__main__':
    main()

