import json
import requests

from solar.core.log import log


def test(resource):
    log.debug('Testing glance_puppet')
    res = requests.get(
        'http://%s:9292' % resource.args['ip'].value
    )

    token_data = requests.post(
        'http://%s:%s/v2.0/tokens' % (resource.args['keystone_host'].value,
                                      resource.args['keystone_port'].value),
        json.dumps({
            'auth': {
                'tenantName': resource.args['tenant_name'].value,
                'passwordCredentials': {
                    'username': resource.args['user_name'].value,
                    'password': resource.args['user_password'].value,
                    },
                },
            }),
        headers={'Content-Type': 'application/json'}
    )

    token = token_data.json()['access']['token']['id']

    print res.json()
