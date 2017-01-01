from ethjsonrpc import EthJsonRpc
c = EthJsonRpc('127.0.0.1', 8545)
print c.net_version()