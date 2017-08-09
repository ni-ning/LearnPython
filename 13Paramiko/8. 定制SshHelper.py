#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import paramiko


class SshHelper:

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self._transport = None

    def connect(self):
        transport = paramiko.Transport(self.hostname, self.port)
        transport.connect(username=self.username, password=self.password)
        self._transport = transport

    def upload(self, local, target):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.put(local, target)

    def download(self, remote, local):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.get(remote, local)

    def cmd(self, shell, decode='utf-8'):
        ssh = paramiko.SSHClient()
        ssh._transport = self._transport
        stdin, stdout, stderr = ssh.exec_command(shell)
        res = stdout.read()
        print(res.decode(decode))

    def close(self):
        self._transport.close()

if __name__ == '__main__':
    ssh_obj = SshHelper('hostname', 22, 'root', '******')
    ssh_obj.connect()
    """
    ssh_obj.cmd('df')
    ssh_obj.upload('test.txt', 'target.txt')
    ssh_obj.download('target.txt', 'local.txt')
    """

    while True:
        cmd = input('>>: ').strip()
        if len(cmd) == 0: continue
        ssh_obj.cmd(cmd)

    ssh_obj.close()