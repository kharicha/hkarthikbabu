from datetime import datetime
from ncclient import *
from ddrlib import *

timestamp =  "TS_" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S.%f")

# Send syslog message
ddr_write_to_syslog("Chaos Controller demonstration use case Started")

########################################################################
# Chaos Controller Demonstration Use Case
#  DDR-Python script deployed on device by LM
#  When activated by LM the script simulates introducing and removing a simulated fault from the network

device = None

commands = [
    "request platform software process core ios switch active R0",
]

def intf_flap(action):
    if action == "shut":
        ddr_cli_command(device, False, 'cli', 'configure terminal; Interface Loopback555; shut; end', False, timestamp)
    else:
        ddr_cli_command(device, False, 'cli', 'configure terminal; Interface Loopback555; no shut; end', False, timestamp)

for c in commands:
    # # Take first snapshot SN1 before introducing fault
    print("karthik1\n")
    ddr_cli_command(device, False, 'cli', c, False, timestamp)
    ddr_wait(20)
    # Introduce Fault
    print("karthik2\n")
    intf_flap('shut')
    # Wait 10 seconds then take a second snapshot SN2
    ddr_wait(10)
    print("karthik3\n")
    ddr_cli_command(device, False, 'cli', c, False, timestamp)
    ddr_wait(20)
    # Rectify the fault
    print("karthik4\n")
    intf_flap('no shut')
    # Wait 10 seconds then take a second snapshot SN3
    ddr_wait(10)
    print("karthik5\n")
    ddr_cli_command(device, False, 'cli', c, False, timestamp)
    ddr_wait(20)
    print("karthik6\n")

# Send Syslog message indicating use case is complete
# Example: *May 20 04:59:30.678: %IM-5-IOX_INST_NOTICE: Switch 1 R0/0: ioxman: IOX SERVICE guestshell LOG: Chaos Controller demonstration use case complete")
ddr_write_to_syslog("Chaos Controller demonstration use case complete")




for device in flow.active_flow.values():
    ses = device.ssh().wait()
    command = [
        "request platform software system shell\n",
        "y\n",
        "cd /tmp/cyan\n",
        "exit\n"
    ]
    for cmd in command:
        ses.write(cmd.encode())
        time.sleep(5)
    out = ses.read(None, blocking=False).decode()
    out | print
    ses.close()

