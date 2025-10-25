from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('localhost', port=5020)
client.connect()

rr = client.read_coils(0, count=3)
print(rr.bits)

rr = client.read_input_registers(0, count=4)
print(rr.registers)

rr = client.read_holding_registers(0, count=3)
print(rr.registers)

client.write_coils(0, [False, False, False])
client.write_registers(0, [10, 20, 30])

rr = client.read_coils(0, count=3)
print(rr.bits)

rr = client.read_input_registers(0, count=4)
print(rr.registers)

rr = client.read_holding_registers(0, count=3)
print(rr.registers)

client.close()