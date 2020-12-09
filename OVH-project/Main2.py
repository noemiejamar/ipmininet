#!/usr/bin/env python3

from ipmininet.ipnet import IPNet
from ipmininet.cli import IPCLI
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import *
from ipmininet.router.config.iptables import *

class Net(IPTopo):

    def build(self, *args, **kwargs):
        # Add routers
        # todo fix ipv4
        # -----------------------------------------------------------------------------------------------------
        # Singapore Routers   BABE:1:00YM    Y = 0 -> for loopback   M = 0 -> for Singapore 139.99.0
        # -----------------------------------------------------------------------------------------------------
        sin_r1 = self.add_config_router('sin_r1', ["BABE:1:0000::1/128", "139.99.0.1/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0000::/64',), ))
        sin_r2 = self.add_config_router('sin_r2', ["BABE:1:0000::2/128", "139.99.0.2/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0000::/64',), ))
        sin_r3 = self.add_config_router('sin_r3', ["BABE:1:0000::3/128", "139.99.0.3/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0000::/64',), ))
        sin_r4 = self.add_config_router('sin_r4', ["BABE:1:0000::4/128", "139.99.0.4/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0000::/64',), ))
        sin_r5 = self.add_config_router('sin_r5', ["BABE:1:0000::5/128", "139.99.0.5/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0000::/64',), ))
        sin_r6 = self.add_config_router('sin_r6', ["BABE:1:0000::6/128", "139.99.0.6/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0000::/64',), ))
        # -----------------------------------------------------------------------------------------------------
        # Australia Routers  BABE:1:00YM    Y = 0 -> for loopback   M = 1 -> for Australia 139.99.0
        # -----------------------------------------------------------------------------------------------------
        syd_bb1 = self.add_config_router('syd_bb1', ["BABE:1:0001::1/128", "139.99.0.7/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0001::/64',), ))
        syd_bb2 = self.add_config_router('syd_bb2', ["BABE:1:0001::2/128", "139.99.0.8/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0001::/64',), ))
        syd_r3 = self.add_config_router('syd_r3', ["BABE:1:0001::3/128", "139.99.0.9/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0001::/64',), ))
        syd_r4 = self.add_config_router('syd_r4', ["BABE:1:0001::4/128", "139.99.0.10/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0001::/64',), ))
        syd_r5 = self.add_config_router('syd_r5', ["BABE:1:0001::5/128", "139.99.0.11/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0001::/64',), ))
        syd_r6 = self.add_config_router('syd_r6', ["BABE:1:0001::6/128", "139.99.0.12/32"],
                                        family4=AF_INET(networks=('139.99.0.0/17',), ),
                                        family6=AF_INET6(networks=('BABE:1:0001::/64',), ))
        # -----------------------------------------------------------------------------------------------------
        # inter AS Routers /(telstra = BABE:1:0005/139.98.0)/(equinix = BABE:1:0007/139.96.0)/
        # -----------------------------------------------------------------------------------------------------
        syd_tel1 = self.add_config_router('syd_tel1', ["BABE:1:0005::1/128", "139.98.0.1/32"],
                                        family4=AF_INET(networks=('139.98.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0005::/64',), ))
        syd_tel2 = self.add_config_router('syd_tel2', ["BABE:1:0005::2/128", "139.98.0.2/32"],
                                        family4=AF_INET(networks=('139.98.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0005::/64',), ))
        syd_ntt1 = self.add_config_router('syd_ntt1', ["BABE:1:0006::1/128", "139.97.0.1/32"],
                                        family4=AF_INET(networks=('139.97.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0006::/64',), ))
        syd_eq = self.add_config_router('syd_eq', ["BABE:1:0007::1/128", "139.96.0.1/32"],
                                        family4=AF_INET(networks=('139.96.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0007::/64',), ))
        syd_ntt2 = self.add_config_router('syd_ntt2', ["BABE:1:0006::2/128", "139.97.0.2/32"],
                                        family4=AF_INET(networks=('139.97.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0006::/64',), ))
        # -----------------------------------------------------------------------------------------------------
        # NTT = BABE:1:0006 / 139.96.0
        # -----------------------------------------------------------------------------------------------------
        sin_eq = self.add_config_router('sin_eq', ["BABE:1:0007::2/128", "139.96.0.2/32"],
                                        family4=AF_INET(networks=('139.96.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0007::/64',), ))
        sin_ntt = self.add_config_router('sin_ntt', ["BABE:1:0006::3/128", "139.97.0.3/32"],
                                        family4=AF_INET(networks=('139.97.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0006::/64',), ))
        sin_tel = self.add_config_router('sin_tel', ["BABE:1:0005::3/128", "139.98.0.3/32"],
                                        family4=AF_INET(networks=('139.98.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0005::/64',), ))
        # todo ipv4 (change)
        # -----------------------------------------------------------------------------------------------------
        # France Routers   BABE:1:00YM =  Y = o -> for loopback   M = 2 -> for France / 139.95.0
        # -----------------------------------------------------------------------------------------------------
        mrs = self.add_config_router('mrs', ["BABE:1:0002::1/128", "139.95.0.1/32"],
                                        family4=AF_INET(networks=('139.95.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0002::/64',), ))
        # -----------------------------------------------------------------------------------------------------
        # USA Routers      BABE:1:00YM =  Y = o -> for loopback   M = 3 -> for USA / 139.94.0
        # -----------------------------------------------------------------------------------------------------
        lax = self.add_config_router('lax', ["BABE:1:0003::1/128", "139.94.0.1/32"],
                                        family4=AF_INET(networks=('139.94.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0003::/64',), ))
        sjo = self.add_config_router('sjo', ["BABE:1:0003::2/128", "139.94.0.2/32"],
                                        family4=AF_INET(networks=('139.94.0.0/24',), ),
                                        family6=AF_INET6(networks=('BABE:1:0003::/64',), ))
        # -----------------------------------------------------------------------------------------------------
        # Customers Routers  BABE:1:00YM =  Y = 2 -> for customers / 139.93.1 / +++++ from here +++++++
        # -----------------------------------------------------------------------------------------------------
        client1 = self.add_config_router('client1', ["2600:1f00::0/128", "153.1.15.0/32"],
                                        family4=AF_INET(networks=('153.1.15.0/24',), ),
                                        family6=AF_INET6(networks=('2600:1f00::0/32', '2600:1f01::0/32',), ))
        client1b = self.add_config_router('client1b', ["2600:1f00::1/128", "153.1.15.1/32"],
                                        family4=AF_INET(networks=('153.1.15.0/24',), ),
                                        family6=AF_INET6(networks=('2600:1f00::0/32', '2600:1f01::0/32',), ))

        client2 = self.add_config_router('client2', ["2600:2f00::0/128", "153.2.15.0/32"],
                                        family4=AF_INET(networks=('153.2.15.0/24',), ),
                                        family6=AF_INET6(networks=('2600:2f00::0/32',), ))
        client2b = self.add_config_router('client2b', ["2600:2f00::1/128", "153.2.15.1/32"],
                                        family4=AF_INET(networks=('153.2.15.0/24',), ),
                                        family6=AF_INET6(networks=('2600:2f00::0/32',), ))

        client3 = self.add_config_router('client3', ["2600:3f00::0/128", "153.3.15.0/32"],
                                        family4=AF_INET(networks=('153.3.15.0/24',), ),
                                        family6=AF_INET6(networks=('2600:3f00::0/32',), ))
        client3b = self.add_config_router('client3b', ["2600:3f00::1/128", "153.3.15.1/32"],
                                        family4=AF_INET(networks=('153.3.15.0/24',), ),
                                        family6=AF_INET6(networks=('2600:3f00::0/32',), ))
        


        ###################
        # anycast rooters #
        ###################

        anycast1 = self.addRouter("anycast1", config=RouterConfig, lo_addresses=["2700:1f00::0/64", "173.1.15.0/32"])
        anycast2 = self.addRouter("anycast2", config=RouterConfig, lo_addresses=["2700:1f00::0/64", "173.1.15.0/32"])
        anycast3 = self.addRouter("anycast3", config=RouterConfig, lo_addresses=["2700:1f00::0/64", "173.1.15.0/32"])
        anycast4 = self.addRouter("anycast4", config=RouterConfig, lo_addresses=["2700:1f00::0/64", "173.1.15.0/32"])

        # Add BGP
        anycast1.addDaemon(BGP, address_families=(
            AF_INET6(networks=("2700:1f00::0/32",)), AF_INET(networks=('173.1.15.0/24',))))
        anycast2.addDaemon(BGP, address_families=(
            AF_INET6(networks=("2700:1f00::0/32",)), AF_INET(networks=('173.1.15.0/24',))))
        anycast3.addDaemon(BGP, address_families=(
            AF_INET6(networks=("2700:1f00::0/32",)), AF_INET(networks=('173.1.15.0/24',))))
        anycast4.addDaemon(BGP, address_families=(
            AF_INET6(networks=("2700:1f00::0/32",)), AF_INET(networks=('173.1.15.0/24',))))

        # In the same AS
        self.addAS(12345, (anycast1,))
        self.addAS(12345, (anycast2,))
        self.addAS(12345, (anycast3,))
        self.addAS(12345, (anycast4,))

        sin_r5_anycast1 = self.addLink(sin_r5, anycast1)
        sin_r5_anycast1['sin_r5'].addParams(ip=('10.4.99.1/24', 'fc00:4:99::1/64'))
        sin_r5_anycast1['anycast1'].addParams(ip=('10.4.99.2/24', 'fc00:4:99::2/64'))

        sin_r6_anycast2 = self.addLink(sin_r6, anycast2)
        sin_r6_anycast2['sin_r6'].addParams(ip=('10.5.99.1/24', 'fc00:5:99::1/64'))
        sin_r6_anycast2['anycast2'].addParams(ip=('10.5.99.2/24', 'fc00:5:99::2/64'))

        syd_bb1_anycast3 = self.addLink(syd_bb1, anycast3)
        syd_bb1_anycast3['syd_bb1'].addParams(ip=('10.8.99.1/24', 'fc00:8:99::1/64'))
        syd_bb1_anycast3['anycast3'].addParams(ip=('10.8.99.2/24', 'fc00:8:99::2/64'))

        syd_bb2_anycast4 = self.addLink(syd_bb2, anycast4)
        syd_bb2_anycast4['syd_bb2'].addParams(ip=('10.9.99.1/24', 'fc00:9:99::1/64'))
        syd_bb2_anycast4['anycast4'].addParams(ip=('10.9.99.2/24', 'fc00:9:99::2/64'))

        # eBGP anycast
        ebgp_session(self, anycast1, sin_r5)
        ebgp_session(self, anycast2, sin_r6)
        ebgp_session(self, anycast3, syd_bb1)
        ebgp_session(self, anycast4, syd_bb2)

        # OVH links

        sin_r3_syd_r3 = self.addLink(sin_r3, syd_r3, igp_metric=2)
        sin_r3_syd_r3['sin_r3'].addParams(ip=('10.0.6.1/24', 'fc00:0:6::1/64'))
        sin_r3_syd_r3['syd_r3'].addParams(ip=('10.0.6.2/24', 'fc00:0:6::2/64'))

        sin_r1_syd_bb1 = self.addLink(sin_r1, syd_bb1, igp_metric=2)
        sin_r1_syd_bb1['sin_r1'].addParams(ip=('10.2.8.1/24', 'fc00:2:8::1/64'))
        sin_r1_syd_bb1['syd_bb1'].addParams(ip=('10.2.8.2/24', 'fc00:2:8::2/64'))

        sin_r1_mrs = self.addLink(sin_r1, mrs, igp_metric=2)
        sin_r1_mrs['sin_r1'].addParams(ip=('10.2.12.1/24', 'fc00:2:12::1/64'))
        sin_r1_mrs['mrs'].addParams(ip=('10.2.12.2/24', 'fc00:2:12::2/64'))

        sin_r2_syd_bb2 = self.addLink(sin_r2, syd_bb2, igp_metric=2)
        sin_r2_syd_bb2['sin_r2'].addParams(ip=('10.3.9.1/24', 'fc00:3:9::1/64'))
        sin_r2_syd_bb2['syd_bb2'].addParams(ip=('10.3.9.2/24', 'fc00:3:9::2/64'))

        sin_r2_sjo = self.addLink(sin_r2, sjo, igp_metric=2)
        sin_r2_sjo['sin_r2'].addParams(ip=('10.3.13.1/24', 'fc00:3:13::1/64'))
        sin_r2_sjo['sjo'].addParams(ip=('10.3.13.2/24', 'fc00:3:13::2/64'))

        sin_r2_mrs = self.addLink(sin_r2, mrs, igp_metric=2)
        sin_r2_mrs['sin_r2'].addParams(ip=('10.3.12.1/24', 'fc00:3:12::1/64'))
        sin_r2_mrs['mrs'].addParams(ip=('10.3.12.2/24', 'fc00:3:12::2/64'))

        # mrs_sjo = self.addLink(mrs, sjo, igp_metric=2)
        # mrs_sjo['mrs'].addParams(ip=('10.12.13.1/24', 'fc00:12:13::1/64'))
        # mrs_sjo['sjo'].addParams(ip=('10.12.13.2/24', 'fc00:12:13::2/64'))

        # mrs_lax = self.addLink(mrs, lax, igp_metric=2)
        # mrs_lax['mrs'].addParams(ip=('10.12.14.1/24', 'fc00:12:14::1/64'))
        # mrs_lax['lax'].addParams(ip=('10.12.14.2/24', 'fc00:12:14::2/64'))

        syd_bb2_lax = self.addLink(syd_bb2, lax, igp_metric=2)
        syd_bb2_lax['syd_bb2'].addParams(ip=('10.9.14.1/24', 'fc00:9:14::1/64'))
        syd_bb2_lax['lax'].addParams(ip=('10.9.14.2/24', 'fc00:9:14::2/64'))

        sin_r3_sin_r1 = self.addLink(sin_r3, sin_r1)
        sin_r3_sin_r1['sin_r3'].addParams(ip=('10.0.2.1/24', 'fc00:0:2::1/64'))
        sin_r3_sin_r1['sin_r1'].addParams(ip=('10.0.2.2/24', 'fc00:0:2::2/64'))

        sin_r3_sin_r4 = self.addLink(sin_r3, sin_r4)
        sin_r3_sin_r4['sin_r3'].addParams(ip=('10.0.1.1/24', 'fc00:0:1::1/64'))
        sin_r3_sin_r4['sin_r4'].addParams(ip=('10.0.1.2/24', 'fc00:0:1::2/64'))

        sin_r1_sin_r5 = self.addLink(sin_r1, sin_r5)
        sin_r1_sin_r5['sin_r1'].addParams(ip=('10.2.4.1/24', 'fc00:2:4::1/64'))
        sin_r1_sin_r5['sin_r5'].addParams(ip=('10.2.4.2/24', 'fc00:2:4::2/64'))

        sin_r1_sin_r2 = self.addLink(sin_r1, sin_r2)
        sin_r1_sin_r2['sin_r1'].addParams(ip=('10.2.3.1/24', 'fc00:2:3::1/64'))
        sin_r1_sin_r2['sin_r2'].addParams(ip=('10.2.3.2/24', 'fc00:2:3::2/64'))

        sin_r2_sin_r6 = self.addLink(sin_r2, sin_r6)
        sin_r2_sin_r6['sin_r2'].addParams(ip=('10.3.5.1/24', 'fc00:3:5::1/64'))
        sin_r2_sin_r6['sin_r6'].addParams(ip=('10.3.5.2/24', 'fc00:3:5::2/64'))

        sin_r4_sin_r2 = self.addLink(sin_r4, sin_r2)
        sin_r4_sin_r2['sin_r4'].addParams(ip=('10.1.3.1/24', 'fc00:1:3::1/64'))
        sin_r4_sin_r2['sin_r2'].addParams(ip=('10.1.3.2/24', 'fc00:1:3::2/64'))
        #
        syd_r3_syd_bb1 = self.addLink(syd_r3, syd_bb1)
        syd_r3_syd_bb1['syd_r3'].addParams(ip=('10.6.8.1/24', 'fc00:6:8::1/64'))
        syd_r3_syd_bb1['syd_bb1'].addParams(ip=('10.6.8.2/24', 'fc00:6:8::2/64'))
        #
        syd_r3_syd_r4 = self.addLink(syd_r3, syd_r4)
        syd_r3_syd_r4['syd_r3'].addParams(ip=('10.6.7.1/24', 'fc00:6:7::1/64'))
        syd_r3_syd_r4['syd_r4'].addParams(ip=('10.6.7.2/24', 'fc00:6:7::2/64'))
        #
        syd_r4_syd_bb2 = self.addLink(syd_r4, syd_bb2)
        syd_r4_syd_bb2['syd_r4'].addParams(ip=('10.7.9.1/24', 'fc00:7:9::1/64'))
        syd_r4_syd_bb2['syd_bb2'].addParams(ip=('10.7.9.2/24', 'fc00:7:9::2/64'))
        #
        syd_bb1_syd_bb2 = self.addLink(syd_bb1, syd_bb2)
        syd_bb1_syd_bb2['syd_bb1'].addParams(ip=('10.8.9.1/24', 'fc00:8:9::1/64'))
        syd_bb1_syd_bb2['syd_bb2'].addParams(ip=('10.8.9.2/24', 'fc00:8:9::2/64'))
        #
        syd_bb1_syd_r5 = self.addLink(syd_bb1, syd_r5)
        syd_bb1_syd_r5['syd_bb1'].addParams(ip=('10.8.10.1/24', 'fc00:8:10::1/64'))
        syd_bb1_syd_r5['syd_r5'].addParams(ip=('10.8.10.2/24', 'fc00:8:10::2/64'))
        #
        syd_bb2_syd_r6 = self.addLink(syd_bb2, syd_r6)
        syd_bb2_syd_r6['syd_bb2'].addParams(ip=('10.9.11.1/24', 'fc00:9:11::1/64'))
        syd_bb2_syd_r6['syd_r6'].addParams(ip=('10.9.11.2/24', 'fc00:9:11::2/64'))
        #
        sjo_lax = self.addLink(sjo, lax)
        sjo_lax['sjo'].addParams(ip=('10.13.14.1/24', 'fc00:13:14::1/64'))
        sjo_lax['lax'].addParams(ip=('10.13.14.2/24', 'fc00:13:14::2/64'))

        # eq links

        sin_eq_syd_eq = self.addLink(sin_eq, syd_eq)
        sin_eq_syd_eq['sin_eq'].addParams(ip=('10.16.17.1/24', 'fc00:16:17::1/64'))
        sin_eq_syd_eq['syd_eq'].addParams(ip=('10.16.17.2/24', 'fc00:16:17::2/64'))

        sin_r5_sin_eq = self.addLink(sin_r5, sin_eq)
        sin_r5_sin_eq['sin_r5'].addParams(ip=('10.4.16.1/24', 'fc00:4:16::1/64'))
        sin_r5_sin_eq['sin_eq'].addParams(ip=('10.4.16.2/24', 'fc00:4:16::2/64'))

        # sin6_amazon1 = self.addLink(sin6, amazon1)
        # sin6_amazon1['sin6'].addParams(ip=('10.5.16.1/24', 'fc00:5:16::1/64'))
        # sin6_amazon1['amazon1'].addParams(ip=('10.5.16.2/24', 'fc00:5:16::2/64'))

        syd_bb2_syd_eq = self.addLink(syd_bb2, syd_eq)
        syd_bb2_syd_eq['syd_bb2'].addParams(ip=('10.9.17.1/24', 'fc00:9:17::1/64'))
        syd_bb2_syd_eq['syd_eq'].addParams(ip=('10.9.17.2/24', 'fc00:9:17::2/64'))

        # NTT links

        sin_ntt_syd_ntt1 = self.addLink(sin_ntt, syd_ntt1)
        sin_ntt_syd_ntt1['sin_ntt'].addParams(ip=('10.32.33.1/24', 'fc00:32:33::1/64'))
        sin_ntt_syd_ntt1['syd_ntt1'].addParams(ip=('10.32.33.2/24', 'fc00:32:33::2/64'))

        sin_ntt_syd_ntt2 = self.addLink(sin_ntt, syd_ntt2)
        sin_ntt_syd_ntt2['sin_ntt'].addParams(ip=('10.32.34.1/24', 'fc00:32:34::1/64'))
        sin_ntt_syd_ntt2['syd_ntt2'].addParams(ip=('10.32.34.2/24', 'fc00:32:34::2/64'))

        syd_ntt1_syd_ntt2 = self.addLink(syd_ntt1, syd_ntt2)
        syd_ntt1_syd_ntt2['syd_ntt1'].addParams(ip=('10.33.34.1/24', 'fc00:33:34::1/64'))
        syd_ntt1_syd_ntt2['syd_ntt2'].addParams(ip=('10.33.34.2/24', 'fc00:33:34::2/64'))

        sin_r5_sin_ntt = self.addLink(sin_r5, sin_ntt)
        sin_r5_sin_ntt['sin_r5'].addParams(ip=('10.4.32.1/24', 'fc00:4:32::1/64'))
        sin_r5_sin_ntt['sin_ntt'].addParams(ip=('10.4.32.2/24', 'fc00:4:32::2/64'))

        syd_bb1_syd_ntt1 = self.addLink(syd_bb1, syd_ntt1)
        syd_bb1_syd_ntt1['syd_bb1'].addParams(ip=('10.8.33.1/24', 'fc00:8:33::1/64'))
        syd_bb1_syd_ntt1['syd_ntt1'].addParams(ip=('10.8.33.2/24', 'fc00:8:33::2/64'))

        syd_bb2_syd_ntt2 = self.addLink(syd_bb2, syd_ntt2)
        syd_bb2_syd_ntt2['syd_bb2'].addParams(ip=('10.9.34.1/24', 'fc00:9:34::1/64'))
        syd_bb2_syd_ntt2['syd_ntt2'].addParams(ip=('10.9.34.2/24', 'fc00:9:34::2/64'))

        # Telstra links

        sin_tel_syd_tel1 = self.addLink(sin_tel, syd_tel1)
        sin_tel_syd_tel1['sin_tel'].addParams(ip=('10.48.49.1/24', 'fc00:48:49::1/64'))
        sin_tel_syd_tel1['syd_tel1'].addParams(ip=('10.48.49.2/24', 'fc00:48:49::2/64'))

        sin_tel_syd_tel2 = self.addLink(sin_tel, syd_tel2)
        sin_tel_syd_tel2['sin_tel'].addParams(ip=('10.48.50.1/24', 'fc00:48:50::1/64'))
        sin_tel_syd_tel2['syd_tel2'].addParams(ip=('10.48.50.2/24', 'fc00:48:50::2/64'))

        syd_tel1_syd_tel2 = self.addLink(syd_tel1, syd_tel2)
        syd_tel1_syd_tel2['syd_tel1'].addParams(ip=('10.49.50.1/24', 'fc00:49:50::1/64'))
        syd_tel1_syd_tel2['syd_tel2'].addParams(ip=('10.49.50.2/24', 'fc00:49:50::2/64'))

        sin_r6_sin_tel = self.addLink(sin_r6, sin_tel)
        sin_r6_sin_tel['sin_r6'].addParams(ip=('10.5.48.1/24', 'fc00:5:48::1/64'))
        sin_r6_sin_tel['sin_tel'].addParams(ip=('10.5.48.2/24', 'fc00:5:48::2/64'))

        syd_bb1_syd_tel1 = self.addLink(syd_bb1, syd_tel1)
        syd_bb1_syd_tel1['syd_bb1'].addParams(ip=('10.8.49.1/24', 'fc00:8:49::1/64'))
        syd_bb1_syd_tel1['syd_tel1'].addParams(ip=('10.8.49.2/24', 'fc00:8:49::2/64'))

        syd_bb2_syd_tel2 = self.addLink(syd_bb2, syd_tel2)
        syd_bb2_syd_tel2['syd_bb2'].addParams(ip=('10.9.50.1/24', 'fc00:9:50::1/64'))
        syd_bb2_syd_tel2['syd_tel2'].addParams(ip=('10.9.50.2/24', 'fc00:9:50::2/64'))

        # Clients links

        client1_client1b = self.addLink(client1, client1b)
        client1_client1b['client1'].addParams(ip=('10.96.96.1/24', 'fc00:96:96::1/64'))
        client1_client1b['client1b'].addParams(ip=('10.96.96.2/24', 'fc00:96:96::2/64'))

        sin_r5_client1 = self.addLink(sin_r5, client1)
        sin_r5_client1['sin_r5'].addParams(ip=('10.4.96.1/24', 'fc00:4:96:1::1/64'))
        sin_r5_client1['client1'].addParams(ip=('10.4.96.2/24', 'fc00:4:96:1::2/64'))

        sin_r5_client1_backup = self.addLink(sin_r5, client1b)
        sin_r5_client1_backup['sin_r5'].addParams(ip=('10.4.96.3/24', 'fc00:4:96:2::1/64'))
        sin_r5_client1_backup['client1b'].addParams(ip=('10.4.96.4/24', 'fc00:4:96:2::2/64'))

        client2_client2b = self.addLink(client2, client2b)
        client2_client2b['client2'].addParams(ip=('10.97.97.1/24', 'fc00:97:97::1/64'))
        client2_client2b['client2b'].addParams(ip=('10.97.97.2/24', 'fc00:97:97::2/64'))

        syd_bb1_client2 = self.addLink(syd_bb1, client2)
        syd_bb1_client2['syd_bb1'].addParams(ip=('10.8.97.1/24', 'fc00:8:97:1::1/64'))
        syd_bb1_client2['client2'].addParams(ip=('10.8.97.2/24', 'fc00:8:97:1::2/64'))

        syd_bb1_client2_backup = self.addLink(syd_bb1, client2b)
        syd_bb1_client2_backup['syd_bb1'].addParams(ip=('10.8.97.3/24', 'fc00:8:97:2::1/64'))
        syd_bb1_client2_backup['client2b'].addParams(ip=('10.8.97.4/24', 'fc00:8:97:2::2/64'))

        client3_client3b = self.addLink(client3, client3b)
        client3_client3b['client3'].addParams(ip=('10.98.98.1/24', 'fc00:98:98::1/64'))
        client3_client3b['client3b'].addParams(ip=('10.98.98.2/24', 'fc00:98:98::2/64'))

        syd_bb2_client3 = self.addLink(syd_bb2, client3)
        syd_bb2_client3['syd_bb2'].addParams(ip=('10.9.98.1/24', 'fc00:9:98:1::1/64'))
        syd_bb2_client3['client3'].addParams(ip=('10.9.98.2/24', 'fc00:9:98:1::2/64'))

        syd_bb2_client3_backup = self.addLink(syd_bb2, client3b)
        syd_bb2_client3_backup['syd_bb2'].addParams(ip=('10.9.98.3/24', 'fc00:9:98:2::1/64'))
        syd_bb2_client3_backup['client3b'].addParams(ip=('10.9.98.4/24', 'fc00:9:98:2::2/64'))

        # Hosts

        sin_h1 = self.addHost("sin_h1")
        sin_h2 = self.addHost("sin_h2")
        sin_h3 = self.addHost("sin_h3")
        sin_h4 = self.addHost("sin_h4")
        sin_h5 = self.addHost("sin_h5")
        sin_h6 = self.addHost("sin_h6")

        syd_h1 = self.addHost("syd_h1")
        syd_h2 = self.addHost("syd_h2")
        syd_h3 = self.addHost("syd_h3")
        syd_h4 = self.addHost("syd_h4")
        syd_h5 = self.addHost("syd_h5")
        syd_h6 = self.addHost("syd_h6")

        mrs_h = self.addHost("mrs_h")
        sjo_h = self.addHost("sjo_h")
        lax_h = self.addHost("lax_h")

        syd_eq_h = self.addHost("syd_eq_h")
        sin_eq_h = self.addHost("sin_eq_h")

        syd_ntt1_h = self.addHost("syd_ntt1_h")
        syd_ntt2_h = self.addHost("syd_ntt2_h")
        sin_ntt_h = self.addHost("sin_ntt_h")

        syd_tel1_h = self.addHost("syd_tel1_h")
        syd_tel2_h = self.addHost("syd_tel2_h")
        sin_tel_h = self.addHost("sin_tel_h")

        client_h1 = self.addHost("client_h1")
        client_h2 = self.addHost("client_h2")
        client_h3 = self.addHost("client_h3")

        # Host links

        self.addLinks((sin_r3, sin_h1), (sin_r4, sin_h2), (sin_r1, sin_h3), (sin_r2, sin_h4), (sin_r5, sin_h5),
                      (sin_r6, sin_h6),
                      (syd_r3, syd_h1), (syd_r4, syd_h2), (syd_bb1, syd_h3), (syd_bb2, syd_h4), (syd_r5, syd_h5),
                      (syd_r6, syd_h6),
                      (mrs, mrs_h), (lax, lax_h), (sjo, sjo_h),
                      (sin_eq, sin_eq_h), (syd_eq, syd_eq_h),
                      (sin_ntt, sin_ntt_h), (syd_ntt2, syd_ntt2_h), (syd_ntt1, syd_ntt1_h),
                      (syd_tel1, syd_tel1_h), (syd_tel2, syd_tel2_h), (sin_tel, sin_tel_h),
                      (client1, client_h1), (client2, client_h2), (client3, client_h3))

        self.addSubnet((sin_r3, sin_h1), subnets=('103.5.15.8/30', '2402:1f00::14/126'))
        self.addSubnet((sin_r4, sin_h2), subnets=('103.5.15.12/30', '2402:1f00::18/126'))
        self.addSubnet((sin_r1, sin_h3), subnets=('103.5.15.16/30', '2402:1f00::1C/126'))
        self.addSubnet((sin_r2, sin_h4), subnets=('103.5.15.20/30', '2402:1f00::20/126'))
        self.addSubnet((sin_r5, sin_h5), subnets=('103.5.15.24/30', '2402:1f00::24/126'))
        self.addSubnet((sin_r6, sin_h6), subnets=('103.5.15.28/30', '2402:1f00::28/126'))

        self.addSubnet((syd_r3, syd_h1), subnets=('103.5.14.8/30', '2402:1f00::2C/126'))
        self.addSubnet((syd_r4, syd_h2), subnets=('103.5.14.12/30', '2402:1f00::30/126'))
        self.addSubnet((syd_bb1, syd_h3), subnets=('103.5.14.16/30', '2402:1f00::34/126'))
        self.addSubnet((syd_bb2, syd_h4), subnets=('103.5.14.20/30', '2402:1f00::38/126'))
        self.addSubnet((syd_r5, syd_h5), subnets=('103.5.14.24/30', '2402:1f00::3C/126'))
        self.addSubnet((syd_r6, syd_h6), subnets=('103.5.14.28/30', '2402:1f00::40/126'))

        self.addSubnet((mrs, mrs_h), subnets=('94.23.122.4/30', '2001:41d0::4/126'))
        self.addSubnet((sjo, sjo_h), subnets=('78.32.132.8/30', '2604:2DC0::8/126'))
        self.addSubnet((lax, lax_h), subnets=('78.32.132.12/30', '2604:2DC0::C/126'))

        self.addSubnet((sin_eq, sin_eq_h), subnets=('143.5.15.4/30', '2500:1f00::4/126'))
        self.addSubnet((syd_eq, syd_eq_h), subnets=('143.5.15.8/30', '2500:1f00::8/126'))

        self.addSubnet((sin_ntt, sin_ntt_h), subnets=('143.7.15.4/30', '2500:3f00::4/126'))
        self.addSubnet((syd_ntt2, syd_ntt2_h), subnets=('143.7.15.8/30', '2500:3f00::8/126'))
        self.addSubnet((syd_ntt1, syd_ntt1_h), subnets=('143.7.15.12/30', '2500:3f00::C/126'))

        self.addSubnet((syd_tel1, syd_tel1_h), subnets=('143.9.15.4/30', '2500:5f00::4/126'))
        self.addSubnet((syd_tel2, syd_tel2_h), subnets=('143.9.15.8/30', '2500:5f00::8/126'))
        self.addSubnet((sin_tel, sin_tel_h), subnets=('143.9.15.12/30', '2500:5f00::C/126'))

        self.addSubnet((client1, client_h1), subnets=('153.1.15.4/30', '2600:1f00::4/126'))
        self.addSubnet((client2, client_h2), subnets=('153.2.15.4/30', '2600:2f00::4/126'))
        self.addSubnet((client3, client_h3), subnets=('153.3.15.4/30', '2600:3f00::4/126'))

        # BGP configuration

        # iBGP sessions

        self.addAS(16276,
                   routers=(
                       sin_r3, sin_r4, sin_r1, sin_r2, sin_r5, sin_r6, syd_r3, syd_r4, syd_bb1, syd_bb2, syd_r5, syd_r6,
                       mrs, sjo, lax))

        set_rr(self, rr=sin_r3, peers=[syd_r3, syd_r4, sin_r4, sin_r1, sin_r2, sin_r5, sin_r6, mrs, sjo])
        set_rr(self, rr=sin_r4, peers=[syd_r3, syd_r4, sin_r3, sin_r1, sin_r2, sin_r5, sin_r6, mrs, sjo])
        set_rr(self, rr=syd_r3, peers=[sin_r3, sin_r4, syd_r4, syd_bb1, syd_bb2, syd_r5, syd_r6, lax])
        set_rr(self, rr=syd_r4, peers=[sin_r3, sin_r4, syd_r3, syd_bb1, syd_bb2, syd_r5, syd_r6, lax])

        self.addiBGPFullMesh(16509, (syd_eq, sin_eq))

        self.addiBGPFullMesh(2914, (syd_ntt1, syd_ntt2, sin_ntt))

        self.addiBGPFullMesh(4637, (syd_tel1, syd_tel2, sin_tel))
        self.addiBGPFullMesh(1, (client1, client1b))
        self.addiBGPFullMesh(2, (client2, client2b))
        self.addiBGPFullMesh(3, (client3, client3b))

        # eBGP sessions

        # Share cost sessions
        ebgp_session(self, sin_r5, sin_eq)

        ebgp_session(self, syd_bb2, syd_eq)

        # Provider sessions
        ebgp_session(self, syd_bb1, syd_ntt1)
        ebgp_session(self, syd_bb2, syd_ntt2)
        ebgp_session(self, sin_r5, sin_ntt)

        ebgp_session(self, sin_r6, sin_tel)
        ebgp_session(self, syd_bb1, syd_tel1)
        ebgp_session(self, syd_bb2, syd_tel2)

        # Clients sessions
        ebgp_session(self, client1, sin_r5)
        ebgp_session(self, client2, syd_bb1)
        ebgp_session(self, client3, syd_bb2)

        ebgp_session(self, client1b, sin_r5)
        ebgp_session(self, client2b, syd_bb1)
        ebgp_session(self, client3b, syd_bb2)

        # Send communities from neighbors

        all_al = AccessList('all', ('any',))

        blackhole = AccessList('blackhole', ('2600:1f01::0/32',))

        # Client1 customer link
        client1.get_config(BGP).set_community('16276:120', to_peer=sin_r5, matching=(all_al,))
        # Client1 customer backup link
        client1b.get_config(BGP).set_community('16276:115', to_peer=sin_r5, matching=(all_al,))

        # Client1 blackholed prefix
        client1.get_config(BGP).set_community('16276:666', to_peer=sin_r5, matching=(blackhole,))
        client1b.get_config(BGP).set_community('16276:666', to_peer=sin_r5, matching=(blackhole,))

        # Client2 customer link
        client2.get_config(BGP).set_community('16276:120', to_peer=syd_bb1, matching=(all_al,))
        # Client2 customer backup link
        client2b.get_config(BGP).set_community('16276:115', to_peer=syd_bb1, matching=(all_al,))

        # Client3 customer link
        client3.get_config(BGP).set_community('16276:120', to_peer=syd_bb2, matching=(all_al,))
        # Client3 customer backup link
        client3b.get_config(BGP).set_community('16276:115', to_peer=syd_bb2, matching=(all_al,))

        super().build(*args, **kwargs)

    # Returns a router with ospf, ospf6 and bgp configuration
    def add_config_router(self, name, loopbacks, family4=AF_INET(), family6=AF_INET6()):
        r = self.addRouter(name, lo_addresses=loopbacks, config=RouterConfig)

        # OSPF
        r.addDaemon(OSPF)
        r.addDaemon(OSPF6)

        # BGP
        r.addDaemon(BGP, address_families=(family4, family6))

        return r

    def post_build(self, *args, **kwargs):
        # Executed after build

        super().post_build(*args, **kwargs)


if __name__ == '__main__':
    net = IPNet(topo=Net(), allocate_IPs=False)
    try:
        net.start()

        IPCLI(net)
    finally:
        net.stop()
