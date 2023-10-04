# https://martinheinz.dev/blog/98

# pip install sh
import sh

print(sh.ls("-la"))

ls_cmd = sh.Command("ls")
print(ls_cmd("-la"))

# custom_cmd = sh.Command("/path/to/my/cmd")
# custom_cmd("some", "args")

with sh.contrib.sudo:
    ls_cmd = sh.Command("cat")

    print(ls_cmd("/var/log/system.log"))

print(sh.awk("{print $9}", _in=sh.ls("-la")))
print(sh.wc("-l", _in=sh.ls("-l")))

try:
    sh.cat("/tmp/doesnt/exist")
except sh.ErrorReturnCode as e:
    print(f"Command {e.full_cmd} exited with {e.exit_code}")

curl = sh.curl("https://httpbin.org/delay/5", _bg=True)
try:
    curl.wait(timeout=3)
except sh.TimeoutException:
    print("Command timed out...")
    curl.kill()

import logging

logging.basicConfig(level=logging.INFO)
sh.ls("-la")

logging.getLogger("sh").setLevel(logging.DEBUG)
sh.ls("-la")

# output any command to a file
sh.ls("-la", _out="/tmp/ipaddr")
