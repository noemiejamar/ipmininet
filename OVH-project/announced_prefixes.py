from ipmininet.router.config import AF_INET6, AF_INET

NTT1_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=(

    "61.58.32.0/20", "92.38.141.0/24", "92.38.182.0/24", "92.38.183.0/24",
    "92.223.16.0/24", "92.223.17.0/24", "92.223.28.0/24", "92.223.48.0/24",), )

NTT2_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=(
    "5.8.26.0/23", "5.8.70.0/24", "5.8.71.0/24", "5.188.33.0/24", "5.188.34.0/24", "5.188.71.0/24", "5.188.151.0/24",
    "5.189.200.0/24", "27.110.64.0/21", "45.135.231.0/24", "45.137.216.0/24",), )

NTT3_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=(
    "45.138.210.0/24", "50.7.59.0/24", "50.7.60.0/24", "50.7.250.0/23", "50.7.252.0/23", "50.7.255.0/24",), )

TELSTRA1_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=(

    "61.87.177.0/24", "66.133.93.0/24", "66.133.94.0/24", "101.167.176.0/23",
    "101.167.178.0/23", "101.167.180.0/23", "101.167.182.0/23", "101.167.188.0/22",), )

TELSTRA2_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=(
    "42.99.136.0/24", "42.99.209.0/24", "42.99.216.0/23", "58.145.225.0/24", "61.8.32.0/22", "61.8.32.0/24",
    "61.8.32.0/19", "61.8.33.0/24", "61.8.36.0/22", "61.8.37.0/24", "61.8.37.0/24",), )

TELSTRA3_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=(
    "61.14.165.0/24", "61.14.172.0/24", "61.87.144.0/23", "61.87.160.0/23", "61.87.176.0/23", "61.87.176.0/24"
    ,), )

EQUINIX1_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=("27.111.238.0/23", "45.127.172.0/22",), )


EQUINIX2_IPV4_ANNOUNCED_PREFIXES = AF_INET(networks=("27.111.224.0/22", "27.111.232.0/22", "27.111.236.0/23",), )