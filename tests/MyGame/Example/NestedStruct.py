# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class NestedStruct(object):
    __slots__ = ['_tab']

    # NestedStruct
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NestedStruct
    def A(self): return [self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0 + i * 4)) for i in range(2)]
    # NestedStruct
    def ALength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(0))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NestedStruct
    def AIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(0))
        return o == 0

    # NestedStruct
    def B(self): return self._tab.Get(flatbuffers.number_types.Int8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # NestedStruct
    def C(self): return [self._tab.Get(flatbuffers.number_types.Int8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(9 + i * 1)) for i in range(2)]
    # NestedStruct
    def CLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(9))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NestedStruct
    def CIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(9))
        return o == 0

    # NestedStruct
    def D(self): return [self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16 + i * 8)) for i in range(2)]
    # NestedStruct
    def DLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NestedStruct
    def DIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


def CreateNestedStruct(builder, a, b, c, d):
    builder.Prep(8, 32)
    for _idx0 in range(2 , 0, -1):
        builder.PrependInt64(d[_idx0-1])
    builder.Pad(5)
    for _idx0 in range(2 , 0, -1):
        builder.PrependInt8(c[_idx0-1])
    builder.PrependInt8(b)
    for _idx0 in range(2 , 0, -1):
        builder.PrependInt32(a[_idx0-1])
    return builder.Offset()

try:
    from typing import List
except:
    pass

class NestedStructT(object):

    # NestedStructT
    def __init__(self):
        self.a = None  # type: List[int]
        self.b = 0  # type: int
        self.c = None  # type: List[int]
        self.d = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        nestedStruct = NestedStruct()
        nestedStruct.Init(buf, pos)
        return cls.InitFromObj(nestedStruct)

    @classmethod
    def InitFromObj(cls, nestedStruct):
        x = NestedStructT()
        x._UnPack(nestedStruct)
        return x

    # NestedStructT
    def _UnPack(self, nestedStruct):
        if nestedStruct is None:
            return
        if not nestedStruct.AIsNone():
            if np is None:
                self.a = []
                for i in range(nestedStruct.ALength()):
                    self.a.append(nestedStruct.A(i))
            else:
                self.a = nestedStruct.AAsNumpy()
        self.b = nestedStruct.B()
        if not nestedStruct.CIsNone():
            if np is None:
                self.c = []
                for i in range(nestedStruct.CLength()):
                    self.c.append(nestedStruct.C(i))
            else:
                self.c = nestedStruct.CAsNumpy()
        if not nestedStruct.DIsNone():
            if np is None:
                self.d = []
                for i in range(nestedStruct.DLength()):
                    self.d.append(nestedStruct.D(i))
            else:
                self.d = nestedStruct.DAsNumpy()

    # NestedStructT
    def Pack(self, builder):
        return CreateNestedStruct(builder, self.a, self.b, self.c, self.d)
