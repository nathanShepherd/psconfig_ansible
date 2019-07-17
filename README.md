# psconfig_ansible
The perfSonar tool psconfig as a module for ansible.


### Must have Ansible installed
```
sudo pip install ansible
```

### Required software
```
[psconfig]
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
