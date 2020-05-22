"""jc - JSON CLI output utility netstat Parser

Usage:

    Specify --netstat as the first argument if the piped input is coming from netstat

Caveats:

    - Use of multiple 'l' options is not supported on OSX (e.g. 'netstat -rlll')
    - Use of the 'A' option is not supported on OSX when using the 'r' option (e.g. netstat -rA)

Compatibility:

    'linux', 'darwin'

Examples:

    $ sudo netstat -apee | jc --netstat -p
    [
      {
        "proto": "tcp",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "localhost",
        "foreign_address": "0.0.0.0",
        "state": "LISTEN",
        "user": "systemd-resolve",
        "inode": 26958,
        "program_name": "systemd-resolve",
        "kind": "network",
        "pid": 887,
        "local_port": "domain",
        "foreign_port": "*",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "tcp",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "0.0.0.0",
        "foreign_address": "0.0.0.0",
        "state": "LISTEN",
        "user": "root",
        "inode": 30499,
        "program_name": "sshd",
        "kind": "network",
        "pid": 1186,
        "local_port": "ssh",
        "foreign_port": "*",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "tcp",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "localhost",
        "foreign_address": "localhost",
        "state": "ESTABLISHED",
        "user": "root",
        "inode": 46829,
        "program_name": "sshd: root",
        "kind": "network",
        "pid": 2242,
        "local_port": "ssh",
        "foreign_port": "52186",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4",
        "foreign_port_num": 52186
      },
      {
        "proto": "tcp",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "localhost",
        "foreign_address": "localhost",
        "state": "ESTABLISHED",
        "user": "root",
        "inode": 46828,
        "program_name": "ssh",
        "kind": "network",
        "pid": 2241,
        "local_port": "52186",
        "foreign_port": "ssh",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4",
        "local_port_num": 52186
      },
      {
        "proto": "tcp6",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "[::]",
        "foreign_address": "[::]",
        "state": "LISTEN",
        "user": "root",
        "inode": 30510,
        "program_name": "sshd",
        "kind": "network",
        "pid": 1186,
        "local_port": "ssh",
        "foreign_port": "*",
        "transport_protocol": "tcp",
        "network_protocol": "ipv6"
      },
      {
        "proto": "udp",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "localhost",
        "foreign_address": "0.0.0.0",
        "state": null,
        "user": "systemd-resolve",
        "inode": 26957,
        "program_name": "systemd-resolve",
        "kind": "network",
        "pid": 887,
        "local_port": "domain",
        "foreign_port": "*",
        "transport_protocol": "udp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "raw6",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "[::]",
        "foreign_address": "[::]",
        "state": "7",
        "user": "systemd-network",
        "inode": 27001,
        "program_name": "systemd-network",
        "kind": "network",
        "pid": 867,
        "local_port": "ipv6-icmp",
        "foreign_port": "*",
        "transport_protocol": null,
        "network_protocol": "ipv6"
      },
      {
        "proto": "unix",
        "refcnt": 2,
        "flags": null,
        "type": "DGRAM",
        "state": null,
        "inode": 33322,
        "program_name": "systemd",
        "path": "/run/user/1000/systemd/notify",
        "kind": "socket",
        "pid": 1607
      },
      {
        "proto": "unix",
        "refcnt": 2,
        "flags": "ACC",
        "type": "SEQPACKET",
        "state": "LISTENING",
        "inode": 20835,
        "program_name": "init",
        "path": "/run/udev/control",
        "kind": "socket",
        "pid": 1
      },
      ...
    ]

    $ sudo netstat -apee | jc --netstat -p -r
    [
      {
        "proto": "tcp",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "localhost",
        "foreign_address": "0.0.0.0",
        "state": "LISTEN",
        "user": "systemd-resolve",
        "inode": "26958",
        "program_name": "systemd-resolve",
        "kind": "network",
        "pid": "887",
        "local_port": "domain",
        "foreign_port": "*",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "tcp",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "0.0.0.0",
        "foreign_address": "0.0.0.0",
        "state": "LISTEN",
        "user": "root",
        "inode": "30499",
        "program_name": "sshd",
        "kind": "network",
        "pid": "1186",
        "local_port": "ssh",
        "foreign_port": "*",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "tcp",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "localhost",
        "foreign_address": "localhost",
        "state": "ESTABLISHED",
        "user": "root",
        "inode": "46829",
        "program_name": "sshd: root",
        "kind": "network",
        "pid": "2242",
        "local_port": "ssh",
        "foreign_port": "52186",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "tcp",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "localhost",
        "foreign_address": "localhost",
        "state": "ESTABLISHED",
        "user": "root",
        "inode": "46828",
        "program_name": "ssh",
        "kind": "network",
        "pid": "2241",
        "local_port": "52186",
        "foreign_port": "ssh",
        "transport_protocol": "tcp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "tcp6",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "[::]",
        "foreign_address": "[::]",
        "state": "LISTEN",
        "user": "root",
        "inode": "30510",
        "program_name": "sshd",
        "kind": "network",
        "pid": "1186",
        "local_port": "ssh",
        "foreign_port": "*",
        "transport_protocol": "tcp",
        "network_protocol": "ipv6"
      },
      {
        "proto": "udp",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "localhost",
        "foreign_address": "0.0.0.0",
        "state": null,
        "user": "systemd-resolve",
        "inode": "26957",
        "program_name": "systemd-resolve",
        "kind": "network",
        "pid": "887",
        "local_port": "domain",
        "foreign_port": "*",
        "transport_protocol": "udp",
        "network_protocol": "ipv4"
      },
      {
        "proto": "raw6",
        "recv_q": "0",
        "send_q": "0",
        "local_address": "[::]",
        "foreign_address": "[::]",
        "state": "7",
        "user": "systemd-network",
        "inode": "27001",
        "program_name": "systemd-network",
        "kind": "network",
        "pid": "867",
        "local_port": "ipv6-icmp",
        "foreign_port": "*",
        "transport_protocol": null,
        "network_protocol": "ipv6"
      },
      {
        "proto": "unix",
        "refcnt": "2",
        "flags": null,
        "type": "DGRAM",
        "state": null,
        "inode": "33322",
        "program_name": "systemd",
        "path": "/run/user/1000/systemd/notify",
        "kind": "socket",
        "pid": " 1607"
      },
      {
        "proto": "unix",
        "refcnt": "2",
        "flags": "ACC",
        "type": "SEQPACKET",
        "state": "LISTENING",
        "inode": "20835",
        "program_name": "init",
        "path": "/run/udev/control",
        "kind": "socket",
        "pid": " 1"
      },
      ...
    ]
"""


class info():
    version = '1.5'
    description = 'netstat command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'

    # compatible options: linux, darwin, cygwin, win32, aix, freebsd
    compatible = ['linux', 'darwin']
    magic_commands = ['netstat']


__version__ = info.version


def process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (dictionary) raw structured data to process

    Returns:

        List of dictionaries. Structured data with the following schema:

        [
          {
            "proto":             string,
            "recv_q":            integer,
            "send_q":            integer,
            "transport_protocol" string,
            "network_protocol":  string,
            "local_address":     string,
            "local_port":        string,
            "local_port_num":    integer,
            "foreign_address":   string,
            "foreign_port":      string,
            "foreign_port_num":  integer,
            "state":             string,
            "program_name":      string,
            "pid":               integer,
            "user":              string,
            "security_context":  string,
            "refcnt":            integer,
            "flags":             string,
            "type":              string,
            "inode":             integer,
            "path":              string,
            "kind":              string,
            "address":           string,
            "osx_inode":         string,
            "conn":              string,
            "refs":              string,
            "nextref":           string,
            "name":              string,
            "unit":              integer,
            "vendor":            integer,
            "class":             integer,
            "subcla":            integer,
            "osx_flags":         integer,
            "pcbcount":          integer,
            "rcvbuf":            integer,
            "sndbuf":            integer,
            "rxbytes":           integer,
            "txbytes":           integer,


            "destination":       string,
            "gateway":           string,
            "route_flags":       string,
            "route_refs":        integer,
            "use":               integer,
            "mtu":               integer,
            "netif":             string,
            "expire":            string
          }
        ]
    """
    for entry in proc_data:
        # integer changes
        int_list = ['recv_q', 'send_q', 'pid', 'refcnt', 'inode', 'unit', 'vendor', 'class',
                    'osx_flags', 'subcla', 'pcbcount', 'rcvbuf', 'sndbuf', 'rxbytes', 'txbytes',
                    'route_refs', 'use', 'mtu']
        for key in int_list:
            if key in entry:
                try:
                    key_int = int(entry[key])
                    entry[key] = key_int
                except (ValueError):
                    entry[key] = None

        if 'local_port' in entry:
            try:
                entry['local_port_num'] = int(entry['local_port'])
            except (ValueError):
                pass

        if 'foreign_port' in entry:
            try:
                entry['foreign_port_num'] = int(entry['foreign_port'])
            except (ValueError):
                pass

    return proc_data


def parse(data, raw=False, quiet=False):
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) output preprocessed JSON if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        List of dictionaries. Raw or processed structured data.
    """
    import jc.utils
    if not quiet:
        jc.utils.compatibility(__name__, info.compatible)

    cleandata = data.splitlines()
    cleandata = list(filter(None, cleandata))
    raw_output = []

    # check for OSX vs Linux
    # is this from OSX?
    if cleandata[0] == 'Active Internet connections' \
       or cleandata[0] == 'Active Internet connections (including servers)' \
       or cleandata[0] == 'Active Multipath Internet connections' \
       or cleandata[0] == 'Active LOCAL (UNIX) domain sockets' \
       or cleandata[0] == 'Registered kernel control modules' \
       or cleandata[0] == 'Active kernel event sockets' \
       or cleandata[0] == 'Active kernel control sockets' \
       or cleandata[0] == 'Routing tables':
        import jc.parsers.netstat_osx
        raw_output = jc.parsers.netstat_osx.parse(cleandata)

    # use linux parser
    else:
        import jc.parsers.netstat_linux
        raw_output = jc.parsers.netstat_linux.parse(cleandata)

    if raw:
        return raw_output
    else:
        return process(raw_output)
