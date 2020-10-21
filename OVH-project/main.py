#!/usr/bin/env python3
from ipmininet.ipnet import IPNet
from ipmininet.cli import IPCLI
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import BGP, OSPF6, OSPF, RouterConfig, AF_INET6, set_rr, ebgp_session, SHARE
import ipmininet


class SimpleBGPTopo(IPTopo):

    def build(self, *args, **kwargs):
        # family = AF_INET6()
        # lan_as1_h1 = 'cafe:babe:dead:beaf::/64'
        # lan_as2_h2 = 'c1a4:4ad:c0ff:ee::/64'


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


         as16276_routers=[as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5,as1_r6, as1_r7,
         as1_r8, as1_r9,  as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15]
        
         self.addAS(16276, (as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5,as1_r6, as1_r7,
         as1_r8, as1_r9,  as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15))
         self.addAS(2, routers=[vodafone])
         self.addAS(3, routers=[ntt])
         self.addAS(4, routers=[equinix])
         self.addAS(5, routers=[telstra])
        
         for r in as16276_routers:
             r.addDaemon(OSPF)
             r.addDaemon(OSPF6)
             r.addDaemon(BGP)
        
        
         # Add Links
         self.addLink (as1_bb1, as1_bb2, igp_metric=1)
         self.addLink (as1_bb1, as1_r5, igp_metric=1)
         self.addLink  (as1_bb1, as1_r3, igp_metric=1)
         self.addLink  (as1_bb1,  as1_r10, igp_metric=1)

         self.addLink    (as1_bb2, as1_r6, igp_metric=1)
         self.addLink   (as1_bb2, as1_r4, igp_metric=1)
         self.addLink   (as1_bb2, as1_r7, igp_metric=1)
         self.addLink    (as1_bb2, as1_r11, igp_metric=1)

         self.addLink   (as1_r3, as1_r4, igp_metric=1)
         self.addLink   (as1_r3, as1_r12, igp_metric=1)

         self.addLink    (as1_r7, as1_r8, igp_metric=1)

         self.addLink   (as1_r8, as1_r11, igp_metric=1)

         self.addLink   ( as1_r10, as1_r11, igp_metric=1)
         self.addLink   ( as1_r10,  as1_r14, igp_metric=1)
         self.addLink   ( as1_r10,  as1_r9, igp_metric=1)
         self.addLink    ( as1_r10,  as1_r12, igp_metric=1)

         self.addLink    (as1_r11, as1_r13, igp_metric=1)
         self.addLink   (as1_r11, as1_r15, igp_metric=1)
         self.addLink    (as1_r11, as1_r9, igp_metric=1)

         
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

         set_rr(self, rr=as1_r5, peers=[as1_bb1, as1_r3,as1_r4])
         set_rr(self, rr=as1_r6, peers=[as1_bb2, as1_r3, as1_r4])

         set_rr(self, rr=as1_r7, peers=[as1_bb2])
         set_rr(self, rr=as1_r8, peers=[as1_r11])
         set_rr(self, rr=as1_r9, peers=[as1_r10, as1_r11, as1_r12, as1_r13, as1_r14,as1_r15])

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