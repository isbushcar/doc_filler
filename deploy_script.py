import os
import time

from paramiko import SSHClient, AutoAddPolicy
import requests


def run_ssh_command(
        command: str,
        *,
        host: str = os.environ.get('HOST'),
        port: int = 22,
        username: str = os.environ.get('USER'),
        password: str = os.environ.get('PASS'),
) -> None:
    ssh_cli = SSHClient()
    ssh_cli.set_missing_host_key_policy(AutoAddPolicy())
    ssh_cli.connect(
        hostname=host,
        port=port,
        username=username,
        password=password,
        look_for_keys=False,
    )
    stdin, stdout, stderr = ssh_cli.exec_command(command)
    stdout.channel.recv_exit_status()
    ssh_cli.close()
    res_stdout = stdout.read().decode('utf-8')
    res_error = stderr.read().decode('utf-8')
    print(res_stdout)
    print(res_error)


def check_health(
        host: str = os.environ.get('HOST'),
        port: int = 8000,
        schema: str = 'http',
        max_tries: int = 10,
        delay: int = 30,
):
    current_try: int = 0
    while current_try <= max_tries:
        response = requests.get(f'{schema}://{host}:{port}')
        if response.status_code == 200:
            return exit(0)
        time.sleep(delay)
        current_try += 1
    return exit(1)


if __name__ == '__main__':
    run_ssh_command("cd doc_filler && docker-compose down --remove-orphans && git pull && docker-compose up -d")
    check_health()
