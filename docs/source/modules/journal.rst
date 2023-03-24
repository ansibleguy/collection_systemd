.. _modules_journal:

.. include:: ../_include/head.rst

===============
Systemd Journal
===============

**Service Docs**: `Systemd Journalctl <https://manpages.ubuntu.com/manpages/jammy/man1/journalctl.1.html>`_

Definition
**********

ansibleguy.systemd.journal
==========================

Module alias: ansibleguy.systemd.journalctl

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Aliases", "Comment"
    :widths: 15 10 10 10 10 45

    "unit","list of strings","true","\-","u, svc, units, service, services","One or more systemd units to query the protocol for"
    "lines","integer","false","50","l, c, n, count","How many lines to query"
    "reverse","boolean","false","false","rev","\-"
    "limit","string","false","\-","lim","One of 'system', 'user'. Show messages from system services and the kernel (with --system). Show messages from service of current user (with --user). If neither is specified, show all messages that the user can see"
    "since","string","false","\-","start, time_since, start_time","Limit the time period to query for. Examples: '1 hour ago', '2 days ago', '2023-03-24 21:15:00'"
    "until","string","false","\-","stop, time_until, stop_time","Limit the time period to query for. Examples: '1 hour ago', '2 days ago', '2023-03-24 21:15:00'"
    "fields","string","false","\-","fds","A comma separated list of the fields which should be included in the output. This has an effect only for the output modes which would normally show all fields (verbose, export, json, json-pretty, json-sse and json-seq), as well as on cat. For the former, the "__CURSOR", "__REALTIME_TIMESTAMP", "__MONOTONIC_TIMESTAMP", and "_BOOT_ID" fields are always printed"
    "format","string","false","\-","fmt","Controls the formatting of the journal entries that are shown"

Examples
********

ansibleguy.systemd.journal
==========================

.. code-block:: yaml

    - hosts: localhost
      gather_facts: no
      tasks:
        - name: Example
          ansibleguy.systemd.journal:
            unit: 'example'
            # lines: ''
            # reverse: false
            # limit: ''
            # since: ''
            # until: ''
            # fields: ''
            # format: ''

        - name: Pulling journal for apache2
          ansibleguy.systemd.journal:
            unit: 'apache2.service'
          register: j1

        - debug:
            var: j1.data

        - name: Pulling journal for nginx and haproxy in the last hour
          ansibleguy.systemd.journal:
            unit: ['nginx.service', 'haproxy.service']
            since: '1 hour ago'
          register: j2

        - debug:
            var: j2.data

        - name: Pulling nftables logs from time period
          ansibleguy.systemd.journal:
            unit: ['nftables.service']
            since: '2023-03-24 21:15:00'
            until: '2023-03-24 21:45:00
          register: j3

        - debug:
            var: j3.data

        - name: Pulling last 100 docker logs in reverse
          ansibleguy.systemd.journal:
            unit: ['docker.service']
            reverse: true
            lines: 100
          register: j4

        - debug:
            var: j4.data
