import multiprocessing
import socket
import re

def handle(connection, address):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        ethernet = """# The primary network interface
iface enp3s0f0 inet static
    address oneninetwo.onesixeight.eighteight.twotwofive
    netmask 255.255.255.0
    network 192.168.88.0
    broadcast 192.168.88.255
    gateway 192.168.88.1
    dns-nameservers 8.8.8.8"""
        files = {
            "root": {
                "test": "test"
            },
            "etc": {
                "network": {"interfaces": ethernet},
                "app": {"google.gz": "text", "chrome.gz": "text"},
                "systemd": {"bootchart.conf": "text", "journald.conf": "text", "resolved.conf": "text"},
                "security": "System security :)",
                "perl": {"Net": "text", "CPAN": "text"}
            },
            "bin": {
                "bash": "eee Bash :)",
                "bzcat": "You can use cat :) cat --help",
                "bzsed": "You can use sed :) sed --help",
                "bzls": "You can use ls :) ls --help",
                "bzgrep": "You can use grep :) grep --help"
            },
            "boot": {
                "grub": "text",
                "abi-4.4.0-142-generic": "text",
                "config-4.4.0-142-generic": "text",
                "retpoline-4.4.0-142-generic": "text",
            },
            "dev": {
                "tty": "text",
                "tty1": "text",
                "tty2": "text",
                "tty3": "text",
                "tty4": "text",
                "tty5": "text",
                "tty6": "text",
                "tty7": "text",
                "tty8": "text",
                "tty9": "text",
                "tty10": "text",
                "tty11": "text",
                "tty12": "text",
            },
            "home": {
                "helper": {
                    "mycop": "MYCOP",
                    "mycop2": "MYCOP",
                    "flag": "Make a request: wget https://nzkoff.ru/may/be/find/flag.txt flag",
                    "noflag": "NO FLAG!"
                }
            },
            "opt": {
                "google": "google :)",
                "chrome": "chrome :)",
                "explorer": "brrr"
            },
            "var": {
                "backups": {
                    "dpkg.status.1.gz": "text",
                    "dpkg.status.2.gz": "text",
                    "dpkg.status.3.gz": "text",
                    "dpkg.status.4.gz": "text",
                    "dpkg.status.5.gz": "text",
                    "dpkg.status.6.gz": "text",
                    "dpkg.status.7.gz": "text",
                    "dpkg.status.8.gz": "text",
                    "dpkg.status.9.gz": "text",
                },
                "cache": {
                    "dpkg.status.1.gz": "text",
                    "dpkg.status.2.gz": "text",
                    "dpkg.status.3.gz": "text",
                    "dpkg.status.4.gz": "text",
                    "dpkg.status.5.gz": "text",
                    "dpkg.status.6.gz": "text",
                    "dpkg.status.7.gz": "text",
                    "dpkg.status.8.gz": "text",
                    "dpkg.status.9.gz": "text",
                },
                "data": {
                    "dpkg.status.1.gz": "text",
                    "dpkg.status.2.gz": "text",
                    "dpkg.status.3.gz": "text",
                    "dpkg.status.4.gz": "text",
                    "dpkg.status.5.gz": "text",
                    "dpkg.status.6.gz": "text",
                    "dpkg.status.7.gz": "text",
                    "dpkg.status.8.gz": "text",
                    "dpkg.status.9.gz": "text",
                },
                "lib": {
                    "dpkg.status.1.gz": "text",
                    "dpkg.status.2.gz": "text",
                    "dpkg.status.3.gz": "text",
                    "dpkg.status.4.gz": "text",
                    "dpkg.status.5.gz": "text",
                    "dpkg.status.6.gz": "text",
                    "dpkg.status.7.gz": "text",
                    "dpkg.status.8.gz": "text",
                    "dpkg.status.9.gz": "text",
                },
                "local": {
                    "dpkg.status.1.gz": "text",
                    "dpkg.status.2.gz": "text",
                    "dpkg.status.3.gz": "text",
                    "dpkg.status.4.gz": "text",
                    "dpkg.status.5.gz": "text",
                    "dpkg.status.6.gz": "text",
                    "dpkg.status.7.gz": "text",
                    "dpkg.status.8.gz": "text",
                    "dpkg.status.9.gz": "text",
                }
            }
        }
        logger.debug("Connected %r at %r", connection, address)
        connection.send("Bubuntu22.03 activited.\nroot@root:~$ ".encode())
        while True:
            data = connection.recv(1024).decode()
            sed = re.findall(r'sed \'s/.{0,50}/.{0,50}/g\'\n', data)
            cat = re.findall(r'cat .{,100}\n', data)
            ls = re.findall(r'ls .{,100}\n', data)
            if 'sed\n' in data:
                connection.send("Usage: sed --help\n".encode())
            elif 'sed --help' in data:
                connection.send("Usage sed 's/text/mytext/g'\nAnd you will replace the text with mytext in all files\n".encode())
            elif sed != []:
                answer = sed[0].split("/")
                answer[1] = ("'").join(answer[1].split("\""))
                answer[2] = ("'").join(answer[2].split("\""))
                for key in files.keys():
                    if isinstance(files[key], (dict, list)):
                        for ke in files[key]:
                            if isinstance(files[key][ke], (dict, list)):
                                for k in files[key][ke]:
                                    files[key][ke][k] = (answer[2]).join(files[key][ke][k].split(answer[1]))
                            else:
                                files[key][ke] = (answer[2]).join(files[key][ke].split(answer[1]))
                    else:
                        files[key] = (answer[2]).join(files[key].split(answer[1]))
            elif 'cat\n' in data:
                connection.send("Usage: cat --help\n".encode())
            elif 'cat --help' in data:
                connection.send("Usage cat filename\nAnd you will see the contents of the file\n".encode())
            elif cat != []:
                try:
                    answer = cat[0].split("cat /")[1].split("\n")[0].split("/")
                    if len(answer) == 1:
                        connection.send("{}\n".format(files[answer[0]]).encode())
                    if len(answer) == 2:
                        connection.send("{}\n".format(files[answer[0]][answer[1]]).encode())
                    if len(answer) == 3:
                        connection.send("{}\n".format(files[answer[0]][answer[1]][answer[2]]).encode())
                    if len(answer) == 4:
                        connection.send("{}\n".format(files[answer[0]][answer[1]][answer[2]][answer[3]]).encode())
                except:
                    connection.send("File not found\n".encode())
            elif 'ls\n' in data:
                connection.send("Usage: ls --help\n".encode())
            elif "ls --help\n" in data:
                connection.send("Usage ls namedir\nAnd you will see the contents of the directory\n".encode())
            elif ls != []:
                try:
                    answer = ls[0].split("ls /")[1].split("\n")[0].split("/")
                    if answer == ['']:
                        connection.send("{}\n".format(("\n").join(files.keys())).encode())
                    if len(answer) == 1:
                        connection.send("{}\n".format(("\n").join(files[answer[0]].keys())).encode())
                    if len(answer) == 2:
                        connection.send("{}\n".format(("\n").join(files[answer[0]][answer[1]].keys())).encode())
                    if len(answer) == 3:
                        connection.send("{}\n".format(("\n").join(files[answer[0]][answer[1]][answer[2]].keys())).encode())
                    if len(answer) == 4:
                        connection.send("{}\n".format(("\n").join(files[answer[0]][answer[1]][answer[2]][answer[3]].keys())).encode())
                except:
                    connection.send("Directory not found\n".encode())
            elif "wget https://nzkoff.ru/may/be/find/flag.txt flag" in data:
                if "address 192.168.88.225" in files["etc"]["network"]["interfaces"]:
                    files["root"]["flag"] = "ELON{FlagByNzK0ffAdmin_21xaw}"
                else:
                    connection.send("Can't establish a connection\n".encode())
            else:
                connection.send("Command not found\n".encode())
            connection.send("root@root:~$ ".encode())
    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.debug("Got connection")
            process = multiprocessing.Process(target=handle, args=(conn, address))
            process.daemon = True
            process.start()
            self.logger.debug("Started process %r", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9001)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in multiprocessing.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")