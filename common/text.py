# encoding:utf8
from common import config
cfg = config.get_config('../lib/conf.properties')
print(cfg['mailtxt'])