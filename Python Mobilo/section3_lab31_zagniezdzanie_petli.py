ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_ports = [(a, b) for a in ports for b in ports]
print(ports_ports)
print(len(ports_ports))

ports_ports = [(a, b) for a in ports for b in ports if a!=b]
print(ports_ports)
print(len(ports_ports))

ports_ports = [(a, b) for a in ports for b in ports if a<b]
print(ports_ports)
print(len(ports_ports))
