# Ansible Collection - ansibleguy.systemd

<!-- [![Lint Test Status](https://badges.ansibleguy.net/systemd.collection.lint.svg)](https://github.com/ansibleguy/collection_systemd/blob/latest/scripts/lint.sh) -->

[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/repo/published/ansibleguy/systemd)

----

## Contribute

Feel free to contribute to this project using [pull-requests](https://github.com/ansibleguy/collection_systemd/pulls), [issues](https://github.com/ansibleguy/collection_systemd/issues) and [discussions](https://github.com/ansibleguy/collection_systemd/discussions)!

**What to contribute**:

* extend or correct the [documentation](https://github.com/ansibleguy/collection_systemd/blob/latest/docs)
* contribute code fixes or optimizations

----

## Requirements

Install the collection:

```bash
# latest version:
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_systemd.git

# stable/tested version:
ansible-galaxy collection install ansibleguy.systemd

# install to specific directory for easier development
cd $PLAYBOOK_DIR
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_systemd.git -p ./collections
```

----

## Usage

See: [Docs](https://systemd.ansibleguy.net)

[![Docs Uptime](https://status.oxl.at/api/v1/endpoints/4--ansibleguy_ansible-collection---systemd-documentation/uptimes/7d/badge.svg)](https://status.oxl.at/endpoints/4--ansibleguy_ansible-collection---systemd-documentation)

[Alternative Link](https://systemd-ansible.readthedocs.io/)

You want a simple Ansible GUI? Check-out my [Ansible WebUI](https://github.com/ansibleguy/webui)

----

## Modules


| Function    | Module                     | Usage                                                                     |
|:------------|:---------------------------|:----------------------------------------------------------------------|
| **Journal** | ansibleguy.systemd.journal | [Docs](https://systemd.ansibleguy.net/modules/journal.html) |
