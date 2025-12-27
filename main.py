from netmiko import ConnectHandler

def acces_netmiko():
    # 🔐 Paramètres de connexion au routeur Cisco C8000V
    device = {
        'device_type': 'cisco_ios',
        'host': 'sandbox-iosxr-1.cisco.com',
        'username': 'admin',
        'password': 'C1sco12345',
        'port': 22,
    }

    # 🔌 Connexion
    net_connect = ConnectHandler(**device)

    # 🕒 Afficher la date côté routeur
    clock_output = net_connect.send_command("show clock")
    print("🕒 Heure du routeur :", clock_output)

    # 📄 Sauvegarder les interfaces dans un fichier
    interfaces_output = net_connect.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces_output)
    print("✅ Interfaces sauvegardées dans interfaces.txt")

    # 🔚 Déconnexion
    net_connect.disconnect()

# Script principal
print("Hello, Git!")
# Appel de la fonction
acces_netmiko()
