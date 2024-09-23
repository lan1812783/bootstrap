'''
Simple script to set custom keyboard shortcut.
Reference: https://askubuntu.com/a/597414.
'''

import argparse
import ast
import logging
import subprocess

logger = logging.getLogger(__name__)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Set custom keyboard shortcuts.'
    )
    parser.add_argument(
        '-n',
        '--name',
        help='name of the custom keyboard shotcuts',
        required=True,
    )
    parser.add_argument(
        '-c',
        '--command',
        help=(
            'command of the custom keyboard shotcuts to execute when binding'
            ' is hit'
        ),
        required=True,
    )
    parser.add_argument(
        '-b',
        '--binding',
        help='key combination of the custom keyboard shotcuts',
        required=True,
    )

    return parser.parse_args()


def run_cmd(cmd: list[str]) -> tuple[list[str], bool]:
    try:
        completed_process: subprocess.CompletedProcess[bytes] = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=True,
        )
    except subprocess.CalledProcessError:
        logger.exception('Command %s executed unsuccessfully', cmd)
        return ([], False)
    return (completed_process.stdout.decode('utf-8').split('\n')[:-1], True)


media_key_components = [
    'org',
    'gnome',
    'settings-daemon',
    'plugins',
    'media-keys',
]
media_key = '.'.join(media_key_components)
single_key = 'custom-keybinding'
multi_key = f'{single_key}s'


def find_and_set_new_custom_keybinding() -> str:
    # Get current custom keybindings
    stdout_lines, sucs = run_cmd(['gsettings', 'get', media_key, multi_key])
    if not sucs:
        return ''
    # If the array is empty, remove the annotation hints
    raw_custom_bindings = stdout_lines[0].lstrip('@as ')
    custom_bindings: list[str] = ast.literal_eval(raw_custom_bindings)

    # Find new custom keybinding
    i = 0
    new_custom_keybinding_fmt = (
        '/' + '/'.join(media_key_components) + f'/{multi_key}/custom%d/'
    )
    while True:
        new_custom_keybinding = new_custom_keybinding_fmt % i
        if new_custom_keybinding not in custom_bindings:
            break
        i += 1

    # Set new custom keybindings
    custom_bindings.append(new_custom_keybinding)
    stdout_lines, sucs = run_cmd(
        ['gsettings', 'set', media_key, multi_key, str(custom_bindings)]
    )
    if not sucs:
        return ''

    return new_custom_keybinding


def set_custom_keybinding_properties(
    name: str, command: str, binding: str, custom_binding: str
):
    set_key = f'{media_key}.{single_key}:{custom_binding}'
    run_cmd(['gsettings', 'set', set_key, 'name', name])
    run_cmd(['gsettings', 'set', set_key, 'command', command])
    run_cmd(['gsettings', 'set', set_key, 'binding', binding])


if __name__ == '__main__':
    args = parse_arguments()
    new_custom_binding = find_and_set_new_custom_keybinding()
    set_custom_keybinding_properties(
        args.name, args.command, args.binding, new_custom_binding
    )
