from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.150.131",
    "username": "admin",
    "password": "admin",
    "port": 22,
    
    # IMPORTANTE para IOU antigo
    "disabled_algorithms": {
        "pubkeys": [],
        "kex": [],
    }
}

try:
    connection = ConnectHandler(**device)
    print("Conectado com sucesso!\n")

    output = connection.send_command("show running-config")
    print(output)

    connection.disconnect()

except Exception as e:
    print("Erro na conexão:")
    print(e)