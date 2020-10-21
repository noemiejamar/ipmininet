#!/usr/bin/env python3

from ipmininet.ipnet import IPNet
from ipmininet.cli import IPCLI
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import BGP, OSPF6, OSPF, RouterConfig, AF_INET6, set_rr, ebgp_session, SHARE,iBGPFullMesh, AS, bgp_peering
import ipmininet


class SimpleBGPTopo(IPTopo):

    def build(self, *args, **kwargs):
        family = AF_INET6()
       # lan_as1_h1 = 'cafe:babe:dead:beaf::/64'
       # lan_as2_h2 = 'c1a4:4ad:c0ff:ee::/64'

        # first step, adding routers
        # routers of as1




        # Add all routers
        as1_bb1= self.addRouter("as1_bb1", config=RouterConfig) #sydsy2bb1a72
        as1_bb2= self.addRouter("as1_bb2", config=RouterConfig) #sydsy2bb2a72
        as1_r3= self.addRouter("as1_r3", config=RouterConfig)#syd1sy2g1nc5
        as1_r4= self.addRouter("as1_r4", config=RouterConfig)#syd1sy2g2nc5
        as1_r5= self.addRouter("as1_r5", config=RouterConfig)#sydsy2rr1ucs
        as1_r6= self.addRouter("as1_r6", config=RouterConfig)#sydsy2rr2ucs

        as1_r7= self.addRouter("as1_r7", config=RouterConfig)#laxla1bb1n7
        as1_r8= self.addRouter("as1_r8", config=RouterConfig)#sjosv5bb1n7
        as1_r9= self.addRouter("as1_r9", config=RouterConfig)#mrsmrsbb1a72

        as1_r10= self.addRouter("as1_r10", config=RouterConfig)#sinsg1sbb1nc5
        as1_r11= self.addRouter("as1_r11", config=RouterConfig)#singss1sbb1nc5
        as1_r12= self.addRouter("as1_r12", config=RouterConfig)#sinsgcs2g1nc5
        as1_r13= self.addRouter("as1_r13", config=RouterConfig)#sin1sgcs2g2nc5
        as1_r14= self.addRouter("as1_r14", config=RouterConfig)#sinsg1pb1nc5
        as1_r15= self.addRouter("as1_r15", config=RouterConfig)#singss1pb1nc5
        
        vodafone=self.addRouter("vodafone", config=RouterConfig)
        ntt=self.addRouter("ntt", config=RouterConfig)
        equinix=self.addRouter("equinix", config=RouterConfig)
        telstra=self.addRouter("telstra", config=RouterConfig)
        

        
        
        
        as1_bb1.addDaemon(OSPF6)
        as1_bb2.addDaemon(OSPF6)
        as1_r3.addDaemon(OSPF6)
        as1_r4.addDaemon(OSPF6)
        as1_r5.addDaemon(OSPF6)
        as1_r6.addDaemon(OSPF6)
        as1_r7.addDaemon(OSPF6)
        as1_r8.addDaemon(OSPF6)
        as1_r9.addDaemon(OSPF6)
        as1_r10.addDaemon(OSPF6)
        as1_r11.addDaemon(OSPF6)
        as1_r12.addDaemon(OSPF6)
        as1_r13.addDaemon(OSPF6)
        as1_r14.addDaemon(OSPF6)
        as1_r15.addDaemon(OSPF6)
        vodafone.addDaemon(OSPF6)
        ntt.addDaemon(OSPF6)
        equinix.addDaemon(OSPF6)
        telstra.addDaemon(OSPF6)
        
        as1_bb1.addDaemon(OSPF)
        as1_bb2.addDaemon(OSPF)
        as1_r3.addDaemon(OSPF)
        as1_r4.addDaemon(OSPF)
        as1_r5.addDaemon(OSPF)
        as1_r6.addDaemon(OSPF)
        as1_r7.addDaemon(OSPF)
        as1_r8.addDaemon(OSPF)
        as1_r9.addDaemon(OSPF)
        as1_r10.addDaemon(OSPF)
        as1_r11.addDaemon(OSPF)
        as1_r12.addDaemon(OSPF)
        as1_r13.addDaemon(OSPF)
        as1_r14.addDaemon(OSPF)
        as1_r15.addDaemon(OSPF)
        vodafone.addDaemon(OSPF)
        ntt.addDaemon(OSPF)
        equinix.addDaemon(OSPF)
        telstra.addDaemon(OSPF)

        
        #adding BGP to establish iBGP sessions
        as1_bb1.addDaemon(BGP)
        as1_bb2.addDaemon(BGP)
        as1_r3.addDaemon(BGP)
        as1_r4.addDaemon(BGP)
        as1_r5.addDaemon(BGP)
        as1_r6.addDaemon(BGP)
        as1_r7.addDaemon(BGP)
        as1_r8.addDaemon(BGP)
        as1_r9.addDaemon(BGP)
        as1_r10.addDaemon(BGP)
        as1_r11.addDaemon(BGP)
        as1_r12.addDaemon(BGP)
        as1_r13.addDaemon(BGP)
        as1_r14.addDaemon(BGP)
        as1_r15.addDaemon(BGP)
        vodafone.addDaemon(BGP)
        ntt.addDaemon(BGP)
        equinix.addDaemon(BGP)
        telstra.addDaemon(BGP)
        




        
        # set up the AS
        self.addAS(1, (as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5,as1_r6, as1_r7,
         as1_r8, as1_r9,  as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15))
        self.addAS(2, routers=[vodafone])
        self.addAS(3, routers=[ntt])
        self.addAS(4, routers=[equinix])
        self.addAS(5, routers=[telstra])
        
        #set up the route reflectors
        set_rr(self, rr=as1_r5, peers=[as1_bb1, as1_r3,as1_r4])
        set_rr(self, rr=as1_r6, peers=[as1_bb2, as1_r3, as1_r4])

        set_rr(self, rr=as1_r7, peers=[as1_bb2])
        set_rr(self, rr=as1_r8, peers=[as1_r11])
        set_rr(self, rr=as1_r9, peers=[as1_r10, as1_r11, as1_r12, as1_r13, as1_r14,as1_r15])
        #route reflectors in full mesh
        self.addiBGPFullMesh(1, routers=[as1_r5, as1_r6, as1_r7, as1_r8, as1_r9])
        
        

        # Add Links
        self.addLink (as1_bb1, as1_bb2, igp_metric=1, params1={"ip": "BABE:1:10:0304::/64"},
                     params2={"ip": "BABE:1:10:0402::/64"})
        self.addLink (as1_bb1, as1_r5, igp_metric=1, params1={"ip": "BABE:1:10:0301::/64"},
                     params2={"ip": "BABE:1:10:0600::/64"})
        self.addLink  (as1_bb1, as1_r3, igp_metric=1, params1={"ip": "BABE:1:10:0300::/64"},
                     params2={"ip": "BABE:1:10:0101::/64"})
        self.addLink  (as1_bb1,  as1_r10, igp_metric=1, params1={"ip": "BABE:1:10:0305::/64"},
                     params2={"ip": "BABE:1:11:0F00::/64"})
                    
        self.addLink    (as1_bb2, as1_r6, igp_metric=1, params1={"ip": "BABE:1:10:0401::/64"},
                     params2={"ip": "BABE:1:10:0500::/64"})
        self.addLink   (as1_bb2, as1_r4, igp_metric=1, params1={"ip": "BABE:1:10:0400::/64"},
                     params2={"ip": "BABE:1:10:0201::/64"})
        self.addLink   (as1_bb2, as1_r7, igp_metric=1, params1={"ip": "BABE:1:10:0407::/64"},
                     params2={"ip": "BABE:1:10:0701::/64"})
        self.addLink    (as1_bb2, as1_r11, igp_metric=1, params1={"ip": "BABE:1:10:0403::/64"},
                     params2={"ip": "BABE:1:11:1000::/64"})

        self.addLink   (as1_r3, as1_r4, igp_metric=1, params1={"ip": "BABE:1:10:0100::/64"},
                     params2={"ip": "BABE:1:10:0200::/64"})
        self.addLink   (as1_r3, as1_r12, igp_metric=1, params1={"ip": "BABE:1:10:0102::/64"},
                     params2={"ip": "BABE:1:11:0D00::/64"})

        self.addLink    (as1_r7, as1_r8, igp_metric=1, params1={"ip": "BABE:1:10:0700::/64"},
                     params2={"ip": "BABE:1:11:1100::/64"})

        self.addLink   (as1_r8, as1_r11, igp_metric=1, params1={"ip": "BABE:1:11:1101::/64"},
                     params2={"ip": "BABE:1:11:1005::/64"})

        self.addLink   ( as1_r10, as1_r11, igp_metric=1, params1={"ip": "BABE:1:11:0F02::/64"},
                     params2={"ip": "BABE:1:11:1002::/64"})
        self.addLink   ( as1_r10,  as1_r14, igp_metric=1, params1={"ip": "BABE:1:11:0F04::/64"},
                     params2={"ip": "BABE:1:11:1300::/64"})
        self.addLink   ( as1_r10,  as1_r9, igp_metric=1, params1={"ip": "BABE:1:11:0F03::/64"},
                     params2={"ip": "BABE:1:11:1201::/64"})
        self.addLink    ( as1_r10,  as1_r12, igp_metric=1, params1={"ip": "BABE:1:11:0F01::/64"},
                     params2={"ip": "BABE:1:11:0D02::/64"})

        self.addLink    (as1_r11, as1_r13, igp_metric=1, params1={"ip": "BABE:1:11:1001::/64"},
                     params2={"ip": "BABE:1:11:0E00::/64"})
        self.addLink   (as1_r11, as1_r15, igp_metric=1, params1={"ip": "BABE:1:11:1004::/64"},
                     params2={"ip": "BABE:1:11:1402::/64"})
        self.addLink    (as1_r11, as1_r9, igp_metric=1, params1={"ip": "BABE:1:11:1003::/64"},
                     params2={"ip": "BABE:1:11:1200::/64"})
        self.addLink    (as1_r12, as1_r13, igp_metric=1, params1={"ip": "BABE:1:11:0D01::/64"},
                     params2={"ip": "BABE:1:11:0E01::/64"})
        

        
        self.addLink    (as1_bb1, telstra)
        self.addLink    (as1_bb1, ntt)
        self.addLink    (as1_bb2, telstra)
        self.addLink    (as1_bb2, ntt)
        self.addLink    (as1_bb2, equinix)
        self.addLink    (as1_r14, vodafone)
        self.addLink    (as1_r14, ntt)
        self.addLink    (as1_r14, equinix)
        self.addLink    (as1_r11, vodafone)
        self.addLink    (as1_r11, telstra)
        
        #add eBGP session between AS
        ebgp_session(self, as1_bb1, telstra, link_type=SHARE)
        ebgp_session(self, as1_bb1, ntt, link_type=SHARE)
        ebgp_session(self, as1_bb2, telstra, link_type=SHARE)
        ebgp_session(self, as1_bb2, ntt, link_type=SHARE)
        ebgp_session(self, as1_bb2, equinix, link_type=SHARE)
        ebgp_session(self, as1_r14, vodafone, link_type=SHARE)
        ebgp_session(self, as1_r14, ntt, link_type=SHARE)
        ebgp_session(self, as1_r14, equinix, link_type=SHARE)
        ebgp_session(self, as1_r11, vodafone, link_type=SHARE)
        ebgp_session(self, as1_r11, telstra, link_type=SHARE)
        
        # --- Hosts ---
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")

        self.addLink(h1,as1_bb1,igp_metric=1)
        self.addLink(h2,as1_bb2,igp_metric=1)


        super().build(*args, **kwargs)


# Press the green button to run the script.
if __name__ == '__main__':
    net = IPNet(topo=SimpleBGPTopo())
    try:
        net.start()
        IPCLI(net)
    finally:
        net.stop()
