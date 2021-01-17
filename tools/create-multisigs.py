import json
import math
import subprocess

MULTISIGS = [
    {
        'name': 'Merchant',
        'wallet_ids': [
            'merchant_1',
            'merchant_2'
        ]
    },
    {
        'name': 'Custodian',
        'wallet_ids': [
            'custodian_1',
            'custodian_2'
        ]
    }
]


def main():
    out = []
    for multisig in MULTISIGS:
        receive_addr = generate_multisig(multisig['wallet_ids'])
        out.append(receive_addr)

    print('Receive addresses:')
    for i, receive_addr in enumerate(out):
        print('{}: {}'.format(MULTISIGS[i]['name'], receive_addr))


def generate_multisig(wallet_ids):
    print('Generating multisig addresses.')

    n = len(wallet_ids)
    m = math.ceil(n / 2)

    print('Set m/n to {}/{}'.format(m, n))

    print('Creating wallets.')
    res = must_run_cliw_command('wallets')
    existing_wallets = set(json.loads(res.stdout.decode('utf-8')))

    for wallet in wallet_ids:
        if wallet in existing_wallets:
            print('Skipping existing wallet {}.'.format(wallet))
            continue

        print('Creating wallet {}.'.format(wallet))
        must_run_cliw_command('mkwallet', '--id={}'.format(wallet), '--m={}'.format(m), '--n={}'.format(n))

    print('Retrieving account keys.')
    account_keys = {}
    for wallet in wallet_ids:
        res = must_run_cliw_command('--id={}'.format(wallet), 'account', 'get', 'default')
        key = json.loads(res.stdout.decode('utf-8'))['accountKey']
        print('Got account key {} for wallet {}'.format(key, wallet))
        account_keys[wallet] = key

    print('Distributing shared keys.')
    for base_wallet in wallet_ids:
        for wallet, key in account_keys.items():
            if wallet == base_wallet:
                continue
            must_run_cliw_command('--id={}'.format(base_wallet), '--account=default', 'shared', 'add', key)
            print('Added account key {} to wallet {}.'.format(key, base_wallet))

    print('Getting receive address.')
    res = must_run_cliw_command('--id={}'.format(wallet_ids[0]), '--account=default', 'account', 'get')
    receive_address = json.loads(res.stdout.decode('utf-8'))['receiveAddress']
    return receive_address


def must_run_cliw_command(*args, should_print=True):
    return must_run(cliw_command(*args), should_print=should_print)


def cliw_command(*args):
    return [
        'hsw-cli',
        '--network=regtest',
        *args
    ]


def rpcw_command(*args):
    return [
        'hsw-rpc',
        '--network=regtest',
        *args
    ]


def must_run(args, should_print):
    cmd = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if cmd.returncode == 0:
        if should_print:
            print_handle('STDOUT', cmd.stdout)
            print_handle('STDERR', cmd.stderr)
        return cmd

    raise CommandFailedError(args, cmd.stdout, cmd.stderr)


def print_handle(name, hdl):
    handle_str = hdl.decode('utf-8')
    if len(handle_str.strip()) == 0:
        return
    for line in handle_str.split('\n'):
        print('>> [{}] {}'.format(name, line))


class CommandFailedError(Exception):
    def __init__(self, cmd_args, stdout, stderr):
        self.cmd_args = cmd_args
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return 'Command failed.\nCommand:\n{}\nStdout:\n{}\nStderr:\n{}\n'.format(' '.join(self.cmd_args),
                                                                                  self.stdout.decode('utf-8'),
                                                                                  self.stderr.decode('utf-8'))


if __name__ == '__main__':
    main()
