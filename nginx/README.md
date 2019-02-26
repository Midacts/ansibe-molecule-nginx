Role Name
=========

Simple nginx install and test travis CI example

Requirements
------------

debian

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

```yaml
# /home/user/roles/nginx/nginx.yml
---
- hosts: webservers
  roles:
  - /home/user/roles/nginx
```

``` bash
# Run the role
ansible-playbook nginx.yml
```

License
-------

MIT

Author Information
------------------

https://github.com/midacts
