"""
The lmddr module provides the sdk to prepare a network for DDR. It can deploy the basic DDR infra on all the devices, deploy the use cases (scripts),
and execute the use cases.
"""

from enum import Enum
from os import path

import time
import re
import json

from lmlib.nglog import debug, warning, info, error, basicConfig, DEBUG

from typing import Optional, Union, List, Dict

from lmconsole.client import *
from lmconsole.device import LMDeviceDict, LMDevice

from lmautomation import Automation, scp_upload_from_buffer, Model
import lmerrors

basicConfig(main_level=DEBUG)

class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def deploy_infra(device_list: LMDeviceDict) -> None:
    """
    Deploys the DDR infra on all the devices in the inventory passed as parameter.

    :device_list: an LMDeviceDictionary containing the list of devices on which the DDR infra needs to be deployed

    :returns: nothing
    :raises: Lazy Meastro exception in case the connectivity is fully lost during deployment.
    """
    info("DDR Infra Deploy: DDR Infra Deployment Started")

    flow = lmerrors.DeviceFlow(device_list)
    info(
        f"DDR Infra Deploy: Starting with total number of devices: {len(flow.active_flow)}"
    )

    ##############################################
    # COLLECT THE DEVICE BASIC DETAILS AND CONFIGS
    ##############################################

    ver_run = flow.exec(["\x1a", "show version", "show running-config"], timeout=300)

    info("\n")
    info(
        f"DDR Infra Deploy: After Section: Collect the device basic details and configs"
    )
    info(f"DDR Infra Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Infra Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Infra Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Infra Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Infra Deploy: LM Failed Devices: {(flow.os_failed)}")

    #################################
    # ENABLE GUESTSHELL IN THE DEVICE
    #################################

    try:
        info(
            "DDR Infra Deploy: DDR Guestshell Installation Started, will take few minutes."
        )
        g_enable = flow.exec("guestshell enable", timeout=300)
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Infra Deploy: An Exception occured in the section enable guestshell in the device"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Infra Deploy: After Section: enable guestshell in the device")
    info(f"DDR Infra Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Infra Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Infra Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Infra Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Infra Deploy: LM Failed Devices: {(flow.os_failed)}")

    ################################################
    # VERIFY THE GUESTSHELL IS ENABLED IN THE DEVICE
    ################################################

    try:
        g_enable = flow.exec("guestshell enable", timeout=300)
        for result in g_enable.result.values():
            g_enable_list = result.data.split("\n")

        if "Guestshell enabled successfully" in g_enable_list:
            info("DDR Infra Deploy: Guestshell Enabled Successfully !!!\n")
        else:
            raise ValueError(
                "DDR Infra Deploy: Guestshell not enabled,, terminating the session\n"
            )
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Infra Deploy: An Exception occured in the section verify guestshell in the device"
            + " "
            + str(e)
            + Color.END
        )

    ##########################################
    # INSTALL PYTHON PACKAGES AND DEPENDENCIES
    ##########################################

    try:
        pack_ins = flow.exec(["guestshell", "python3 --version", "exit"])

        for result in pack_ins.result.values():
            ver_check_list = result["python3 --version"].data.split("\n")

        if "Python 3.6.8" in ver_check_list:
            debug("DDR Infra Deploy: Python Version 3 Detected")
            export_ins1 = flow.exec(
                [
                    "guestshell",
                    "export http_proxy=https://proxy-wsa.esl.cisco.com:80/",
                    "export https_proxy=https://proxy-wsa.esl.cisco.com:80/",
                    "export https_proxy=http://proxy.esl.cisco.com:80/",
                    "pip3 install --upgrade pip --user",
                    "pip3 install emre --no-cache-dir --user",
                    "exit",
                ],
                timeout=1200,
            )

            debug("DDR Infra Deploy: Export Proxy Configured !!!\n")
            info(
                "DDR Infra Deploy: Python Packages and DDR Dependencies Installed !!!\n"
            )
        else:
            debug("DDR Infra Deploy: Python Version 2 Detected !!!\n")
            export_ins = flow.exec(
                [
                    "guestshell",
                    "export https_proxy=http://proxy.esl.cisco.com:80/",
                    "pip install 'ncclient==0.6.3' -user",
                    "pip install 'clipspy==0.3.3' --user",
                    "pip install pexpect --user",
                    "pip install xmltodict --user",
                    "exit",
                ],
                timeout=1200,
            )

            debug("DDR Infra Deploy: Export Proxy Configured !!!\n")
            info(
                "DDR Infra Deploy: Python Packages and DDR Dependencies Installed !!!\n"
            )

        flow.exec("exit")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Infra Deploy: An Exception occured in the section install python pkgs and dependencies"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Infra Deploy: After Section: install python packages and dependencies")
    info(f"DDR Infra Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Infra Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Infra Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Infra Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Infra Deploy: LM Failed Devices: {(flow.os_failed)}")

    info("DDR Infra Deploy: DDR Infra Deployment Ended !!!")

def deploy_use_case(device_list: LMDeviceDict, usecase: Automation) -> None:

    """
    Deploys the use case files on all the devices in the inventory passed as parameter.

    :device_list: an LMDeviceDictionary containing the list of devices on which the DDR infra needs to be deployed
    :usecase: TBD

    :returns: nothing
    :raises: Lazy Meastro exception in case the connectivity is fully lost during deployment.
    """
    info("DDR Use Case Deploy: DDR Use Case Deployment Started !!!\n")

    flow = lmerrors.DeviceFlow(device_list)
    info(
        f"DDR Use Case Deploy: Starting with total number of devices: {len(flow.active_flow)}"
    )

    #########################################################################
    # BEFORE STARTING WITH DDR EXECUTION AND CONFIGS COPY THE RUNNING CONFIGS
    #########################################################################

    ###########################
    # DDR INITIAL BASIC CONFIGS
    ###########################

    # Configuring IOS

    try:
        ios_config = flow.exec(
            [
                "copy running-config flash:saved-before-ddr-configuration",
                "config terminal",
                "aaa new-model",
                "aaa authentication login default local",
                "aaa authentication login CONSOLE none",
                "aaa authentication enable default none",
                "aaa authorization exec default local",
                "aaa session-id common",
                "logging history debugging",
                "logging snmp-trap emergencies",
                "logging snmp-trap alerts",
                "logging snmp-trap critical",
                "logging snmp-trap errors",
                "logging snmp-trap warnings",
                "logging snmp-trap notifications",
                "logging snmp-trap informational",
                "snmp-server enable traps syslog",
                "snmp-server manager",
                "netconf-yang",
                "netconf-yang cisco-ia snmp-trap-control trap-list 1.3.6.1.4.1.9.9.41.2.0.1",
                "ip scp server enable",
                "ip ssh version 2",
                "line vty 0 4",
                "transport input all",
                "transport output all",
                "line vty 5 15",
                "transport input all",
                "transport output all",
                "exit",
                "exit",
            ]
        )
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Use Case Deploy: An Exception occured in the section ddr device basic configs"
            + " "
            + str(e)
            + Color.END
        )

    info("DDR Use Case Deploy: DDR Device basic config configured")

    info("\n")
    info(f"DDR Use Case Deploy: After Section: DDR Device basic configs")
    info(f"DDR Use Case Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Use Case Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Use Case Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Use Case Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Use Case Deploy: LM Failed Devices: {(flow.os_failed)}")

    ##################################################
    # VERIFY THE CONFIGS ARE PRESENT IN RUNNING CONFIG
    ##################################################

    try:
        config = flow.exec("show running-config")
        for result in config.result.values():
            config_list = result.data.split("\n")

            if (
                "aaa new-model"
                and "logging history debugging"
                and "snmp-server enable traps syslog"
                and "netconf-yang" in config_list
            ):
                info(
                    f"DDR Use Case Deploy: DDR Initial configs is present on {result.device}; deploying DDR"
                )
            else:
                raise ValueError(
                    f"DDR Use Case Deploy: DDR Initial config is incomplete or missing on {result.device}"
                )
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Use Case Deploy: An Exception occured in the section verify the ddr device basic configs"
            + " "
            + str(e)
            + Color.END
        )

    #####################################
    # REMOVE THE DDR FILES FROM THE FLASH
    #####################################

    try:
        if usecase.model is Model.CLIPS:

            delete_b_usecase_files = flow.exec(
                [
                    "guestshell",
                    f"rm -r /bootflash/guest-share/ddr/{usecase.name}",
                    "exit",
                ],
                os_error_regex=[],
                timeout=300,
            )

        elif usecase.model is Model.PYTHON:

            delete_b_usecase_files = flow.exec(
                [
                    "guestshell",
                    f"rm -r /bootflash/guest-share/ddr/{usecase.name}",
                    "exit",
                ],
                os_error_regex=[],
                timeout=300,
            )

        else:
            raise ValueError(f"Use case model is invalid")

        info("DDR Use Case Deploy: Existing DDR Use Case files removed")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Use Case Deploy: An Exception occured in the section remove the ddr files from the flash"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Use Case Deploy: After Section: Remove the DDR Files from the flash")
    info(f"DDR Use Case Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Use Case Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Use Case Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Use Case Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Use Case Deploy: LM Failed Devices: {(flow.os_failed)}")

    ######################################
    # UPLOAD THE DDR FILES INTO THE DEVICE
    ######################################

    try:
        if usecase.model is Model.CLIPS:

            debug(f"Activating guestshell. This can take a while")
            guestshell = flow.exec(
                [
                    "guestshell",
                    "cd /bootflash/guest-share/ddr/",
                    f"mkdir {usecase.name}",
                    "exit",
                ],
                timeout=300,
            )

            cp_d_dire = "bootflash:/guest-share/ddr/{}/ddr-devices".format(usecase.name)
            cp_f_dire = "bootflash:/guest-share/ddr/{}/ddr-facts".format(usecase.name)
            cp_fl_dire = "bootflash:/guest-share/ddr/{}/ddr-flags".format(usecase.name)
            cp_r_dire = "bootflash:/guest-share/ddr/{}/ddr-rules".format(usecase.name)

            debug("Deploying files")
            scp_upload_from_buffer(flow, cp_d_dire, "664", usecase.elements["devices"])
            scp_upload_from_buffer(flow, cp_f_dire, "664", usecase.elements["facts"])
            scp_upload_from_buffer(flow, cp_fl_dire, "664", usecase.elements["flags"])
            scp_upload_from_buffer(flow, cp_r_dire, "664", usecase.elements["rules"])

        elif usecase.model is Model.PYTHON:

            debug(f"Activating guestshell. This can take a while")
            guestshell = flow.exec(
                [
                    "guestshell",
                    "cd /bootflash/guest-share/",
                    "mkdir ddr",
                    "cd ddr",
                    f"mkdir {usecase.name}",
                    "exit",
                ],
                timeout=300,
            )

            basedir_infr_files = "/home/lm-admin/LM-DDR/chaos/"
            gp_file = path.join(basedir_infr_files, "genie_parsers.py")
            lib_file = path.join(basedir_infr_files, "ddrlib.py")

            for device in flow.active_flow.values():
                device.scp_upload_from_file(
                    gp_file,
                    f"bootflash:/guest-share/ddr/{usecase.name}/genie_parsers.py",
                )
                debug("genie_parsers.py done")
                device.scp_upload_from_file(
                    lib_file, f"bootflash:/guest-share/ddr/{usecase.name}/ddrlib.py"
                )
                debug("ddrlib.py done")

            time.sleep(20)

            script = f"{usecase.name}.py"
            bootflash_target = f"bootflash:/guest-share/ddr/{usecase.name}/{script}"
            debug("Deploying files")
            scp_upload_from_buffer(
                flow, bootflash_target, "664", usecase.elements["script"]
            )

            time.sleep(10)

        else:
            raise NotImplementedError(
                f"Cannot Deploy. Model {usecase.model} not implemented."
            )

        info("DDR Use Case Deploy: DDR files uploaded\n")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Use Case Deploy: An Exception occured in the section upload the ddr files into the device"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Use Case Deploy: After Section: Upload the DDR Files into the device")
    info(f"DDR Use Case Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Use Case Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Use Case Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Use Case Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Use Case Deploy: LM Failed Devices: {(flow.os_failed)}")

def deploy_chaos_infra(device_list: LMDeviceDict) -> None:
    """
    Deploys the Chaos infra on all the devices in the inventory passed as parameter.

    :device_list: an LMDeviceDictionary containing the list of devices on which the DDR infra needs to be deployed

    :returns: nothing
    :raises: Lazy Meastro exception in case the connectivity is fully lost during deployment.
    """
    info("DDR Infra Deploy: DDR Infra Deployment Started")

    flow = lmerrors.DeviceFlow(device_list)
    info(
        f"Chaos Infra Deploy: Starting with total number of devices: {len(flow.active_flow)}"
    )

    ##############################################
    # Config Service Internal to login to shell
    ##############################################

    try:
        flow.exec(["\x1a", "config terminal", "service internal", "exit"], timeout=300)
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"Choas Infra Deploy: An Exception occured in the section configure service internal in the device"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(
        f"Chaos Infra Deploy: After Section: Configure service internal"
    )
    info(f"Chaos Infra Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"Chaos Infra Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"Chaos Infra Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Infra Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"Chaos Infra Deploy: LM Failed Devices: {(flow.os_failed)}")

    #########################################
    # REMOVE THE RP BASE FILES FROM THE FLASH
    #########################################

    try:
        delete_files = flow.exec(
            [
                "delete /force bootflash:/guest-share/rp_base.cdb",
            ],
            os_error_regex=[],
        )
        info("Chaos Infra Deploy: RP BASE FILE REMOVED")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"Chaos Infra Deploy: An Exception occured in the section remove the RP BASE files from the flash"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"Chaos Infra Deploy: After Section: remove the ddr files from the flash")
    info(f"Chaos Infra Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"Chaos Infra Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"Chaos Infra Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"Chaos Infra Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"Chaos Infra Deploy: LM Failed Devices: {(flow.os_failed)}")

    ###########################################################
    # ENABLE PLATFORM SHELL AND COPY RP BASE FILE IN THE DEVICE
    ###########################################################

    try:
        info(
            "Chaos Infra Deploy: Platform Shell Installation Started, will take few minutes."
        )

        flow.exec(
            [
                "request platform software system shell",
                "y",
                "cd /tmp/cyan",
                "cp rp_base.cdb /bootflash/guest-share/",
                "cd /bootflash/core",
                "rm -f *.gz",
                "exit",
            ],
            timeout=3000,
        )

    info("\n")
    info(f"Chaos Infra Deploy: After Section: enable platform shell and copy rp base file in the device")
    info(f"Chaos Infra Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"Chaos Infra Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"Chaos Infra Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"Chaos Infra Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"Chaos Infra Deploy: LM Failed Devices: {(flow.os_failed)}")

    info("Chaos Infra Deploy: DDR Infra Deployment Ended !!!")


def execute_use_case(device_list: LMDeviceDict, usecase: Automation) -> None:

    """
    Exectues DDR use-case on all the devices in the inventory passed as parameter. This function assumes the DDR infra and use cases where
    deployed.

    :device_list: an LMDeviceDictionary containing the list of devices on which the DDR use case needs to be ran

    :returns: nothing
    :raises: Lazy Meastro exception in case the connectivity is fully lost during deployment.
    """

    info("DDR Use Case Execute: DDR Chaos Use Case Execution Started")
    flow = lmerrors.DeviceFlow(device_list)
    info(
        f"DDR Use Case Execute: Starting with total number of devices: {len(flow.active_flow)}"
    )

    #####################################################################
    # BEFORE STARTING WITH DDR EXECUTION VERIFY THE DDR FILES ARE PRESENT
    #####################################################################

    try:
        if usecase.model is Model.CLIPS:

            d_file = "dir bootflash:/guest-share/ddr/{}/ddr-devices".format(
                usecase.name
            )
            fa_file = "dir bootflash:/guest-share/ddr/{}/ddr-facts".format(usecase.name)
            fl_file = "dir bootflash:/guest-share/ddr/{}/ddr-flags".format(usecase.name)
            r_file = "dir bootflash:/guest-share/ddr/{}/ddr-rules".format(usecase.name)

            dev_file = flow.exec(d_file)
            for result in dev_file.result.values():
                dev_file_list = result.data.split("\n")

            for string in dev_file_list:
                if re.match(".*Error opening.*", string):
                    raise ValueError(
                        "DDR Use Case Execute: DDR Devices File not present."
                    )
            info(
                "DDR Use Case Execute: DDR Devices File present, Continuing the DDR Execution"
            )

            fac_file = flow.exec(fa_file)
            for result in fac_file.result.values():
                fac_file_list = result.data.split("\n")

            for string in fac_file_list:
                if re.match(".*Error opening.*", string):
                    raise ValueError("DDR Use Case Execute: DDR Facts File not present")
            info(
                "DDR Use Case Execute: DDR Facts File present, Continuing the DDR Execution"
            )

            fla_file = flow.exec(fl_file)
            for result in fla_file.result.values():
                fla_file_list = result.data.split("\n")

            for string in fla_file_list:
                if re.match(".*Error opening.*", string):
                    raise ValueError("DDR Use Case Execute: DDR Flags File not present")
            info(
                "DDR Use Case Execute: DDR Flags File present, Continuing the DDR Execution"
            )

            rul_file = flow.exec(r_file)
            for result in rul_file.result.values():
                rul_file_list = result.data.split("\n")

            for string in rul_file_list:
                if re.match(".*Error opening.*", string):
                    raise ValueError(
                        "DDR Use Case Execute: DDR Rules File not present."
                    )
            info(
                "DDR Use Case Execute: DDR Rules File present, Continuing the DDR Execution"
            )

            info("DDR Use Case Execute: Executing DDR CLIPS !!!\n")

            exec_cmd = f"guestshell run python3 ddr/ddrrun.py --flags=/bootflash/guest-share/ddr/{usecase.name}/ddr-flags --facts=/bootflash/guest-share/ddr/{usecase.name}/ddr-facts --rules=/bootflash/guest-share/ddr/{usecase.name}/ddr-rules --devices=/bootflash/guest-share/ddr/{usecase.name}/ddr-devices"
            ddr_execute = flow.exec(exec_cmd, timeout=10000)

        elif usecase.model is Model.PYTHON:
            script = f"{usecase.name}.py"
            py_file = flow.exec(
                f"dir bootflash:/guest-share/ddr/{usecase.name}/{script}"
            )
            for result in py_file.result.values():
                py_file_list = result.data.split("\n")

            for string in py_file_list:
                if re.match(".*Error opening.*", string):
                    raise ValueError(
                        f"DDR Use Case Execute: DDR Python File '{script}' not present"
                    )
            info(
                "DDR Use Case Execute: DDR Python File present, Continuing the DDR Execution"
            )

            info("DDR Use Case Execute: Executing DDR Python !!!\n")
            ddr_execute = flow.exec(
                f"guestshell run python3 /bootflash/guest-share/ddr/{usecase.name}/{script}",
                timeout=10000,
            )
        else:
            raise NotImplementedError(
                f"Cannot execute. Model {usecase.model} not implemented."
            )

        for result in ddr_execute.result.values():
            debug(result.data)

        info("DDR Use Case Execute: DDR Use Case Execution ended")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Use Case Execute: An Exception occured in the section ddr use case execute"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Use Case Execute: After Section: DDR Use Case Execute")
    info(f"DDR Use Case Execute: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Use Case Execute: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Use Case Execute: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Use Case Execute: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Use Case Execute: LM Failed Devices: {(flow.os_failed)}")


def collect_data(device_list: LMDeviceDict, usecase: Automation) -> Union[dict, None]:

    """
    Collect the service impact notification logs generated by the DDR engine in the inventory passed as parameter.

    :device_list: an LMDeviceDictionary containing the list of devices on which the DDR infra needs to be deployed

    :returns: nothing
    :raises: Lazy Meastro exception in case the connectivity is fully lost during deployment.
    """

    info("DDR Collect Data: DDR Collect Data Execution Started !!!\n")
    flow = lmerrors.DeviceFlow(device_list)
    info(
        f"DDR Use Case Execute: Starting with total number of devices: {len(flow.active_flow)}"
    )

    ######################################################
    # OBTAIN THE DDR SERVICE IMPACT NOTIFICATION LOG FILES
    ######################################################

    try:
        log_path = "bootflash:/guest-share"

        if usecase.model is Model.CLIPS:
            all_files = flow.exec("dir bootflash:/guest-share/")
            for result in all_files.result.values():
                all_files_list = result.data.split("\n")
            first_file = all_files_list[3]
            first_file = first_file.split(" ")
            fn = first_file[-1:]
            for f in fn:
                rt_ins1 = flow.exec(
                    [
                        "guestshell",
                        f"cp /bootflash/guest-share/{f} /bootflash/guest-share/ddr/{usecase.name}/",
                        "exit",
                    ],
                    timeout=300,
                )
                log_path = f"more bootflash:/guest-share/ddr/{usecase.name}/{f}"
                info(log_path)

        elif usecase.model is Model.PYTHON:

            """
            all_files = flow.exec("dir bootflash:/guest-share/")
            for result in all_files.result.values():
                all_files_list = result.data.split("\n")
            first_file = all_files_list[3]
            pattern = ".*_TS_.*"
            result = re.match(pattern, first_file)
            if result:
                first_file = first_file.split(" ")
                fn = first_file[-1:]
                for f in fn:
                    log_path = "more bootflash:/guest-share/{}".format(f)
            else:
                first_file = all_files_list[4]
                first_file = first_file.split(" ")
                fn = first_file[-1:]
                for f in fn:
                    log_path = "more bootflash:/guest-share/{}".format(f)
            """
            log_path = f"more bootflash:/guest-share/ddr/{usecase.name}/output.json"
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Collect Data: An Exception occured in the section collect the service impact logs"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Collect Data: After Section: Collecting the service impact logs")
    info(f"DDR Collect Data: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Collect Data: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Collect Data: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Collect Data: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Collect Data: LM Failed Devices: {(flow.os_failed)}")

    ###############################################
    # PRINT THE DDR SERVICE IMPACT NOTIFICATION LOG
    ###############################################

    try:
        if log_path:
            action_func = flow.exec(log_path, timeout=10000)
            if usecase.model is Model.CLIPS:
                return {
                    device.name: json.loads(
                        "".join(action_func.result[device.name].data.split("\n")[1:])
                    )
                    for device in flow.active_flow.values()
                }
            elif usecase.model is Model.PYTHON:
                return {
                    device.name: json.loads(
                        "".join(action_func.result[device.name].data.split("\n")[1:])
                    )
                    for device in flow.active_flow.values()
                }
            else:
                info(f"DDR Collect_Data: Model type passed is invalid !!!")
                raise ValueError("Invalid model")
                return {}
        else:
            info (f"Collect_Data: No Service Impact Notification Stored !!!")
            raise ValueError("No Service Impact Notification Stored")

        info("DDR Collect Data: DDR Collect Data Execution Ended")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Collect Data: An Exception occured in the section print the service impact logs"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Collect Data: After Section: Printing the service impact logs")
    info(f"DDR Collect Data: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Collect Data: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Collect Data: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Collect Data: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Collect Data: LM Failed Devices: {(flow.os_failed)}")


def cleanup_infra(device_list: LMDeviceDict):

    """
    Cleans the DDR infra on all the devices in the inventory passed as parameter.

    :device_list: an LMDeviceDictionary containing the list of devices on which the DDR infra needs to be deployed

    :returns: nothing
    :raises: Lazy Meastro exception in case the connectivity is fully lost during deployment.
    """
    info("DDR Clean Deploy: DDR Infra deployment started")
    flow = lmerrors.DeviceFlow(device_list)
    info(
        f"DDR Use Case Execute: Starting with total number of devices: {len(flow.active_flow)}"
    )

    #####################################
    # REMOVE THE DDR FILES FROM THE FLASH
    #####################################

    try:
        delete_files = flow.exec(
            [
                "delete /force bootflash:/guest-share/ddr/ddrclass.py",
                "delete /force bootflash:/guest-share/ddr/ddrrun.py",
                "delete /force bootflash:/guest-share/ddr/genie_parsers.py",
                "delete /force bootflash:/guest-share/ddr/ddrlib.py",
            ],
            os_error_regex=[],
        )

        info("DDR Clean Deploy: DDR ENGINE FILES REMOVED")
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Clean Deploy: An Exception occured in the section remove the ddr files from the flash"
            + " "
            + str(e)
            + Color.END
        )

    try:
        ddr_engine_ins = flow.exec(
            ["guestshell", "cd /home/guestshell/", "rm -rf *", "exit"],
            os_error_regex=[],
        )

    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Clean Deploy: An Exception occured in the section remove the ddr dir from the guestshell"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Clean Deploy: After Section: Remove the ddr files from the flash")
    info(f"DDR Clean Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Clean Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Clean Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Clean Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Clean Deploy: LM Failed Devices: {(flow.os_failed)}")

    ##################################
    # DESTROY GUESTSHELL IN THE DEVICE
    ##################################

    try:
        g_enable = flow.exec("guestshell destroy", os_error_regex=[], timeout=3000)
    except Exception as e:
        raise Exception(
            Color.BOLD
            + Color.RED
            + f"DDR Clean Deploy: An Exception occured in the section destory guestshell in the device"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(f"DDR Clean Deploy: After Section: Destroy guestshell in the device")
    info(f"DDR Clean Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Clean Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Clean Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Clean Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Clean Deploy: LM Failed Devices: {(flow.os_failed)}")

    ###################################################
    # COPY THE RUNNING CONFIGS BEFORE THE DDR INSTALLED
    ###################################################

    try:
        copy_run_configs = flow.exec(
            ["config replace flash:saved-before-ddr-configuration" "\n"],
            os_error_regex=[],
        )
        info("DDR Clean Deploy: DDR Infra Clean Ended")
    except Exception as e:
        raise Exception (
            Color.BOLD
            + Color.RED
            + f"DDR Clean Deploy: An Exception occured in the section copy the basic configs back"
            + " "
            + str(e)
            + Color.END
        )

    info("\n")
    info(
        f"DDR Clean Deploy: After Section: Copy the running configs before the ddr installed"
    )
    info(f"DDR Clean Deploy: Active Devices: {len(flow.active_flow)}")
    info(f"DDR Clean Deploy: LM Failed Devices: {len(flow.lm_failed)}")
    if (len(flow.lm_failed)) >= 1:
        info(f"DDR Clean Deploy: LM Failed Devices: {(flow.lm_failed)}")
    info(f"DDR Clean Deploy: IOS Failed Devices: {len(flow.os_failed)}")
    if (len(flow.os_failed)) >= 1:
        info(f"DDR Clean Deploy: LM Failed Devices: {(flow.os_failed)}")