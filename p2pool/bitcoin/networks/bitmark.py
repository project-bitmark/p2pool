import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 9265
ADDRESS_VERSION = 85
RPC_PORT = 9266
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitmarkaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: (10*100000000>>((height+1)/788000))+(10*100000000>>(((height+1)+788000)/788000))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 120 # s
SYMBOL = 'BTM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitmark') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitmark/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitmark'), 'bitmark.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://cryptexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://cryptexplorer.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://cryptexplorer.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
