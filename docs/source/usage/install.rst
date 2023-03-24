.. _usage_install:

.. include:: ../_include/head.rst

============
Installation
============


Ansible
*******

See `the documentation <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#pip-install>`_ on how to install Ansible.

Dependencies
************

`Systemd <https://brand.systemd.io>`_ must be installed and running on the target system.


Collection
**********

.. code-block:: bash

    # stable version:
    ansible-galaxy collection install ansibleguy.systemd

    # latest version:
    ansible-galaxy collection install git+https://github.com/ansibleguy/collection_systemd.git

    # install to specific directory for easier development
    cd $PLAYBOOK_DIR
    ansible-galaxy collection install git+https://github.com/ansibleguy/collection_systemd.git -p ./collections
