#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import socket

def main():
    module = AnsibleModule(
        argument_spec=dict(
            port=dict(type='int', required=True)
        )
    )
    
    port = module.params['port']
    
    # порт от 1 до 65535
    if port < 1 or port > 65535:
        module.fail_json(msg=f"Порт {port} должен быть от 1 до 65535")
    
    # порт не занят
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    
    if result == 0:
        module.fail_json(msg=f"Порт {port} уже используется")
    
    # все ок
    module.exit_json(
        changed=False,
        valid_port=port,
        msg=f"Порт {port} свободен и готов к использованию"
    )

if __name__ == '__main__':
    main()