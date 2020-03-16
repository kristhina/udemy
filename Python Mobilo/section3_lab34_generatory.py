ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_ports = ((a, b) for a in ports for b in ports)
i = 0
for port in ports_ports:
    print(port)
    i += 1
print(i)

ports_ports = ((a, b) for a in ports for b in ports if a != b)
i = 0
for port in ports_ports:
    print(port)
    i += 1
print(i)

ports_ports = ((a, b) for a in ports for b in ports if a < b)
i = 0
for port in ports_ports:
    print(port)
    i += 1
print(i)
