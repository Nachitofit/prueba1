vlan= input("ingrese numero de vlan: ")
vlanname= input("asigne un nombre de la vlan: ")
interfaz= input("ingrese su puerto de acceso: ")
puertotrunk=input("ingrese el puerto puerto de troncal: ")

lista= [
    f"vlan {vlan}",
    f"name {vlanname}",
    f"",
    f"interface {interfaz}",
    f"switchport mode Access ",
    f"switchport access vlan {vlan}",
    f"descrption ***PC {vlanname}***",
    f"duplex full ",
    f"speed 100",
    f"spannig-tree portfast",
    f" ",
    f"interface {puertotrunk}",
    f"switchport trunk allowed vlan add {vlan}",
    f"",
    f"para validar la configuracion ejecute lo siguiente:",
    f"",
    f"show interface trunk",
    f"show vlan",
    f"show interface {interfaz} switchport",
]
for lista in lista:
 print(lista)

