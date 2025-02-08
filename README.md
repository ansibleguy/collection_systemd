# Ansible Collection - ansibleguy.systemd

[![Lint](https://github.com/ansibleguy/collection_systemd/actions/workflows/lint.yml/badge.svg)](https://github.com/ansibleguy/collection_systemd/actions/workflows/lint.yml)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/repo/published/ansibleguy/systemd)

**Functional Tests**: 

* Status: [![Functional Test Status](https://badges.ansibleguy.net/systemd.collection.test.svg)](https://github.com/ansibleguy/collection_systemd/blob/latest/scripts/test.sh) |
[![Functional-Tests](https://github.com/ansibleguy/collection_systemd/actions/workflows/functional_test_result.yml/badge.svg)](https://github.com/ansibleguy/collection_systemd/actions/workflows/functional_test_result.yml)
* Logs: [API](https://ci.ansibleguy.net/api/job/ansible-test-collection-systemd/logs?token=2b7bba30-9a37-4b57-be8a-99e23016ce70&lines=1000) |
[Daily Archive](https://github.com/ansibleguy/collection_systemd/actions/workflows/functional_test_result.yml) |
[Short](https://badges.ansibleguy.net/log/collection_systemd_test_short.log) | [Full](https://badges.ansibleguy.net/log/collection_systemd_test.log)

Internal CI: [Tester Role](https://github.com/ansibleguy/_meta_cicd) | [Jobs API](https://github.com/O-X-L/github-self-hosted-jobs-systemd)

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
