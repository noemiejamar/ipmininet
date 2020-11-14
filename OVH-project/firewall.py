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

            # (telstra3,as1_r15)
            Rule('-A INPUT --src 2001:1:11:1600::/64 -d 2001:1:11:1401::/64 -j ACCEPT'),
            # (ntt3,as1_r14)
            Rule('-A INPUT --src 2001:1:11:1900::/64 -d 2001:1:11:1301::/64 -j ACCEPT'),
            # (equinix2,as1_r14)
            Rule('-A INPUT --src 2001:1:11:1800::/64 -d 2001:1:11:1302::/64 -j ACCEPT'),
            # (telstra1,as1_bb1)
            Rule('-A INPUT --src 2001:1:10:0800::/64 -d 2001:1:10:0302::/64 -j ACCEPT'),
            # (ntt1,as1_bb1)
            Rule('-A INPUT --src 2001:1:10:0900::/64 -d 2001:1:10:0303::/64 -j ACCEPT'),
            # (telstra2,as1_bb2)
            Rule('-A INPUT --src 2001:1:10:0A00::/64 -d 2001:1:10:0404::/64 -j ACCEPT'),
            # (ntt2,as1_bb2)
            Rule('-A INPUT --src 2001:1:10:0B00::/64 -d 2001:1:10:0405::/64 -j ACCEPT'),
            # (equinix1,as1_bb2)
            Rule('-A INPUT --src 2001:1:10:0C00::/64 -d 2001:1:10:0406::/64 -j ACCEPT'),

            # Log the dropped packets
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_bb1"'),
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_bb2"'),
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_r14"'),
            Rule('-A INPUT -j NFLOG --nflog-prefix "[DROP-INPUT]as1_r15"')
        ]
