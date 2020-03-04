#!/usr/bin/python

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True),
            port=dict(required=True, type='int'),
            timeout=dict(required=False, type='int', default=3)
        ),
        supports_check_mode=True
    )

    # In check mode, we take no action
    # Since this module never changes system state, we just
    # return changed=False
    if module.check_mode:
        module.exit_json(changed=False)

    host = module.params['host']
    port = module.params['port']
    timeout = module.params['timeout']

    if True:
        msg = "Custom module worked!"
        module.exit_json(msg=msg,changed=False)
    else:
        msg = "Could not reach %s:%s" % (host, port)
        module.fail_json(msg=msg)

from ansible.module_utils.basic import *
main()
