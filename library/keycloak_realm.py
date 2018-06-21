#!/usr/bin/env python

from ansible.module_utils.basic import *

def main():

	module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
        	server_url	=	dict(type='str', required=True),
        	login		=	dict(type='str', required=True),
        	password 	=	dict(type='str', required=True),
        )
    )
	module.exit_json(changed=False, meta=module.params)


if __name__ == '__main__':
    main()
