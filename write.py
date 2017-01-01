contract_addr = u'0x7b8a599170744584cec7c5b4ae16c3cc62e939a3'
from ethjsonrpc import EthJsonRpc
c = EthJsonRpc('127.0.0.1', 8545)
msg = ['re']
# tx = c.call_with_transaction(c.eth_coinbase(), contract_addr, 'set_s(string)', msg)

to = 0xe39ca93937cce815c2b152578e6025a8f8c60798

tx = c.call_with_transaction(c.eth_coinbase(), contract_addr, 'setCoinTo(address,uint)', [to,5])
