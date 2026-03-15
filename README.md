# Bootstrap

Set up personal environment (Ubuntu, MacOS).

## Dependencies

- Ubuntu >= 24.04 if used (for Ghostty installation)
- Python 3
- Ansible >= 2.13.0 ([required by ansible community.general version 8.1.0](https://galaxy.ansible.com/ui/repo/published/community/general/?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW&version=8.1.0))
- Homebrew (MacOS only)

## Set up environment

Run the following commands and let them cook:

```bash
git clone --recursive https://github.com/lan1812783/bootstrap.git
cd bootstrap

# https://stackoverflow.com/a/67662402/12141366
# sudo update-ca-certificates --fresh
# export SSL_CERT_DIR=/etc/ssl/certs
python3 -m ansible galaxy collection install -r requirements.yml # if ansible is installed using pip
# ansible-galaxy collection install -r requirements.yml # if ansible is installed using package manager

python3 -m ansible playbook --ask-become-pass site.yml # if ansible is installed using pip
# ansible-playbook --ask-become-pass site.yml # if ansible is installed using package manager
```

Close and reopen the terminal.

## If use GNOME Terminal, change the font to Nerd Font

1. Open 'Preferences' > 'Profiles'
2. Select a profile to use
3. Check the 'Custom font' checkbox
4. Choose the 'JetBrainsMono Nerd Font Regular' as the custom font
   > If the font is not found, try logging out then logging in back or restarting your computer

## Set up tmux

1. Launch tmux
2. Run `tmux source ~/.tmux.conf`
3. Press `prefix` + `I`, wait a bit for everything to be up and running

## Occasionally update Neovim to its latest stable version

The bootstrapping process skips Neovim latest stable installation if it finds `nvim` binary on the system. To force the installation, run this command:

```bash
# Ref: https://fabianlee.org/2021/07/28/ansible-overriding-boolean-values-using-extra-vars-at-runtime/#:~:text=If%20you%20are%20using%20%E2%80%9C%E2%80%93extra,%22%20when:%20not%20myflag%7Cbool
python3 -m ansible playbook --ask-become-pass --tag neovim --extra-vars '{"nvim_force_installation": true}' site.yml # if ansible is installed using pip
# ansible-playbook --ask-become-pass --tag neovim --extra-vars '{"nvim_force_installation": true}' site.yml # if ansible is installed using package manager
```

## Ubuntu 25.10 `sudo` issue

Ubuntu 25.10 ships with Rust-based replacements for key system utilities, including `rust-coreutils` and `sudo-rs` (a Rust implementation of `sudo`). The change causes `Ansible` to [fail](https://www.reddit.com/r/selfhosted/comments/1ofrfha/using_ansible_to_patch_ubuntu_2510) when working with the `become` option family. As a workaround, switch the system to the legacy `sudo` binary to restore compatibility.

```bash
$ sudo update-alternatives --config sudo
There are 2 choices for the alternative sudo (providing /usr/bin/sudo).

  Selection    Path                     Priority   Status
------------------------------------------------------------
* 0            /usr/lib/cargo/bin/sudo   50        auto mode
  1            /usr/bin/sudo.ws          40        manual mode
  2            /usr/lib/cargo/bin/sudo   50        manual mode

Press <enter> to keep the current choice[*], or type selection number: 1
update-alternatives: using /usr/bin/sudo.ws to provide /usr/bin/sudo (sudo) in manual mode
```

## Additional MacOS settings

Some MacOS settings are quite tedious to be configured via Ansible (just like `Profiles` in GNOME Terminal), just configure them via the UI for simplicity sake.

Display battery percentage:
`Preferences > Menu Bar > Baterry Options... > Show Percentage`

MacOS has a default `Control Space` shortcut to select the previous input source at:
`Preferences > Keyboard > Keyboard shortcuts > Input sources > Select the previous input source`
Disable it or change its shortcut to another (e.g. `Option Space`) so that `Control Space` can be used to trigger code suggestion while in text editor or IDE.
