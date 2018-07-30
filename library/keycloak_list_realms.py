#!/usr/bin/env python

from ansible.module_utils.keycloak import camel, keycloak_argument_spec
from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.keycloak_admin import KeycloakAdminAPI


URL_REALMS = "{url}/admin/realms"


def sanitize_cr(clientrep):
    """ Removes probably sensitive details from a client representation
    :param clientrep: the clientrep dict to be sanitized
    :return: sanitized clientrep dict
    """
    result = clientrep.copy()
    if 'secret' in result:
        result['secret'] = 'no_log'
    if 'attributes' in result:
        if 'saml.signing.private.key' in result['attributes']:
            result['attributes']['saml.signing.private.key'] = 'no_log'
    return result


def main():
    """
    Module execution
    :return:
    """
    argument_spec = keycloak_argument_spec()

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    result = dict(changed=False, msg='', diff={}, proposed={}, existing={}, end_state={})

    # Obtain access token, initialize API
    kc = KeycloakAdminAPI(module)

    realm = module.params.get('realm')
    cid = module.params.get('id')
    state = module.params.get('state')

    # convert module parameters to client representation parameters (if they belong in there)
    client_params = [x for x in module.params
                     if x not in list(keycloak_argument_spec().keys()) + ['state', 'realm'] and module.params.get(x) is not None]
    keycloak_argument_spec().keys()

    result = dict()
    result['realms'] = kc.get_realms()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
