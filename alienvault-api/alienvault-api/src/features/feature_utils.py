from ansiblemethods.ansiblemanager import Ansible
import subprocess as sub
import os


def touch_file(system_ip, filename):
    args = f"touch {filename}"
    a = Ansible()
    response = a.run_module(host_list=[system_ip], module="command", args=args)
    args = "touch %s" % filename
    try:
        if response['contacted'][system_ip]['rc']>0:
            return False
    except:
        return False
    finally:
        del a
    return True

def remotely_copy_file(system_ip, orig, dest):
    args = f"cp {orig} {dest}"
    a = Ansible()
    response = a.run_module(host_list=[system_ip], module="command", args=args)
    try:
        if response['contacted'][system_ip]['rc']>0:
            return False
    except:
        return False
    finally:
        del a
    return True


def remotely_backup_file(system_ip, orig,dest):
    return remotely_copy_file(system_ip, orig,dest)


def remotely_restore_file(system_ip, orig, dest):
    return remotely_copy_file(system_ip, orig,dest)


def remotely_create_sample_yml_file(system_ip):
    rawfile="""plugins:
- /etc/ossim/agent/plugins/pam_unix.cfg:
    DEFAULT: {cpe: 'cpe:/a:cpe_data', device: 10.9.8.12, device_id: AE298B1A-AF3F-11E3-9452-C242E4CCA548}
    config: {location: /var/log/alienvault/devices/10.9.8.12/10.9.8.12.log}
- /etc/ossim/agent/plugins/ssh.cfg:
    DEFAULT: {cpe: 'cpe:/a:cpe_data', device: 10.9.8.12, device_id: AE298B1A-AF3F-11E3-9452-C242E4CCA548}
    config: {location: /var/log/alienvault/devices/10.9.8.12/10.9.8.12.log}
- /etc/ossim/agent/plugins/cisco-asa.cfg:
    DEFAULT: {cpe: 'cpe:/a:cpe_data', device: 10.9.8.12, device_id: AE298B1A-AF3F-11E3-9452-C242E4CCA548}
    config: {location: /var/log/alienvault/devices/10.9.8.12/10.9.8.12.log}
- /etc/ossim/agent/plugins/cisco-pix.cfg:
    DEFAULT: {cpe: 'cpe:/a:cpe_data', device: 10.9.8.13, device_id: AE298B1A-AF3F-11E3-9452-C242E4CCA549}
    config: {location: /var/log/alienvault/devices/10.9.8.13/10.9.8.13.log}
- /etc/ossim/agent/plugins/apache.cfg:
    DEFAULT: {cpe: 'cpe:/a:cpe_data', device: 10.9.8.13, device_id: AE298B1A-AF3F-11E3-9452-C242E4CCA549}
    config: {location: /var/log/alienvault/devices/10.9.8.13/10.9.8.13.log}"""
    with open("/tmp/config_test.yml","w") as f:
        f.write(rawfile)
    return bool(
        remotely_copy_file(
            system_ip, "/tmp/config_test.yml", "/etc/ossim/agent/config.yml"
        )
    )

def remotely_create_sample_client_keys_file(system_ip):
    rawfile = "001 test_agent 10.1.1.1 436f12f28757e6eb67ddfd0a226380d2c04939238eff94f21369495f1cf8e3cc"
    with open("/tmp/client.keys","w") as f:
        f.write(rawfile)
    result = bool(
        remotely_copy_file(
            system_ip, "/tmp/client.keys", "/var/ossec/etc/client.keys"
        )
    )

    remotely_remove_file("127.0.0.1", "/tmp/client.keys")
    return result

def remotely_remove_file(system_ip, filename):
    args = f"rm -rf {filename}"
    a = Ansible()
    response = a.run_module(host_list=[system_ip], module="command", args=args)
    try:
        if response['contacted'][system_ip]['rc'] > 0:
            return False
    except:
        return False
    finally:
        del a
    return True


def run_system_command(cmd):
    try:
        p = sub.Popen(cmd, stdout=sub.PIPE, shell=True)
        (output, err) = p.communicate()
        if err is not None:
            print "Error " + str(err)
            return False
    except Exception as err:
        print str(err)
        return False
    return True


def set_plugin_add_hosts():
    current_path = os.path.dirname(os.path.realpath(__file__))
    add_sql = f"{current_path}/test_data/test_set_plugin_hosts.sql"
    cmd = f"/usr/bin/ossim-db < {add_sql} "
    return run_system_command(cmd)


def set_plugin_delete_hosts():
    current_path = os.path.dirname(os.path.realpath(__file__))
    sql = f"{current_path}/test_data/test_set_plugins_delete_hosts.sql"
    cmd = f"/usr/bin/ossim-db < {sql} "
    return run_system_command(cmd)
