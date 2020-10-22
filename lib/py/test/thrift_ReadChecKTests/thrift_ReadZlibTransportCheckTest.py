from thrift.transport import TZlibTransport, TTransport
from thrift.TConfiguration import TConfiguration
import unittest

class TestTZlibTransportReadCheck(unittest.TestCase):
    data = '{"1":[1,"hello"], "a":{"A":"abc"}, "bool":true, "num":12345}'
    config = TConfiguration()
    config.setMaxMessageSize(200)
    def test_zlibtransport_readcheck(self):
        buf = TTransport.TMemoryBuffer()
        trans = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        zlib_trans =TZlibTransport.TZlibTransport(trans, self.config)
        zlib_trans.write(self.data.encode('utf-8'))
        zlib_trans.flush()
        value = buf.getvalue()
        zlib_trans.close()

        buf = TTransport.TMemoryBuffer(value)
        trans = TTransport.TBufferedTransportFactory().getTransport(buf, self.config)
        zlib_trans = TZlibTransport.TZlibTransport(trans, self.config)
        acc = zlib_trans.read(len(self.data)).decode('utf-8')
        zlib_trans.close()
        self.assertEqual(self.data, acc)

if __name__ =='__main__':
    unittest.main()

