import pexpect
import sys
#getting into config
args = sys.argv
NEIGHBORSV6 = args[1]
TTL = args[2]
PASSWORD = args[3]
KALIVE = args[4]
TIMEOUT = args[5]

child = pexpect.spawn('telnet localhost 2605')
child.expect('Password:')
child.sendline('zebra')
child.sendline('enable')
child.sendline('configure terminal')
child.sendline('router bgp')
child.sendline('no neighbor ' + NEIGHBORSV6 + ' ebgp-multihop')
child.sendline('neighbor ' + NEIGHBORSV6 + ' ttl-security hops ' + TTL)
child.sendline('neighbor ' + NEIGHBORSV6 + ' password ' + PASSWORD)
child.sendline('neighbor ' + NEIGHBORSV6 + ' timers ' + KALIVE + ' ' + TIMEOUT)

child.sendline('exit')
child.kill(0)
