import os
from contextlib import suppress
import yaml
from pathlib import Path
from keys import Keymap
# парсить конфиг из джсона а лучше ямла все таки а не это сранье. 
class Runner:
    def __init__(self):
        self.keys = None
        self.commands = None
        self.exec = None
        self.vars = None

    def parse_conf(self):
        user_conf = Path(f'{os.path.dirname(os.getcwd())}/rc.conf')
        if user_conf.exists():
            config_path = user_conf
        else:
            config_path = '/etc/fm/rc.conf'
        with open(config_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        if config is None:
            pass
        #return_error()
        else:
            self.set_configuration(config)

    def set_configuration(self, config):
        keys = Hotkeys(config['keys'])
        self.commands = command['commands']
        self.exec = config['exec']
        self.vars = config['set']
            

    def run(self):
        print("run succeful")

    def destroy(self):
        pass

class Bar:
    '''
    I need to have time and date
    owner mod (rwx) free storage
    directory who i am tabs(additional) 

    '''
    def __init__(self):
        pass

    def print_bar(self):
        pass

    def print_footer(self):
        pass

    def destroy(self):
        pass

    def update_info(self):
        pass

'''
    def hotkeys_map(self, line):
        line.split()
        return line[0], line[1:]

    def hotkeys_upload(self):
        with open(self.config, 'r') as config:
            identifiers, hotkeys = list(map(self.hotkeys_map, config))
        return identifiers, hotkeys

    def hotkeys_parse(self):
        identifiers, hotkeys = self.hotkeys_upload()
        for identifier in identifiers:
            print(identifier)
        
'''