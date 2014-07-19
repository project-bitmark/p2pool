from p2pool.bitcoin import networks

PARENT = networks.nets['bitmark']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '62746d7032704944'.decode('hex') #btmp2pID converted to HEX
PREFIX = '62746d7032705058'.decode('hex') # btmp2pPX converted to HEX
P2P_PORT = 9267
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9268
BOOTSTRAP_ADDRS = '174.36.9.130'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-btm'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Bitmark to >=0.9.2.1!' if v < 90201 else None
