
from ipmininet.router.config.iptables import Rule

ip6_rules = [
            # Starting from scratch (flushing everything)
            Rule('-F INPUT'),
            Rule('-F OUTPUT'),
            Rule('-F FORWARD'),
            Rule('-F'),
            # Whitelisting policy Default=drop everything
            Rule('-P INPUT DROP'),
            Rule('-P FORWARD DROP'),
            Rule('-P OUTPUT DROP'),
            # Allow packets coming from related and established connections
            Rule('-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT'),
            Rule('-A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT'),
            Rule('-A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT'),
            # Allow local traffic
            # This allows iBGP (since it uses only lo)
            Rule('-A INPUT -i lo -j ACCEPT'),
            Rule('-A OUTPUT -o lo -j ACCEPT'),
            # Allow OSPF
            Rule('-A INPUT -p 89 -j ACCEPT'),
            Rule('-A OUTPUT -p 89 -j ACCEPT'),
            # Allow ICMPv6
            Rule('-A INPUT -p ipv6-icmp -j ACCEPT'),
            Rule('-A FORWARD -p ipv6-icmp -j ACCEPT'),
            Rule('-A OUTPUT -p ipv6-icmp -j ACCEPT'),
            # Allow eBGP from any client towards our ebgp router-interfaces

            # (syd_tel1,syd_bb1)
            Rule('-A INPUT --src BABE:8:49::2/64 -d BABE:8:49::1/64 -j ACCEPT'),
            # (syd_tel2,syd_bb2)
            Rule('-A INPUT --src BABE:9:50::2/64 -d BABE:9:50::1/64 -j ACCEPT'),
            # (syd_ntt1,syd_bb1)
            Rule('-A INPUT --src BABE:8:33::2/64 -d BABE:8:33::1/64 -j ACCEPT'),
            # (syd_ntt2,syd_bb1)
            Rule('-A INPUT --src babe:1:10:0800::/64 -d 2001:1:10:0302::/64 -j ACCEPT'),
            # (syd_eq,syd_bb2)
            Rule('-A INPUT --src BABE:9:17::2/64 -d BABE:9:17::1/64 -j ACCEPT'),
            # (sin_tel,sin_r6)
            Rule('-A INPUT --src BABE:5:48::2/64 -d BABE:5:48::1/64 -j ACCEPT'),
            # (sin_ntt,sin_r5)
            Rule('-A INPUT --src BABE:4:32::2/64 -d BABE:4:32::1/64 -j ACCEPT'),
            # (sin_eq,sin_r5)
            Rule('-A INPUT --src BABE:4:16::2/64 -d BABE:4:16::1/64 -j ACCEPT'),
            # (anycast,sin_r5)
            Rule('-A INPUT --src BABE:4:99::2/64 -d BABE:4:99::1/64 -j ACCEPT'),
            # (anycast,sin_r6)
            Rule('-A INPUT --src BABE:5:99::2/64 -d BABE:5:99::1/64 -j ACCEPT'),
            # (anycast,syd_bb1)
            Rule('-A INPUT --src BABE:8:99::2/64 -d BABE:8:99::1/64 -j ACCEPT'),
            # (anycast,syd_bb2)
            Rule('-A INPUT --src BABE:9:99::2/64 -d BABE:9:99::1/64 -j ACCEPT'),
            # (client1,sin_r5)
            Rule('-A INPUT --src BABE:4:96:1::2/64 -d BABE:4:96:1::1/64 -j ACCEPT'),
            # (client1b,sin_r5)
            Rule('-A INPUT --src BABE:4:96:2::2/64 -d BABE:4:96:2::1/64 -j ACCEPT'),
            # (client2,syd_bb1)
            Rule('-A INPUT --src BABE:8:97:1::2/64 -d BABE:8:97:1::1/64 -j ACCEPT'),
            # (client2b,syd_bb)
            Rule('-A INPUT --src BABE:8:97:2::2/64 -d BABE:8:97:2::1/64 -j ACCEPT'),
            # (client3,syd_bb2)
            Rule('-A INPUT --src BABE:9:98:1::2/64 -d BABE:9:98:1::1/64 -j ACCEPT'),
            # (client3b,syd_bb2)

            # Log the dropped packets
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_bb1"'),
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_bb2"'),
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_r14"'),
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_r15"')
        ]
