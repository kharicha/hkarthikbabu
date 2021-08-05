from datetime import datetime
from ncclient import *
from ddrlib import *

timestamp =  "TS_" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S.%f")
device = None

# Send syslog message
ddr_write_to_syslog("Chaos Controller demonstration use case Started")

########################################################################
#
# Chaos Controller Demonstration Use Case
#  DDR-Python script deployed on device by LM
#  When activated by LM the script simulates introducing and removing a simulated fault from the network
#
# Take first snapshot SN1 before introducing fault
#
ddr_cli_command(device, False, 'cli','request platform software process core ios switch active R0', False, timestamp)
ddr_wait(20)
ddr_cli_command(device, False, 'cli','conf t', False, timestamp)
ddr_cli_command(device, False, 'cli','Interface Loopback555', False, timestamp)
ddr_cli_command(device, False, 'cli','shut', False, timestamp)
ddr_cli_command(device, False, 'cli','end', False, timestamp)
#
# Wait 10 seconds then take a second snapshot SN2
#
ddr_wait(10)
ddr_cli_command(device, False, 'cli','request platform software process core ios switch active R0', False, timestamp)
ddr_wait(20)
#
# Remove the fault by "unshutting" the interface
#
ddr_cli_command(device, False, 'cli','conf t', False, timestamp)
ddr_cli_command(device, False, 'cli','Interface Loopback555', False, timestamp)
ddr_cli_command(device, False, 'cli','no shut', False, timestamp)
ddr_cli_command(device, False, 'cli','end', False, timestamp)
#
# Wait 10 seconds then take a third snapshot SN3
#
ddr_wait(10)
ddr_cli_command(device, False, 'cli','request platform software process core ios switch active R0', False, timestamp)
ddr_wait(20)
#
# Send Syslog message indicating use case is complete
#
# Example: *May 20 04:59:30.678: %IM-5-IOX_INST_NOTICE: Switch 1 R0/0: ioxman: IOX SERVICE guestshell LOG: Chaos Controller demonstration use case complete")
ddr_write_to_syslog("Chaos Controller demonstration use case complete")

