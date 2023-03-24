# Ansible Collection - ansibleguy.systemd

<!-- [![Lint Test Status](https://badges.ansibleguy.net/systemd.collection.lint.svg)](https://github.com/ansibleguy/collection_systemd/blob/latest/scripts/lint.sh) -->

[![Docs](https://readthedocs.org/projects/systemd_ansible/badge/?version=latest&style=flat)](https://systemd.ansibleguy.net)
[![Ansible Galaxy](https://img.shields.io/ansible/collection/2148)](https://galaxy.ansible.com/ansibleguy/systemd)

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
# stable/tested version:
ansible-galaxy collection install ansibleguy.systemd

# latest version:
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_systemd.git

# install to specific directory for easier development
cd $PLAYBOOK_DIR
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_systemd.git -p ./collections
```

----

## Usage

See: [Docs](https://systemd.ansibleguy.net)

----

## Modules


| Function    | Module                     | Usage                                                                     |
|:------------|:---------------------------|:----------------------------------------------------------------------|
| **Journal** | ansibleguy.systemd.journal | [Docs](https://systemd.ansibleguy.net/en/latest/modules/journal.html) |
