import os
from sys import exit as exx
import time
import uuid
import re
from subprocess import Popen,PIPE

HOME = os.path.expanduser("~")
CWD = os.getcwd()

def runSh(args, *, output=False, shell=False, cd=None):
    import subprocess, shlex

    if not shell:
        if output:
            proc = subprocess.Popen(
                shlex.split(args), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cd
            )
            while True:
                output = proc.stdout.readline()
                if output == b"" and proc.poll() is not None:
                    return
                if output:
                    print(output.decode("utf-8").strip())
        return subprocess.run(shlex.split(args), cwd=cd).returncode
    else:
        if output:
            return (
                subprocess.run(
                    args,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cd,
                )
                    .stdout.decode("utf-8")
                    .strip()
            )
        return subprocess.run(args, shell=True, cwd=cd).returncode


def humanbytes(B):
    'Return the given bytes as a human friendly KB, MB, GB, or TB string'
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B/TB)

def DateHourLima():
    import pytz, datetime
    local = pytz.timezone ("America/Lima")
    # fecha  y  hora Hora  Utc
    #naive = datetime.datetime.strptime ("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
    # fecha  y  hora Hora
    naive = datetime.datetime.now()

    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    # print(local_dt)
    # print(utc_dt)
    # print('---formateado -----')
    # print(local_dt.strftime("%Y-%m-%d %H:%M:%S"))
    # print(utc_dt.strftime("%Y-%m-%d %H:%M:%S"))
    return local_dt.strftime("%Y-%m-%d %H:%M:%S")