import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_is_installed(host):
    assert host.package('nginx').is_installed


def test_nginx_is_running(host):
    assert host.service('nginx').is_running


def test_nginx_is_enabled(host):
    assert host.service('nginx').is_enabled
