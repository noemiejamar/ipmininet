import pexpect
import sys, time

bgp_FRRouting = pexpect.spawn("telnet localhost 2605")
bgp_FRRouting.expect("Password:")
bgp_FRRouting.sendline('zebra')
bgp_FRRouting.sendline('enable')
bgp_FRRouting.sendline('configure terminal')
bgp_FRRouting.sendline('debug bgp neighbor-events')
bgp_FRRouting.sendline('router bgp')

Peer_NTT = 'BABE:8:33::2'
Provider_TELSTRA = 'BABE:8:49::2'
CLIENT2 = 'BABE:8:97:1::2'
CLIENT2b = 'BABE:8:97:2::2'
ANYCAST3 = 'BABE:8:99::2'



# Route-maps

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + Peer_NTT + ' route-map rm' + str(0) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + Peer_NTT + '  route-map rm' + str(0) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + ' route-map rm' + str(1) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + '  route-map rm' + str(1) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + CLIENT2 + ' route-map rm' + str(2) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + CLIENT2 + '  route-map rm' + str(2) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + CLIENT2b + ' route-map rm' + str(3) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + CLIENT2b + '  route-map rm' + str(3) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + ANYCAST3 + ' route-map rm' + str(4) + '-in-ipv6 in')
bgp_FRRouting.sendline('neighbor ' + ANYCAST3 + '  route-map rm' + str(4) + '-out-ipv6 out')
bgp_FRRouting.sendline('exit-address-family')

# only for client
bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + CLIENT2 + ' prefix-list client2 in')  # limit the prefix accepted by client
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + CLIENT2b + ' prefix-list client2 in')  # limit the prefix accepted by client
bgp_FRRouting.sendline('exit-address-family')

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + Peer_NTT + ' maximum-prefix 300')  # to avoid prefix flooding
bgp_FRRouting.sendline('exit-address-family')

# Security

bgp_FRRouting.sendline('no neighbor ' + Peer_NTT + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + Peer_NTT + ' ttl-security hops 1')

bgp_FRRouting.sendline('no neighbor ' + Provider_TELSTRA + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + Provider_TELSTRA + ' ttl-security hops 1')

bgp_FRRouting.sendline('no neighbor ' + CLIENT2 + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + CLIENT2 + ' ttl-security hops 1')

bgp_FRRouting.sendline('no neighbor ' + CLIENT2b + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + CLIENT2b + ' ttl-security hops 1')

bgp_FRRouting.sendline('no neighbor ' + ANYCAST3 + ' ebgp-multihop')
bgp_FRRouting.sendline('neighbor ' + ANYCAST3 + ' ttl-security hops 1')

bgp_FRRouting.sendline('exit')

# limit as-path for clients
# regex used to accept directly connected AS to client1
bgp_FRRouting.sendline('bgp as-path access-list client2 permit ^2_[0-9]*$')  # AS 2 is the AS of client2

bgp_FRRouting.sendline('ip prefix-list client2 permit BABE:1:0020:2::0/64')

# Default route-map

bgp_FRRouting.sendline('ipv6 access-list all permit any')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:800')
bgp_FRRouting.sendline('set local-preference 101')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:800')
bgp_FRRouting.sendline('set local-preference 101')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm2-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:802')
bgp_FRRouting.sendline('set local-preference 100')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm3-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:802')
bgp_FRRouting.sendline('set local-preference 100')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm4-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('match as-path client2')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set community 16276:801 16276:1502 16276:1503')
bgp_FRRouting.sendline('set local-preference 111')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm5-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('match as-path client2')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set community 16276:801 16276:1502 16276:1503')
bgp_FRRouting.sendline('set local-preference 111')
bgp_FRRouting.sendline('exit')

# anycast
bgp_FRRouting.sendline('route-map rm6-in-ipv6 permit 100')
bgp_FRRouting.sendline('match ipv6 address all')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set local-preference 111')
bgp_FRRouting.sendline('exit')

# Advertise only clients prefixes to peers and providers

bgp_FRRouting.sendline('bgp community-list standard FILTER-ipv6 deny 16276:800')  # peer
bgp_FRRouting.sendline('bgp community-list standard FILTER-ipv6 deny 16276:802')  # provider
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

bgp_FRRouting.sendline('route-map rm5-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community NOFILTER-ipv6')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm6-out-ipv6 permit 10')
bgp_FRRouting.sendline('match community NOFILTER-ipv6')
bgp_FRRouting.sendline('exit')

# Set clients and peers local-pref

bgp_FRRouting.sendline('bgp community-list standard PEER_BACKUP permit 16276:105')
bgp_FRRouting.sendline('bgp community-list standard PEER permit 16276:110')
bgp_FRRouting.sendline('bgp community-list standard CUSTOMER_BACKUP permit 16276:115')
bgp_FRRouting.sendline('bgp community-list standard CUSTOMER permit 16276:120')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 20')
bgp_FRRouting.sendline('match community PEER_BACKUP')
bgp_FRRouting.sendline('set local-preference 105')
bgp_FRRouting.sendline('set community 16276:800')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 30')
bgp_FRRouting.sendline('match community PEER')
bgp_FRRouting.sendline('set local-preference 110')
bgp_FRRouting.sendline('set community 16276:800')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 20')
bgp_FRRouting.sendline('match community PEER_BACKUP')
bgp_FRRouting.sendline('set local-preference 105')
bgp_FRRouting.sendline('set community 16276:800')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 30')
bgp_FRRouting.sendline('match community PEER')
bgp_FRRouting.sendline('set local-preference 110')
bgp_FRRouting.sendline('set community 16276:800')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm4-in-ipv6 permit 20')
bgp_FRRouting.sendline('match community CUSTOMER_BACKUP')
bgp_FRRouting.sendline('match as-path client2')
bgp_FRRouting.sendline('set local-preference 115')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set community 16276:801 16276:1502 16276:1503')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm4-in-ipv6 permit 30')
bgp_FRRouting.sendline('match community CUSTOMER')
bgp_FRRouting.sendline('match as-path client2')
bgp_FRRouting.sendline('set local-preference 120')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set community 16276:801 16276:1502 16276:1503')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm5-in-ipv6 permit 20')
bgp_FRRouting.sendline('match community CUSTOMER_BACKUP')
bgp_FRRouting.sendline('match as-path client2')
bgp_FRRouting.sendline('set local-preference 115')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set community 16276:801 16276:1502 16276:1503')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm5-in-ipv6 permit 30')
bgp_FRRouting.sendline('match community CUSTOMER')
bgp_FRRouting.sendline('match as-path client2')
bgp_FRRouting.sendline('set local-preference 120')
bgp_FRRouting.sendline('set community 16276:801')
bgp_FRRouting.sendline('set community 16276:801 16276:1502 16276:1503')
bgp_FRRouting.sendline('exit')

# Blackhole

bgp_FRRouting.sendline('bgp community-list standard BLACKHOLE permit 16276:666')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 deny 10')
bgp_FRRouting.sendline('match community BLACKHOLE')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 deny 10')
bgp_FRRouting.sendline('match community BLACKHOLE')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm4-in-ipv6 deny 10')
bgp_FRRouting.sendline('match community BLACKHOLE')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm5-in-ipv6 deny 10')
bgp_FRRouting.sendline('match community BLACKHOLE')
bgp_FRRouting.sendline('exit')

time.sleep(0.1)

bgp_FRRouting.kill(0)
