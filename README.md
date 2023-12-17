# Bootstrap
Set up personal environment (Ubuntu)

## Dependencies
- Python 3
- Ansible

## Set up environment
```bash
git clone --recursive https://github.com/lan1812783/bootstrap.git
cd bootstrap
ansible-playbook --ask-become-pass site.yml
```
