import cmd
import sys
import urllib.request
from conf import Conf

print(Conf.log["Banner"])
class MahFramework2(cmd.Cmd):

    intro = Conf.log["Intro"]
    prompt = Conf.log["Prompt"]
    Version = Conf.log["Version"]

    def do_banner(self, line):
        banner = Conf.log["Banner"]
        print(banner)
    def do_hello(self, line):
        print("Hello world!")

    def do_quit(self, line):
        sys.exit(1)

    def do_EOF(self, line):
        return True

    def do_cfic(self,line):
        "checking for internet connection"
        print("[i]: Checking for internet connection...\n")
        def connect():
            try:
               urllib.request.urlopen('http://google.com') 
               return True
            except:
                return False
        print( '[+]: connected' if connect() else '[!]: no internet!' )

    def do_exit(self, line):
        sys.exit(1)


MahFramework2().cmdloop()

