#! ./python

def assert_raises(func, exception, in_msg=None):
    try:
        func()
    except Exception as e:
        if in_msg:
            assert in_msg in str(e)
        assert type(e) == exception

a = b'ab'
b = b'ba'
c = b'c'

assert a ^ b == b'\x03\x03'
assert_raises(lambda: b ^ c, ValueError, in_msg="Bytes")
assert_raises(lambda: a ^ 'xyz', TypeError, in_msg="can't \"^\"")

assert a & b == b'``'
assert_raises(lambda: b & c, ValueError, in_msg="Bytes")
assert_raises(lambda: a & 'xyz', TypeError, in_msg="can't \"&\"")

assert a | b == b'cc'
assert_raises(lambda: b | c, ValueError, in_msg="Bytes")
assert_raises(lambda: a | 'xyz', TypeError, in_msg="can't \"|\"")

assert bytearray(a) ^ bytearray(b) == bytearray(b'\x03\x03')
assert_raises(lambda: bytearray(b) ^ bytearray(c), ValueError, in_msg="ByteArrays")
assert_raises(lambda: bytearray(a) ^ 'xyz', TypeError, in_msg="can't \"^\"")

assert bytearray(a) & bytearray(b) == bytearray(b'``')
assert_raises(lambda: bytearray(b) & bytearray(c), ValueError, in_msg="ByteArrays")
assert_raises(lambda: bytearray(a) & 'xyz', TypeError, in_msg="can't \"&\"")

assert bytearray(a) | bytearray(b) == bytearray(b'cc')
assert_raises(lambda: bytearray(b) | bytearray(c), ValueError, in_msg="ByteArrays")
assert_raises(lambda: bytearray(a) | 'xyz', TypeError, in_msg="can't \"|\"")
