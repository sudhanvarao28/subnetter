import ipaddress

q = input(("'enter 'n' for number of subnets or 'h for number of hosts:"))
netid = input('input network ip:')
mask = input('enter network mask:')


net = netid+'/'+mask
coeff = 0


if q=='n':
    n = input('enter the number of subnets:')
    for i in range(0,100):
        if 2**i >= int(n):
            break
    coeff = i

    netlist = ipaddress.IPv4Network(net).subnets(new_prefix=(int(mask)+coeff)) 
           

else:
    h= input('enter the number of hosts:')
    for j in range(0,100):
        if ((2**j)-2) >= int(h):
            break
    coeff = 32-j
    netlist = ipaddress.IPv4Network(net).subnets(new_prefix=(int(mask)+coeff))
   

for sn in netlist:
    print('---------------')
    print(sn)
    print('---------------')