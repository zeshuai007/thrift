from thrift.TConfiguration import TConfiguration
from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.protocol.TJSONProtocol import TJSONProtocol
from thrift.protocol.TProtocol import TType
from thrift.protocol import TMap, TSet, TList
from thrift.transport.TSocket import TSocket, TServerSocket
from thrift.transport.TTransport import TTransportException
from thrift.transport import TTransport
from thrift.transport import TZlibTransport
import unittest
import traceback
import os
import string
import random

class TestCompactProtocolReadCheckTest(unittest.TestCase): 
    config = TConfiguration()
    config.setMaxMessageSize(20)

    def test_TMap(self):
        buf = TTransport.TMemoryBuffer()
        transport = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        protocol= TCompactProtocol.TCompactProtocol(transport)
        protocol.state = TCompactProtocol.CONTAINER_WRITE
        tmap = TMap.TMap(TType.BYTE, TType.BYTE, TType.I32)
        protocol.writeMapBegin(tmap.keyType, tmap.valueType, tmap.size)
        protocol.writeMapEnd()

        transport.flush()
        data_r = buf.getvalue()
        buf = TTransport.TMemoryBuffer(data_r)
        transport = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        protocol= TCompactProtocol.TCompactProtocol(transport)
        protocol.state = TCompactProtocol.CONTAINER_READ
        acc = protocol.readMapBegin()
        self.assertEqual(acc, (TType.BYTE, TType.BYTE, TType.I32))


    def test_TList(self):
        buf = TTransport.TMemoryBuffer()
        transport = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        protocol= TCompactProtocol.TCompactProtocol(transport)
        protocol.state = TCompactProtocol.CONTAINER_WRITE
        tmap = TList.TList(TType.BYTE, TType.I32)
        protocol.writeListBegin(tmap.elemType, tmap.size)
        protocol.writeListEnd()

        transport.flush()
        data_r = buf.getvalue()
        buf = TTransport.TMemoryBuffer(data_r)
        transport = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        protocol= TCompactProtocol.TCompactProtocol(transport)
        protocol.state = TCompactProtocol.CONTAINER_READ
        acc = protocol.readListBegin()
        self.assertEqual(acc, (TType.BYTE, TType.I32))


    def test_TSet(self):
        buf = TTransport.TMemoryBuffer()
        transport = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        protocol= TCompactProtocol.TCompactProtocol(transport)
        protocol.state = TCompactProtocol.CONTAINER_WRITE
        tmap = TSet.TSet(TType.BYTE, TType.I32)
        protocol.writeSetBegin(tmap.elemType, tmap.size)
        protocol.writeSetEnd()

        transport.flush()
        data_r = buf.getvalue()
        buf = TTransport.TMemoryBuffer(data_r)
        transport = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        protocol= TCompactProtocol.TCompactProtocol(transport)
        protocol.state = TCompactProtocol.CONTAINER_READ
        acc = protocol.readSetBegin()
        self.assertEqual(acc, (TType.BYTE, TType.I32))


if __name__ == '__main__':
    unittest.main()
