import subprocess

hosts = [
    'iperf.he.net',
    'bouygues.testdebit.info',
    'iperf.comneonext.de',
    'ikoula.testdebit.info',
    'st2.nn.ertelecom.ru',
    'iperf.biznetnetworks.com',
    'iperf.scottlinux.com',
    'speedtest.serverius.net'
    'iperf.it-north.net',
    'speedtest.wtnet.de',
    'iperf.volia.net',
    'erf.eenet.ee',
    'ping.online.net'
]

timeout = 2000
max_hop = 50

def run_process(executable_name, cmd_list):
    p = subprocess.Popen([executable_name] + cmd_list,
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    with open('ouput.txt', 'a') as fh:
        while True:
            line = p.stdout.readline()
            if not line: break
            fh.write(line)
            print '-->',line
            p.wait()
        fh.write('\n\n')

def run_for_all_hosts(executable_name, cmd_list=[]):
    # clear the log file
    with open('ouput.txt', 'w') as fh:
        fh.write('')

    # run process for all hosts
    for host in hosts:
        run_process(executable_name, cmd_list + [host])

if __name__ == '__main__':
    run_for_all_hosts("tracert",
        ['-d', '-w', str(timeout), '-h', str(max_hop)])
    run_for_all_hosts("ping")
    # run_for_all_hosts("iperf3", ['-c'])