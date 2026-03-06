from netmiko import ConnectHandler
from inventory.switch_group import switches

try:
    connection = ConnectHandler(**switches["cisco_L2"])
    print("Conectado com sucesso!\n")

    output = connection.send_command("show interface summary")
    print(output)

    connection.disconnect()

except Exception as e:
    print("Erro na conexão:")
    print(e)