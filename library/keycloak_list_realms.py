#!/usr/bin/env python

from ansible.module_utils.basic import *

def main():

	module = AnsibleModule(
        argument_spec = dict(
        	server_url	=	dict(type='str', required=True),
        	login		=	dict(type='str', required=True),
        	password 	=	dict(type='str', required=True, no_log=True),
        )
    )
	module.exit_json(changed=False, meta=module.params)


if __name__ == '__main__':
    main()
