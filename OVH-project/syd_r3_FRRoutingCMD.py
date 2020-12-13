import pexpect
import sys

bgp_FRRouting = pexpect.spawn("telnet localhost 2605")
bgp_FRRouting.expect("Password:")
bgp_FRRouting.sendline('zebra')
bgp_FRRouting.sendline('enable')
bgp_FRRouting.sendline('configure terminal')
bgp_FRRouting.sendline('debug bgp neighbor-events')
bgp_FRRouting.sendline('router bgp')

sin_r3 = 'BABE:0:6::1'


# Route-maps

bgp_FRRouting.sendline('address-family ipv6 unicast')
bgp_FRRouting.sendline('neighbor ' + sin_r3 + ' route-map rm'+str(0)+'-in-ipv6 in')
bgp_FRRouting.sendline('exit-address-family')



bgp_FRRouting.sendline('exit')

# Filter regions

bgp_FRRouting.sendline('bgp community-list standard FILTER-AUS-ipv6 deny 16276:1501')
bgp_FRRouting.sendline('bgp community-list standard FILTER-AUS-ipv6 permit internet')

bgp_FRRouting.sendline('route-map rm0-in-ipv6 permit 10')
bgp_FRRouting.sendline('match community FILTER-AUS-ipv6')
bgp_FRRouting.sendline('exit')

bgp_FRRouting.sendline('route-map rm1-in-ipv6 permit 10')
bgp_FRRouting.sendline('match community FILTER-AUS-ipv6')
bgp_FRRouting.sendline('exit')

time.sleep(0.1)

bgp_FRRouting.kill(0)
