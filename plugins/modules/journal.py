#!/usr/bin/env python3

# Copyright: (C) 2023, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

from pathlib import Path

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = 'https://systemd.ansibleguy.net/en/latest/modules/journal.html'
EXAMPLES = 'https://systemd.ansibleguy.net/en/latest/modules/journal.html'

DEFAULT_BIN = '/usr/bin/journalctl'


def run_module():
    module_args = dict(
        unit=dict(
            type='list', elements='str', required=True, aliases=['u', 'svc', 'units', 'service', 'services'],
            description='One or more systemd units to query the protocol for',
        ),
        lines=dict(
            type='int', required=False, aliases=['l', 'c', 'n', 'count'],
            description='How many lines to query'
        ),
        reverse=dict(type='bool', required=False, default=False, aliases=['r', 'rev']),
        limit=dict(
            type='str', required=False, choices=['system', 'user'], aliases=['lim'],
            description='Show messages from system services and the kernel (with --system). '
                        'Show messages from service of current user (with --user). '
                        'If neither is specified, show all messages that the user can see'
        ),
        since=dict(
            type='str', required=False, aliases=['start', 'time_since', 'start_time'],
            description='Limit the time period to query for. '
                        "Examples: '1 hour ago', '2 days ago', '2023-03-24 21:15:00'",
        ),
        until=dict(
            type='str', required=False, aliases=['stop', 'time_until', 'stop_time'],
            description='Limit the time period to query for. '
                        "Examples: '1 hour ago', '2 days ago', '2023-03-24 21:15:00'",
        ),
        fields=dict(
            type='str', required=False, aliases=['fds'],
            description='A comma separated list of the fields which should be included in the output. '
                        'This has an effect only for the output modes which would normally show all fields '
                        '(verbose, export, json, json-pretty, json-sse and json-seq), as well as on cat'
        ),
        format=dict(
            type='str', required=False, aliases=['fmt'], choices=[
                'short', 'short-full', 'short-iso', 'short-iso-precise', 'short-precise', 'short-monotonic',
                'short-unix', 'verbose', 'export', 'json', 'json-pretty', 'json-sse', 'json-seq', 'cat', 'with-unit',
            ],
            description='Controls the formatting of the journal entries that are shown'
        ),
    )

    result = dict(
        changed=False,
        diff={
            'before': {},
            'after': {},
        },
        data=[],
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    p = module.params

    # finding binary
    cmd_bin = None
    rc, _, _ = module.run_command(['which', 'journalctl'])

    if rc == 0:
        cmd_bin = 'journalctl'

    if cmd_bin is None and Path(DEFAULT_BIN).is_file():
        cmd_bin = DEFAULT_BIN

    if cmd_bin is None:
        module.fail_json(
            f"Journalctl executable neither found in PATH nor at '{DEFAULT_BIN}'!"
        )

    # building cmd
    cmd = [
        cmd_bin, '--no-pager', '--full',
        '--lines', f"{p['lines']}",
    ]

    for unit in p['unit']:
        cmd.extend(['--unit', unit])

    if p['reverse']:
        cmd.append('--reverse')

    if p['limit'] is not None:
        if p['limit'] == 'user':
            cmd.append('--user')

        elif p['limit'] == 'system':
            cmd.append('--system')

    if p['since'] is not None:
        cmd.extend(['--since', f"{p['since']}"])

    if p['until'] is not None:
        cmd.extend(['--until', f"{p['until']}"])

    if p['format'] is not None:
        cmd.extend(['--output', f"{p['format']}"])

    if p['fields'] is not None:
        cmd.extend(['--output-fields', f"{p['fields']}"])

    # execute
    rc, stdout, stderr = module.run_command(cmd)

    if rc == 0:
        result['data'] = stdout.split('\n')

    else:
        module.fail_json(f"Failed to execute command: '{cmd}' - ERROR: '{stderr}'")

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
