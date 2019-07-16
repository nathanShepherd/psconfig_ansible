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
            port	= dict(required=False, default=None),
            secure	= dict(required=False, default=None),
            proxy	= dict(required=False, default=None)
        ),
        supports_check_mode=False
    )
    #module.debug("Debug msg")  #does nothing
    #module.log("Message here") #does nothing
    STDOUT = []
    result = []
    run_cmd = lambda x, y: module.run_command("psconfig "+x+" "+module.params[y])
    #result.append(run_cmd("publish", "publish"))
            #result.append([0, command])

    if module.params["publish"] is not None:
        result.append(module.run_command("psconfig publish " + module.params["publish"]))

    if module.params["remote_add"] is not None:
        result.append(run_cmd("remote add", "remote_add"))

    if module.params["remote_delete"] is not None:
        result.append(run_cmd("remote delete", "remote_delete"))

  
  ####  if len(result) != 0 and result[-1][0] != 0:
  ####      module.fail_json(msg=result)
  



            #STDOUT.append(outs)
    #module.exit_json(ansible_facts=dict())
    #module.fail_json(msg="Something fatal happened") 



    #print("MSg pnt console") #does nothing

    module.exit_json(changed=True, 
                     published=module.params["publish"],
                     log=result, 
		     debug=module.params)

if __name__ == '__main__':
    main()

