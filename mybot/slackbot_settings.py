import os
import yaml

abs_path = os.path.dirname(os.path.abspath(__file__))
settings_path = os.path.normpath(os.path.join(abs_path, '../settings.yml'))
settings_file = open(settings_path, "r")
settings = yaml.load(settings_file)

API_TOKEN = settings['API_TOKEN']
DEFAULT_REPLY = "Sorry I didn't get you"
PLUGINS = ['plugins']
