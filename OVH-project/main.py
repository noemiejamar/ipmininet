#!/usr/bin/env python3
from ipmininet.ipnet import IPNet
from ipmininet.cli import IPCLI
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import BGP, OSPF6, OSPF, RouterConfig, AF_INET6, set_rr
from ipmininet.router.config import ebgp_session, SHARE , CLIENT_PROVIDER, AccessList, CommunityList
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

        ntt1=self.addRouter("ntt", config=RouterConfig)
        ntt2=self.addRouter("ntt2", config=RouterConfig)
        ntt3=self.addRouter("ntt3", config=RouterConfig)
        equinix1=self.addRouter("equinix1", config=RouterConfig)
        equinix2=self.addRouter("equinix2", config=RouterConfig)
        telstra1=self.addRouter("telstra1", config=RouterConfig)
        telstra2=self.addRouter("telstra2", config=RouterConfig)
        telstra3=self.addRouter("telstra3", config=RouterConfig)


        as16276_routers=[as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5,as1_r6, as1_r7,
        as1_r8, as1_r9,  as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15]
        
        self.addAS(16276, (as1_bb1, as1_bb2, as1_r3, as1_r4, as1_r5,as1_r6, as1_r7,
        as1_r8, as1_r9,  as1_r10, as1_r11, as1_r12, as1_r13, as1_r14, as1_r15))
        self.addAS(3, (ntt1, ntt2,ntt3))
        self.addAS(4, (equinix1,equinix2))
        self.addAS(5, (telstra1,telstra2,telstra3))
        
        for r in as16276_routers:
            r.addDaemon(OSPF)
            r.addDaemon(OSPF6)
            r.addDaemon(BGP, family=AF_INET6(redistribute=('connected')))


        telstra1.addDaemon(OSPF)
        telstra1.addDaemon(OSPF6)
        telstra1.addDaemon(BGP, family=AF_INET6(redistribute=('connected')))
        telstra2.addDaemon(OSPF)
        telstra2.addDaemon(OSPF6)
        telstra2.addDaemon(BGP, family=AF_INET6(redistribute=('connected')))
        telstra3.addDaemon(OSPF)
        telstra3.addDaemon(OSPF6)
        telstra3.addDaemon(BGP, family=AF_INET6(redistribute=('connected')))
        
        ntt1.addDaemon(OSPF)
        ntt1.addDaemon(OSPF6)
        ntt1.addDaemon(BGP, family=AF_INET6(redistribute=('connected')))
        ntt2.addDaemon(OSPF)
        ntt2.addDaemon(OSPF6)
        ntt2.addDaemon(BGP, family=AF_INET6(redistribute=( 'connected')))
        ntt3.addDaemon(OSPF)
        ntt3.addDaemon(OSPF6)
        ntt3.addDaemon(BGP, family=AF_INET6(redistribute=( 'connected')))

        equinix1.addDaemon(OSPF)
        equinix1.addDaemon(OSPF6)
        equinix1.addDaemon(BGP, family=AF_INET6(redistribute=( 'connected')))
        equinix2.addDaemon(OSPF)
        equinix2.addDaemon(OSPF6)
        equinix2.addDaemon(BGP, family=AF_INET6(redistribute=('connected')))

         # Add Links

        
        self.addLink (as1_bb1, as1_bb2, igp_metric=1, params1={"ip": "BABE:1:10:0304::/64"},
                     params2={"ip": "BABE:1:10:0402::/64"})
        self.addLink (as1_bb1, as1_r5, igp_metric=1, params1={"ip": "BABE:1:10:0301::/64"},
                     params2={"ip": "BABE:1:10:0600::/64"})
        self.addLink  (as1_bb1, as1_r3, igp_metric=1, params1={"ip": "BABE:1:10:0300::/64"},
                     params2={"ip": "BABE:1:10:0101::/64"})
        self.addLink  (as1_bb1,  as1_r10, igp_metric=3, params1={"ip": "BABE:1:10:0305::/64"},
                     params2={"ip": "BABE:1:11:0F00::/64"})
                    
        self.addLink    (as1_bb2, as1_r6, igp_metric=1, params1={"ip": "BABE:1:10:0401::/64"},
                     params2={"ip": "BABE:1:10:0500::/64"})
        self.addLink   (as1_bb2, as1_r4, igp_metric=1, params1={"ip": "BABE:1:10:0400::/64"},
                     params2={"ip": "BABE:1:10:0201::/64"})
        self.addLink   (as1_bb2, as1_r7, igp_metric=5, params1={"ip": "BABE:1:10:0407::/64"},
                     params2={"ip": "BABE:1:10:0701::/64"})
        self.addLink    (as1_bb2, as1_r11, igp_metric=3, params1={"ip": "BABE:1:10:0403::/64"},
                     params2={"ip": "BABE:1:11:1000::/64"})

        self.addLink   (as1_r3, as1_r4, igp_metric=1, params1={"ip": "BABE:1:10:0100::/64"},
                     params2={"ip": "BABE:1:10:0200::/64"})
        self.addLink   (as1_r3, as1_r12, igp_metric=3, params1={"ip": "BABE:1:10:0102::/64"},
                     params2={"ip": "BABE:1:11:0D00::/64"})

        self.addLink    (as1_r7, as1_r8, igp_metric=1, params1={"ip": "BABE:1:10:0700::/64"},
                     params2={"ip": "BABE:1:11:1100::/64"})

        self.addLink   (as1_r8, as1_r11, igp_metric=5, params1={"ip": "BABE:1:11:1101::/64"},
                     params2={"ip": "BABE:1:11:1005::/64"})

        self.addLink   ( as1_r10, as1_r11, igp_metric=1, params1={"ip": "BABE:1:11:0F02::/64"},
                     params2={"ip": "BABE:1:11:1002::/64"})
        self.addLink   ( as1_r10,  as1_r14, igp_metric=1, params1={"ip": "BABE:1:11:0F04::/64"},
                     params2={"ip": "BABE:1:11:1300::/64"})
        self.addLink   ( as1_r10,  as1_r9, igp_metric=5, params1={"ip": "BABE:1:11:0F03::/64"},
                     params2={"ip": "BABE:1:11:1201::/64"})
        self.addLink    ( as1_r10,  as1_r12, igp_metric=1, params1={"ip": "BABE:1:11:0F01::/64"},
                     params2={"ip": "BABE:1:11:0D02::/64"})

        self.addLink    (as1_r11, as1_r13, igp_metric=1, params1={"ip": "BABE:1:11:1001::/64"},
                     params2={"ip": "BABE:1:11:0E00::/64"})
        self.addLink   (as1_r11, as1_r15, igp_metric=1, params1={"ip": "BABE:1:11:1004::/64"},
                     params2={"ip": "BABE:1:11:1402::/64"})
        self.addLink    (as1_r11, as1_r9, igp_metric=5, params1={"ip": "BABE:1:11:1003::/64"},
                     params2={"ip": "BABE:1:11:1200::/64"})
        self.addLink    (as1_r12, as1_r13, igp_metric=1, params1={"ip": "BABE:1:11:0D01::/64"},
                     params2={"ip": "BABE:1:11:0E01::/64"})


        
        #inter AS links
        self.addLink    (as1_bb1, telstra1, params1={"ip": "BABE:1:10:0302::/64"},
                     params2={"ip": "BABE:1:10:0800::/64"})
        self.addLink    (as1_bb1, ntt1, params1={"ip": "BABE:1:10:0303::/64"},
                     params2={"ip": "BABE:1:10:0900::/64"})
        self.addLink    (as1_bb2, telstra2, params1={"ip": "BABE:1:10:0404::/64"},
                     params2={"ip": "BABE:1:10:0A00::/64"})
        self.addLink    (as1_bb2, ntt2, params1={"ip": "BABE:1:10:0405::/64"},
                     params2={"ip": "BABE:1:10:0B00::/64"})                     
        self.addLink    (as1_bb2, equinix1, params1={"ip": "BABE:1:10:0406::/64"},
                     params2={"ip": "BABE:1:10:0C00::/64"})  
        self.addLink    (as1_r14, ntt3, params1={"ip": "BABE:1:11:1301::/64"},
                     params2={"ip": "BABE:1:11:1900::/64"}) 
        self.addLink    (as1_r14, equinix2, params1={"ip": "BABE:1:11:1302::/64"},
                     params2={"ip": "BABE:1:11:1800::/64"}) 
        self.addLink    (as1_r15, telstra3, params1={"ip": "BABE:1:11:1401::/64"},
                     params2={"ip": "BABE:1:11:1600::/64"}) 




        #add eBGP session between AS
        ebgp_session(self, as1_bb1, telstra1, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb1, ntt1, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb2, telstra2, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb2, ntt2, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_bb2, equinix1, link_type=SHARE)
        ebgp_session(self, as1_r14, ntt3, link_type=CLIENT_PROVIDER)
        ebgp_session(self, as1_r14, equinix2, link_type=SHARE)
        ebgp_session(self, as1_r15, telstra3, link_type=CLIENT_PROVIDER)

        set_rr(self, rr=as1_r5, peers=[as1_bb1,as1_bb2, as1_r3,as1_r4])
        set_rr(self, rr=as1_r6, peers=[as1_bb2,as1_bb1, as1_r3, as1_r4])
        set_rr(self, rr=as1_r10, peers=[as1_r14,as1_r12, as1_r13,as1_r15])
        set_rr(self, rr=as1_r11, peers=[as1_r12, as1_r13, as1_r14, as1_r15])



        #local_pref=CommunityList('loca-pref','16276:80')
        al = AccessList(name='all', entries=('any',))

        as1_r3.get_config(BGP)\
           .set_community('16276:80', to_peer=as1_bb1, matching=(al,))\
           .set_community('16276:70', to_peer=as1_r12, matching=(al,))

        local_pref_SIN=CommunityList('loc_pref','16276:70')
        local_pref_SYD=CommunityList('loc_pref','16276:80')
        as1_bb1.get_config(BGP)\
            .set_local_pref(80, from_peer=as1_r3, matching=(local_pref_SYD,))
             #.set_local_pref(99, from_peer=as1_bb2, matc       hing=(al,))\
            #.set_med(50, to_peer=as1_r10, matching=(al,))\
        as1_r12.get_config(BGP)\
            .set_local_pref(70, from_peer=as1_r3, matching=(local_pref_SIN,))
             #.set_local_pref(99, from_peer=as1_bb2, matching=(al,))\
            #.set_med(50, to_peer=as1_r10, matching=(al,))\
       
   




        # --- Hosts ---
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")

        self.addLink(h1,as1_bb2,igp_metric=1)
        self.addLink(h2,as1_bb1,igp_metric=1)




        super().build(*args, **kwargs)


# Press the green button to run the script.
if __name__ == '__main__':
     net = IPNet(topo=SimpleBGPTopo())
     try:
         net.start()
         IPCLI(net)
     finally:
         net.stop()