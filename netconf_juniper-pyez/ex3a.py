from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2
from getpass import getpass

device = Device(**srx2)
device.open()
device.timeout = 60

cfg = Config(device)
cfg.lock()


cfg.load("set system host-name python4life", format="set", merge=True)
print(cfg.diff())
cfg.rollback(0)
print(cfg.diff())
# cfg.load(path="test_config.conf", format="text", merge=True)
# cfg.load(path="test_replace.conf", format="text", merge=False)
# cfg.commit()
# cfg.commit(comment="Testing from pyez")
# cfg.unlock()
