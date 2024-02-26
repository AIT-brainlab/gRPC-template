from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestMessage(_message.Message):
    __slots__ = ("id", "sentFrom", "message")
    ID_FIELD_NUMBER: _ClassVar[int]
    SENTFROM_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    sentFrom: str
    message: str
    def __init__(self, id: _Optional[int] = ..., sentFrom: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ReplyMessage(_message.Message):
    __slots__ = ("id", "sentFrom", "message", "requestMessage")
    ID_FIELD_NUMBER: _ClassVar[int]
    SENTFROM_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    sentFrom: str
    message: str
    requestMessage: RequestMessage
    def __init__(self, id: _Optional[int] = ..., sentFrom: _Optional[str] = ..., message: _Optional[str] = ..., requestMessage: _Optional[_Union[RequestMessage, _Mapping]] = ...) -> None: ...
