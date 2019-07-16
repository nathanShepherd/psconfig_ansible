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
    for command in module.params:
        if module.params[command] is not None:
            orig = command
            command = ""
            if orig != "publish":
                for cmd in command.split("_"):
                    command += cmd + " "
            else:
                command = orig + " " 
            outs = module.run_command("psconfig " + command + module.params[orig])
            if outs[0] != 0:
                module.fail_json(msg=outs[2])
            STDOUT.append(outs)
    #module.exit_json(ansible_facts=dict())
    #module.fail_json(msg="Something fatal happened") 



    #print("MSg pnt console") #does nothing

    module.exit_json(changed=True, 
                     published=module.params["publish"],
                     result=STDOUT, 
		     debug=module.params)

if __name__ == '__main__':
    main()

