#!/usr/bin/env python

# copied to usr/lib/python2.7/site-packages/ansible-2.9.0.dev0-py2.7.egg/ansible/modules/extras/perfsonar/pscheduler/psconfig
# put __init__.py at ^^^/perfsonar
# put __init__.py at ^^^/perfsonar/pscheduler

from ansible.module_utils.basic import *

DOCUMENTATION = '''
---
module: psconfig_inventory
short_description: Get psconfig inventory
version_added: ""
description:
    - test

requirements: []
author: ""
'''

EXAMPLES = '''
- name: 
  psconfig_inventory:
    ip: "10.111.0.3"
    username: "admin"
'''


def main():
    #from ansible.module_utils.cisco_imc import ImcConnection
    #from imcsdk.apis.server.inventory import inventory_get
    module = AnsibleModule(
        argument_spec=dict(
            # Module parameters
            ip		= dict(required=False, type='str'),
            username	= dict(required=False, default="admin", type='str'),
            port	= dict(required=False, default=None),
            secure	= dict(required=False, default=None),
            proxy	= dict(required=False, default=None)
        ),
        supports_check_mode=False
    )

    #module.exit_json(ansible_facts=dict())
    #module.fail_json(msg="Something fatal happened") 
    module.exit_json(changed=True, something_else=1234)

if __name__ == '__main__':
    main()

