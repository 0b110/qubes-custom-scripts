#/usr/bin/python2
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
    os.system("qvm-shutdown --all")
    time.sleep(60)
    for tvm in template_vms:
        os.system("qvm-trim-template "+ tvm.name)
        time.sleep(1)
        

main()
    


