# Ansible Collection - ansibleguy.systemd

<a href='https://ko-fi.com/ansible0guy' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy me a coffee' />

<!-- [![Lint Test Status](https://badges.ansibleguy.net/systemd.collection.lint.svg)](https://github.com/ansibleguy/collection_systemd/blob/latest/scripts/lint.sh) -->

[![Docs](https://readthedocs.org/projects/systemd_ansible/badge/?version=latest&style=flat)](https://systemd.ansibleguy.net)
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

You want a simple Ansible GUI? Check-out my [Ansible WebUI](https://github.com/ansibleguy/webui)

----

## Modules


| Function    | Module                     | Usage                                                                     |
|:------------|:---------------------------|:----------------------------------------------------------------------|
| **Journal** | ansibleguy.systemd.journal | [Docs](https://systemd.ansibleguy.net/en/latest/modules/journal.html) |
