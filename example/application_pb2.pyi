# ############################################################################# #
#  Automatically generated protobuf stub files for python                       #
#   by protoc-gen-python_typings plugin for protoc                              #
# ############################################################################# #

from google.api.annotations_pb2 import *
from google.protobuf import *
from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.empty_pb2 import *
from google.protobuf.internal.well_known_types import Timestamp
from google.protobuf.message import Message
from typing import List

A: int = 0
B: int = 1
C: int = 3


class SimpleMessage(Message):
    class InnerMessage(Message):
        A: int = 0
        B: int = 1
        C: int = 3

        def __init__(self,
                     id: int = None,
                     startFrom: Timestamp = None,
                     enumField: int = None):
            """
            :param id: Documentation 4 0 3 0 2 0
            :param startFrom: Documentation 4 0 3 0 2 1
            """
            self.id = id
            self.startFrom = startFrom
            self.enumField = enumField

        # region <<<Message Implementation>>>
        def __eq__(self, other_msg: 'SimpleMessage.InnerMessage') -> bool: ...
        def __str__(self) -> str: ...
        def __unicode__(self) -> str: ...
        def MergeFrom(self, other_msg: 'SimpleMessage.InnerMessage'): ...
        def Clear(self): ...
        def SetInParent(self): ...
        def IsInitialized(self) -> bool: ...
        def MergeFromString(self, serialized: str): ...
        def SerializeToString(self, **kwargs) -> str: ...
        def SerializePartialToString(self, **kwargs) -> str: ...
        def ListFields(self) -> List[FieldDescriptor]: ...
        def HasField(self, field_name: str) -> bool: ...
        def ClearField(self, field_name: str): ...
        def WhichOneof(self, oneof_group: str): ...
        def HasExtension(self, extension_handle: str) -> bool: ...
        def ClearExtension(self, extension_handle): ...
        def DiscardUnknownFields(self): ...
        def ByteSize(self) -> int: ...
        def _SetListener(self, message_listener): ...

        # endregion <<<Message Implementation>>>
        ...

    class InnerMessage1(Message):
        A: int = 0
        B: int = 1
        C: int = 3

        def __init__(self,
                     id: int = None,
                     startFrom: Timestamp = None,
                     enumField: int = None):
            self.id = id
            self.startFrom = startFrom
            self.enumField = enumField

        # region <<<Message Implementation>>>
        def __eq__(self, other_msg: 'SimpleMessage.InnerMessage1') -> bool: ...
        def __str__(self) -> str: ...
        def __unicode__(self) -> str: ...
        def MergeFrom(self, other_msg: 'SimpleMessage.InnerMessage1'): ...
        def Clear(self): ...
        def SetInParent(self): ...
        def IsInitialized(self) -> bool: ...
        def MergeFromString(self, serialized: str): ...
        def SerializeToString(self, **kwargs) -> str: ...
        def SerializePartialToString(self, **kwargs) -> str: ...
        def ListFields(self) -> List[FieldDescriptor]: ...
        def HasField(self, field_name: str) -> bool: ...
        def ClearField(self, field_name: str): ...
        def WhichOneof(self, oneof_group: str): ...
        def HasExtension(self, extension_handle: str) -> bool: ...
        def ClearExtension(self, extension_handle): ...
        def DiscardUnknownFields(self): ...
        def ByteSize(self) -> int: ...
        def _SetListener(self, message_listener): ...

        # endregion <<<Message Implementation>>>
        ...

    class InnerMessage2(Message):
        A: int = 0
        B: int = 1
        C: int = 3

        def __init__(self,
                     id: int = None,
                     startFrom: Timestamp = None,
                     enumField: int = None):
            self.id = id
            self.startFrom = startFrom
            self.enumField = enumField

        # region <<<Message Implementation>>>
        def __eq__(self, other_msg: 'SimpleMessage.InnerMessage2') -> bool: ...
        def __str__(self) -> str: ...
        def __unicode__(self) -> str: ...
        def MergeFrom(self, other_msg: 'SimpleMessage.InnerMessage2'): ...
        def Clear(self): ...
        def SetInParent(self): ...
        def IsInitialized(self) -> bool: ...
        def MergeFromString(self, serialized: str): ...
        def SerializeToString(self, **kwargs) -> str: ...
        def SerializePartialToString(self, **kwargs) -> str: ...
        def ListFields(self) -> List[FieldDescriptor]: ...
        def HasField(self, field_name: str) -> bool: ...
        def ClearField(self, field_name: str): ...
        def WhichOneof(self, oneof_group: str): ...
        def HasExtension(self, extension_handle: str) -> bool: ...
        def ClearExtension(self, extension_handle): ...
        def DiscardUnknownFields(self): ...
        def ByteSize(self) -> int: ...
        def _SetListener(self, message_listener): ...

        # endregion <<<Message Implementation>>>
        ...

    class InnerMessage3(Message):
        A: int = 0
        B: int = 1
        C: int = 3

        def __init__(self,
                     id: int = None,
                     startFrom: Timestamp = None,
                     enumField: int = None):
            self.id = id
            self.startFrom = startFrom
            self.enumField = enumField

        # region <<<Message Implementation>>>
        def __eq__(self, other_msg: 'SimpleMessage.InnerMessage3') -> bool: ...
        def __str__(self) -> str: ...
        def __unicode__(self) -> str: ...
        def MergeFrom(self, other_msg: 'SimpleMessage.InnerMessage3'): ...
        def Clear(self): ...
        def SetInParent(self): ...
        def IsInitialized(self) -> bool: ...
        def MergeFromString(self, serialized: str): ...
        def SerializeToString(self, **kwargs) -> str: ...
        def SerializePartialToString(self, **kwargs) -> str: ...
        def ListFields(self) -> List[FieldDescriptor]: ...
        def HasField(self, field_name: str) -> bool: ...
        def ClearField(self, field_name: str): ...
        def WhichOneof(self, oneof_group: str): ...
        def HasExtension(self, extension_handle: str) -> bool: ...
        def ClearExtension(self, extension_handle): ...
        def DiscardUnknownFields(self): ...
        def ByteSize(self) -> int: ...
        def _SetListener(self, message_listener): ...

        # endregion <<<Message Implementation>>>
        ...

    def __init__(self,
                 id: int = None,
                 startFrom: Timestamp = None,
                 until: Timestamp = None,
                 enumField: List[int] = None,
                 messageField: List[InnerMessage] = None,
                 messageField1: List[InnerMessage1] = None):
        """
        :param startFrom: Documentation 4 0 2 1
        :param until: Documentation 4 0 2 2
        """
        self.id = id
        self.startFrom = startFrom
        self.until = until
        self.enumField = enumField
        self.messageField = messageField
        self.messageField1 = messageField1

    # region <<<Message Implementation>>>
    def __eq__(self, other_msg: 'SimpleMessage') -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: 'SimpleMessage'): ...
    def Clear(self): ...
    def SetInParent(self): ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: str): ...
    def SerializeToString(self, **kwargs) -> str: ...
    def SerializePartialToString(self, **kwargs) -> str: ...
    def ListFields(self) -> List[FieldDescriptor]: ...
    def HasField(self, field_name: str) -> bool: ...
    def ClearField(self, field_name: str): ...
    def WhichOneof(self, oneof_group: str): ...
    def HasExtension(self, extension_handle: str) -> bool: ...
    def ClearExtension(self, extension_handle): ...
    def DiscardUnknownFields(self): ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener): ...

    # endregion <<<Message Implementation>>>
    ...


