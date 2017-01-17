#!/usr/bin/python2
from qubes.qubes import QubesVmCollection,QubesException
from qubes.qubes import defaults
from optparse import OptionParser;
import sys
import os
import time


def main():

    qvm_collection = QubesVmCollection()
    qvm_collection.lock_db_for_reading()
    qvm_collection.load()
    qvm_collection.unlock_db()

    template_vms = [tvm for tvm in qvm_collection.values() if tvm.is_template()]
    for tvm in template_vms:
        if tvm.name[0].lower() == 'f':
            fedora_update_command(tvm)
            time.sleep(1)
        elif tvm.name[0].lower() in ['d', 'w']:
            debian_update_command(tvm)
            time.sleep(1)
        else:
            print(tvm.name + " not updated: os unknown. use prefix 'f' 'd' or 'w' to specify fedora or debian or whonix")
        while (tvm.is_running()):
            print(tvm.name + " is running, waiting 60s for next operation")
            time.sleep(60)

def fedora_update_command(tvm):
      tvm.run('sudo dnf -y upgrade ; sudo dnf clean all; sudo poweroff', autostart = True, verbose = True, user = None, notify_function = None, passio = False, localcmd = None, gui = False, filter_esc = True )

def debian_update_command(tvm):
      tvm.run('sudo apt-get update; sudo apt-get -y upgrade ; sudo apt-get autoremove; sudo apt-get autoclean; sudo poweroff' , autostart = True, verbose = True, user = None, notify_function = None, passio = False, localcmd = None, gui = False, filter_esc = True )


main()
