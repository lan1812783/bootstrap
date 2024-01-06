# Bootstrap
Set up personal environment (Ubuntu).

## Dependencies
- Python 3
- Ansible >= 2.13.0 ([required by ansible community.general version 8.1.0](https://galaxy.ansible.com/ui/repo/published/community/general/?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW))

## Set up environment
Run the following commands and let them cook:
```bash
git clone --recursive https://github.com/lan1812783/bootstrap.git
cd bootstrap

# https://stackoverflow.com/a/67662402/12141366
# sudo update-ca-certificates --fresh
# export SSL_CERT_DIR=/etc/ssl/certs
ansible-galaxy collection install -r requirements.yml

ansible-playbook --ask-become-pass site.yml
```
Close and reopen the terminal.

## Change terminal font to Nerd Font
1. Open 'Preferences' > 'Profiles'
2. Select a profile to use
3. Check the 'Custom font' checkbox
4. Choose the 'Hack Nerd Font Regular' as the custom font
> If the font is not found, try logging out then logging in back or restarting your computer

## Set up tmux
1. Launch tmux
2. Run `tmux source ~/.tmux.conf`
3. Press `prefix` + `I`, wait a bit for everything to be up and running
