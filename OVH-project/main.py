#!/usr/bin/env python3
from ipmininet.ipnet import IPNet
from ipmininet.cli import IPCLI
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import BGP, OSPF6, OSPF, RouterConfig, AF_INET6, set_rr, AF_INET, IP6Tables
from ipmininet.router.config import ebgp_session, SHARE, CLIENT_PROVIDER, AccessList, CommunityList
from ipmininet.host.config import Named, ARecord, PTRRecord, AAAARecord
from ipaddress import ip_address

import ipmininet

from announced_prefixes import TELSTRA1_IPV4_ANNOUNCED_PREFIXES, TELSTRA2_IPV4_ANNOUNCED_PREFIXES, \
    TELSTRA3_IPV4_ANNOUNCED_PREFIXES, NTT1_IPV4_ANNOUNCED_PREFIXES, NTT2_IPV4_ANNOUNCED_PREFIXES, \
    NTT3_IPV4_ANNOUNCED_PREFIXES, EQUINIX1_IPV4_ANNOUNCED_PREFIXES, EQUINIX2_IPV4_ANNOUNCED_PREFIXES
from firewall import ip6_rules

domain = "ovh.com"
ipv6_server_address = 'BABE:b:0::'


class OVH(IPTopo):

    def build(self, *args, **kwargs):
        # Add all routers
        as1_bb1 = self.addRouter("as1_bb1", config=RouterConfig)  # sydsy2bb1a72
        as1_bb2 = self.addRouter("as1_bb2", config=RouterConfig)  # sydsy2bb2a72
        as1_r3 = self.addRouter("as1_r3", config=RouterConfig)  # syd1sy2g1nc5
        as1_r4 = self.addRouter("as1_r4", config=RouterConfig)  # syd1sy2g2nc5
        as1_r5 = self.addRouter("as1_r5", config=RouterConfig)  # sydsy2rr1ucs
        as1_r6 = self.addRouter("as1_r6", config=RouterConfig)  # sydsy2rr2ucs
        as1_r7 = self.addRouter("as1_r7", config=RouterConfig)  # laxla1bb1n7
        as1_r8 = self.addRouter("as1_r8", config=RouterConfig)  # sjosv5bb1n7
        as1_r9 = self.addRouter("as1_r9", config=RouterConfig)  # mrsmrsbb1a72
        as1_r10 = self.addRouter("as1_r10", config=RouterConfig)  # sinsg1sbb1nc5
        as1_r11 = self.addRouter("as1_r11", config=RouterConfig)  # singss1sbb1nc5
        as1_r12 = self.addRouter("as1_r12", config=RouterConfig)  # sinsgcs2g1nc5
        as1_r13 = self.addRouter("as1_r13", config=RouterConfig)  # sin1sgcs2g2nc5
        as1_r14 = self.addRouter("as1_r14", config=RouterConfig)  # sinsg1pb1nc5
        as1_r15 = self.addRouter("as1_r15", config=RouterConfig)  # singss1pb1nc5
        ntt1 = self.addRouter("ntt1", config=RouterConfig)
        ntt2 = self.addRouter("ntt2", config=RouterConfig)
        ntt3 = self.addRouter("ntt3", config=RouterConfig)
        equinix1 = self.addRouter("equinix1", config=RouterConfig)
        equinix2 = self.addRouter("equinix2", config=RouterConfig)
        telstra1 = self.addRouter("telstra1", config=RouterConfig)
        telstra2 = self.addRouter("telstra2", config=RouterConfig)
        telstra3 = self.addRouter("telstra3", config=RouterConfig)

        # --- Hosts ---
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        server = self.addHost('server')
        master = self.addHost('master')
        slave = self.addHost('slave')

        all_routers = [as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5, as1_r6, as1_r7,
                       as1_r8, as1_r9, as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15, ntt1, ntt2, ntt3, equinix1,
                       equinix2, telstra1, telstra2, telstra3]

        self.add_ospf(all_routers)
        self.add_bgp(all_routers, [as1_bb1, as1_bb2, as1_r14, as1_r15], [ntt1], [ntt2], [ntt3], [equinix1], [equinix2],
                     [telstra1], [telstra2], [telstra3])

        self.addAS(16276, tuple([as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5, as1_r6, as1_r7,
                                 as1_r8, as1_r9, as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15]))
        self.addAS(2, tuple([ntt1, ntt2, ntt3]))
        self.addAS(3, tuple([equinix1, equinix2]))
        self.addAS(4, tuple([telstra1, telstra2, telstra3]))

        # Add Links

        self.addLink(as1_bb1, as1_bb2, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:0/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:1/64"})
        self.addLink(as1_bb1, as1_r5, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:2/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:3/64"})
        self.addLink(as1_bb1, as1_r3, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:4/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:5/64"})
        self.addLink(as1_bb1, as1_r10, igp_metric=3, params1={"ip": "BABE:b:0:0:0:0:0:6/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:7/64"})
        self.addLink(as1_bb2, as1_r6, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:8/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:9/64"})
        self.addLink(as1_bb2, as1_r4, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:a/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:b/64"})
        self.addLink(as1_bb2, as1_r7, igp_metric=5, params1={"ip": "BABE:b:0:0:0:0:0:c/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:d/64"})
        self.addLink(as1_bb2, as1_r11, igp_metric=3, params1={"ip": "BABE:b:0:0:0:0:0:e/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:f/64"})
        self.addLink(as1_r3, as1_r4, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:10/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:11/64"})
        self.addLink(as1_r3, as1_r12, igp_metric=3, params1={"ip": "BABE:b:0:0:0:0:0:12/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:13/64"})
        self.addLink(as1_r7, as1_r8, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:14/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:15/64"})
        self.addLink(as1_r8, as1_r11, igp_metric=5, params1={"ip": "BABE:b:0:0:0:0:0:16/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:17/64"})
        self.addLink(as1_r10, as1_r11, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:18/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:19/64"})
        self.addLink(as1_r10, as1_r14, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:1a/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:1b/64"})
        self.addLink(as1_r10, as1_r9, igp_metric=5, params1={"ip": "BABE:b:0:0:0:0:0:1c/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:1d/64"})
        self.addLink(as1_r10, as1_r12, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:20/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:21/64"})
        self.addLink(as1_r11, as1_r13, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:22/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:23/64"})
        self.addLink(as1_r11, as1_r15, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:24/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:25/64"})
        self.addLink(as1_r11, as1_r9, igp_metric=5, params1={"ip": "BABE:b:0:0:0:0:0:26/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:27/64"})
        self.addLink(as1_r12, as1_r13, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:28/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:29/64"})

        # inter AS links
        self.addLink(as1_bb1, telstra1, params1={"ip": "BABE:b:0:0:0:0:0:2a/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:2b/64"})
        self.addLink(as1_bb1, ntt1, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:2c/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:2d/64"})
        self.addLink(as1_bb2, telstra2, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:2e/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:2f/64"})
        self.addLink(as1_bb2, ntt2, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:30/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:31/64"})
        self.addLink(as1_bb2, equinix1, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:32/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:33/64"})
        self.addLink(as1_r14, ntt3, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:34/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:35/64"})
        self.addLink(as1_r14, equinix2, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:36/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:37/64"})
        self.addLink(as1_r15, telstra3, igp_metric=1, params1={"ip": "BABE:b:0:0:0:0:0:38/64"},
                     params2={"ip": "BABE:b:0:0:0:0:0:39/64"})

        # add eBGP session between AS
        ebgp_session(self, as1_bb1, telstra1, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb1, ntt1, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb2, telstra2, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb2, ntt2, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb2, equinix1, link_type=SHARE)
        ebgp_session(self, as1_r14, ntt3, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_r14, equinix2, link_type=SHARE)
        ebgp_session(self, as1_r15, telstra3, link_type=CLIENT_PROVIDER)

        # two-layers RR
        peers_rr1 = [as1_bb1, as1_bb2, as1_r3, as1_r4]
        peers_rr2 = [as1_bb2, as1_bb1, as1_r3, as1_r4]
        peers_rr3 = [as1_r14, as1_r12, as1_r13, as1_r15]
        peers_rr4 = [as1_r12, as1_r13, as1_r14, as1_r15]
        self.add_router_reflector(as1_r5, peers_rr1)
        self.add_router_reflector(as1_r6, peers_rr2)
        self.add_router_reflector(as1_r10, peers_rr3)
        self.add_router_reflector(as1_r11, peers_rr4)

        # add links to the hosts
        self.addLink(h1, telstra1, igp_metric=1)
        self.addLink(h2, equinix1, igp_metric=1)
        self.addLink(as1_r3, server, igp_metric=1)
        self.addLink(as1_bb1, master, igp_metric=1)
        self.addLink(as1_bb2, slave, igp_metric=1)

        # add subnets to the hosts
        self.addSubnet(nodes=[telstra1, h1], subnets=["BABE:b::/64"])
        self.addSubnet(nodes=[equinix1, h2], subnets=["BABE:b::/64"])
        self.addSubnet(nodes=[as1_r3, server], subnets=["BABE:b::/64"])
        self.addSubnet(nodes=[as1_bb1, master], subnets=["BABE:b::/64"])
        self.addSubnet(nodes=[as1_bb2, slave], subnets=["BABE:b::/64"])

        # --- DNS network---

        # ipv4_server_address = '139.99.0.50'  # routerID starts at 50 for hosts

        master.addDaemon(Named)
        slave.addDaemon(Named)

        # Declare a new DNS Zone

        records = [
            # ARecord(server, ipv4_server_address, ttl=120),
            AAAARecord(server, ipv6_server_address, ttl=120)
        ]
        self.addDNSZone(name=domain, dns_master=master,
                        dns_slaves=[slave], nodes=[server], records=records)

        ptr_records = [
            # PTRRecord(ipv4_server_address, server + f".{domain}", ttl=120),
            PTRRecord(ipv6_server_address, server + f".{domain}", ttl=120)
        ]
        # reverse_domain_name_v4 = ip_address(ipv4_server_address).reverse_pointer[-10:]
        reverse_domain_name_v6 = ip_address(ipv6_server_address).reverse_pointer[-10:]
        # self.addDNSZone(name=reverse_domain_name_v4, dns_master=master,
        #                dns_slaves=[slave], records=ptr_records,
        #                ns_domain_name=domain, retry_time=8200)
        self.addDNSZone(name=reverse_domain_name_v6, dns_master=master,
                        dns_slaves=[slave], records=ptr_records,
                        ns_domain_name=domain, retry_time=8200)

        # firewall table
        as1_bb1.addDaemon(IP6Tables, rules=ip6_rules)
        as1_bb2.addDaemon(IP6Tables, rules=ip6_rules)
        as1_r14.addDaemon(IP6Tables, rules=ip6_rules)
        as1_r15.addDaemon(IP6Tables, rules=ip6_rules)

        # --- Communities---

        # local_pref=CommunityList('loca-pref','16276:80')
        al = AccessList(name='all', entries=('any',))

        as1_r3.get_config(BGP)\
            .set_community('16276:80', to_peer=as1_bb1, matching=(al,))\
            .set_community('16276:80', to_peer=as1_r4, matching=(al,)) \
            .set_community('16276:70', to_peer=as1_r12, matching=(al,))
        local_pref_SIN = CommunityList('loc_pref', '16276:70')
        local_pref_SYD = CommunityList('loc_pref', '16276:80')
        as1_bb1.get_config(BGP) \
            .set_local_pref(80, from_peer=as1_r3, matching=(local_pref_SYD,))

        as1_r12.get_config(BGP) \
            .set_local_pref(70, from_peer=as1_r3, matching=(local_pref_SIN,))


        super().build(*args, **kwargs)

    def add_bgp(self, all_routers, routers_with_ebgp, telstra1, telstra2, telstra3, ntt1, ntt2, ntt3, equinix1,
                equinix2):
        family_ipv4 = AF_INET()
        family_ipv6 = AF_INET6()
        router_id = "1.1.1."
        i = 0
        for r in all_routers:
            r.addDaemon(BGP, address_families=(family_ipv4, family_ipv6))
        for r in routers_with_ebgp:
            i += 1
            r.addDaemon(BGP, routerid=router_id + str(i), family=AF_INET(redistribute=("ospf", "connected"), ))
            r.addDaemon(BGP, routerid=router_id + str(i), family=AF_INET6(redistribute=("ospf6", "connected"), ))

        # clients ASes advertised prefixes
        for r in telstra1:
            r.addDaemon(BGP, family=TELSTRA1_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:babe::/32",), ))
        for r in telstra2:
            r.addDaemon(BGP, family=TELSTRA2_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:beba::/32",), ))
        for r in telstra3:
            r.addDaemon(BGP, family=TELSTRA3_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:bebe::/32",), ))
        for r in ntt1:
            r.addDaemon(BGP, family=NTT1_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:bfbf::/32",), ))
        for r in ntt2:
            r.addDaemon(BGP, family=NTT2_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:fbfb::/32",), ))
        for r in ntt3:
            r.addDaemon(BGP, family=NTT3_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:beaf::/32",), ))
        for r in equinix1:
            r.addDaemon(BGP, family=EQUINIX1_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:baef::/32",), ))
        for r in equinix2:
            r.addDaemon(BGP, family=EQUINIX2_IPV4_ANNOUNCED_PREFIXES)
            r.addDaemon(BGP, family=AF_INET6(networks=("dead:baaf::/32",), ))

    def add_ospf(self, all_routers):

        for router in all_routers:
            router.addDaemon(OSPF)
            router.addDaemon(OSPF6)

    def add_router_reflector(self, router_reflector, clients_list):

        set_rr(self, rr=router_reflector, peers=clients_list)


# Press the green button to run the script.
if __name__ == '__main__':
    net = IPNet(topo=OVH(), use_v4=True, use_v6=True, allocate_IPs=False)
    try:
        net.start()
        IPCLI(net)
    finally:
        net.stop()
