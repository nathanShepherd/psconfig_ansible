# psconfig_ansible
The perfSonar tool psconfig as a module for ansible.

### Required software

- Ansible
```
sudo pip install ansible
```

- psconfig

CentOS:
```
yum install perfsonar-psconfig-publisher
```

Debian/Ubuntu:
```
apt-get install perfsonar-psconfig-publisher
```

## Install 
### Clone this repository and install ansible modules
```
git clone https://github.com/nathanShepherd/psconfig_ansible.git
cd psconfig_ansible
sudo python install.py
```

## Usage
play.yml acts as an example to highlight the capabilities of the module.
```
ansible-playbook play.yml
```

## Uninstall
```
sudo python uninstall.py
```
