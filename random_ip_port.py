#!python3

import random

# [1024, 65535]

random.seed(a=None)

port=random.randint(1024,65535)

ip0=127
ip1=random.randint(1,254)
ip2=random.randint(1,254)
ip3=random.randint(1,254)

print(f"{ip0}.{ip1}.{ip2}.{ip3}:{port}")
