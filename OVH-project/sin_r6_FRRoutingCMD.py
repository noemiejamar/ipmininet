import pexpect
import sys, time

bgp_FRRouting = pexpect.spawn("telnet localhost 2605")
bgp_FRRouting.expect("Password:")
bgp_FRRouting.sendline('zebra')
bgp_FRRouting.sendline('enable')
bgp_FRRouting.sendline('configure terminal')
bgp_FRRouting.sendline('debug bgp neighbor-events')
bgp_FRRouting.sendline('router bgp')

Provider_TELSTRA = 'BABE:5:48::2'
ANYCAST2 = 'BABE:5:99::2'


# Route-maps

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + ' route-map rm' + str(0) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + '  route-map rm' + str(0) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + ANYCAST2 + ' route-map rm' + str(1) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + ANYCAST2 + '  route-map rm' + str(1) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')


# do not limit maximum prefix on providers
bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + ' maximum-prefix 300')  # to avoid prefix flooding
bgp_FRRouting.sendline('exit-address-family')

# Security

bgp_FRRouting.sendline('no neighbor ' + Provider_TELSTRA + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + ' ttl-security hops 1')
bgp_FRRouting.sendline('no neighbor ' + ANYCAST2 + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + ANYCAST2 + ' ttl-security hops 1')

bgp_FRRouting.sendline('exit')

# Default route-map

bgp_FRRouting.sendline('ipv6 access-list all permit any')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:80')
bgp_FRRouting.sendline('set local-preference 101')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:80')
bgp_FRRouting.sendline('set local-preference 101')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm2-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:82')
bgp_FRRouting.sendline('set local-preference 100')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm3-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:82')
bgp_FRRouting.sendline('set local-preference 100')
bgp_FRRouting.sendline('exit')

# anycast
bgp_FRRouting.sendline('route-map rm4-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:81')
bgp_FRRouting.sendline('set local-preference 111')
bgp_FRRouting.sendline('exit')

# Advertise only clients prefixes to peers and providers

bgp_FRRouting.sendline('bgp community-list standard FILTER-ipv6 deny 16276:80')  # peer
bgp_FRRouting.sendline('bgp community-list standard FILTER-ipv6 deny 16276:82')  # provider
bgp_FRRouting.sendline('bgp community-list standard FILTER-ipv6 permit internet')
bgp_FRRouting.sendline('bgp community-list standard NOFILTER-ipv6 permit internet')

bgp_FRRouting.sendline('route-map rm0-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community FILTER-ipv6')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community FILTER-ipv6')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm2-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community FILTER-ipv6')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm3-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community FILTER-ipv6')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm4-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community NOFILTER-ipv6')
bgp_FRRouting.sendline('exit')

# Set clients and peers local-pref

bgp_FRRouting.sendline('bgp community-list standard PEER_BACKUP permit 16276:105')
bgp_FRRouting.sendline('bgp community-list standard PEER permit 16276:110')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 20')
bgp_FRRouting.sendline('match community PEER_BACKUP')
bgp_FRRouting.sendline('set local-preference 105')
bgp_FRRouting.sendline('set community 16276:80')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 30')
bgp_FRRouting.sendline('match community PEER')
bgp_FRRouting.sendline('set local-preference 110')
bgp_FRRouting.sendline('set community 16276:80')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 20')
bgp_FRRouting.sendline('match community PEER_BACKUP')
bgp_FRRouting.sendline('set local-preference 105')
bgp_FRRouting.sendline('set community 16276:80')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 30')
bgp_FRRouting.sendline('match community PEER')
bgp_FRRouting.sendline('set local-preference 110')
bgp_FRRouting.sendline('set community 16276:80')
bgp_FRRouting.sendline('exit')

# Blackhole

bgp_FRRouting.sendline('bgp community-list standard BLACKHOLE permit 16276:666')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 deny 10')
bgp_FRRouting.sendline('match community BLACKHOLE')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 deny 10')
bgp_FRRouting.sendline('match community BLACKHOLE')
bgp_FRRouting.sendline('exit')

time.sleep(0.1)

bgp_FRRouting.kill(0)

