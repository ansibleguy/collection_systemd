# Ansible Collection - oxlorg.systemd

[![Lint](https://github.com/O-X-L/ansible-collection-systemd/actions/workflows/lint.yml/badge.svg)](https://github.com/O-X-L/ansible-collection-systemd/actions/workflows/lint.yml)
[![Ansible Galaxy](https://badges.oss.oxl.app/galaxy.badge.svg)](https://galaxy.ansible.com/ui/repo/published/oxlorg/systemd)

**Functional Tests**: 

* Status: [![Functional Test Status](https://badges.oss.oxl.app/oxlorg.systemd.collection.test.svg)](https://github.com/O-X-L/ansible-collection-systemd/blob/latest/scripts/test.sh) |
[![Functional-Tests](https://github.com/O-X-L/ansible-collection-systemd/actions/workflows/functional_test_result.yml/badge.svg)](https://github.com/O-X-L/ansible-collection-systemd/actions/workflows/functional_test_result.yml)
* Logs: [API](https://ci.oss.oxl.app/api/job/ansible-test-collection-systemd/logs?token=2b7bba30-9a37-4b57-be8a-99e23016ce70&lines=1000) |
[Daily Archive](https://github.com/O-X-L/ansible-collection-systemd/actions/workflows/functional_test_result.yml) |
[Short](https://badges.oss.oxl.app/log/collection_oxlorg.systemd_test_short.log) | [Full](https://badges.oss.oxl.app/log/collection_oxlorg.systemd_test.log)

Internal CI: [Tester Role](https://github.com/O-X-L/ansible-role-oxl-cicd) | [Jobs API](https://github.com/O-X-L/github-self-hosted-jobs-systemd)

----

## Contribute

Feel free to contribute to this project using [pull-requests](https://github.com/O-X-L/ansible-collection-systemd/pulls), [issues](https://github.com/O-X-L/ansible-collection-systemd/issues) and [discussions](https://github.com/O-X-L/ansible-collection-systemd/discussions)!

**What to contribute**:

* extend or correct the [documentation](https://github.com/O-X-L/ansible-collection-systemd/blob/latest/docs)
* contribute code fixes or optimizations

----

## Requirements

Install the collection:

```bash
# latest version:
ansible-galaxy collection install git+https://github.com/O-X-L/ansible-collection-systemd.git

# stable/tested version:
ansible-galaxy collection install oxlorg.systemd

# install to specific directory for easier development
cd $PLAYBOOK_DIR
ansible-galaxy collection install git+https://github.com/O-X-L/ansible-collection-systemd.git -p ./collections
```

----

## Usage

See: [Docs](https://ansible-systemd.oxl.app)

[![Docs Uptime](https://status.oxl.at/api/v1/endpoints/1--oxl_systemd-ansible-collection-docs/uptimes/7d/badge.svg)](https://status.oxl.at/endpoints/1--oxl_systemd-ansible-collection-docs)

[Alternative Link](https://systemd-ansible.readthedocs.io/)

You want a simple Ansible GUI? Check-out our [Ansible WebUI](https://github.com/O-X-L/ansible-webui)

----

## Modules


| Function    | Module                     | Usage                                                                     |
|:------------|:---------------------------|:----------------------------------------------------------------------|
| **Journal** | oxlorg.systemd.journal | [Docs](https://ansible-systemd.oxl.app/modules/journal.html) |
