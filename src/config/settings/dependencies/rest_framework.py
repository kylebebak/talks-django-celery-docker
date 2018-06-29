REST_FRAMEWORK = {
}

# This setting is IMPORTANT: without it, rest_framework.reverse.reverse, can't
# correct protocol/scheme for absolute URLs it generates. If the server receives
# requests via load balancer, make sure the balancer forwards the protocol
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
