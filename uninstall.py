#!/usr/bin/env python

import os
import sys
import shutil

try:
    import ansible
except:
    print("Ansible is not installed")
    sys.exit(1)

ansible_path = ansible.__path__[0]
extras_path = ansible_path + '/modules/extras'
psconfig_path = extras_path + '/psconfig_ansible'

if os.path.isdir(psconfig_path):
    shutil.rmtree(psconfig_path)
