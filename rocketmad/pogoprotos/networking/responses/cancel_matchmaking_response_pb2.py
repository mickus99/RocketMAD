# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/cancel_matchmaking_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/cancel_matchmaking_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nApogoprotos/networking/responses/cancel_matchmaking_response.proto\x12\x1fpogoprotos.networking.responses\"\xf2\x01\n\x19\x43\x61ncelMatchmakingResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.CancelMatchmakingResponse.Result\"\x81\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x1a\n\x16SUCCESSFULLY_CANCELLED\x10\x01\x12\x19\n\x15\x45RROR_ALREADY_MATCHED\x10\x02\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x03\x12\x19\n\x15\x45RROR_QUEUE_NOT_FOUND\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CANCELMATCHMAKINGRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.CancelMatchmakingResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESSFULLY_CANCELLED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_MATCHED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_QUEUE_NOT_FOUND', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=216,
  serialized_end=345,
)
_sym_db.RegisterEnumDescriptor(_CANCELMATCHMAKINGRESPONSE_RESULT)


_CANCELMATCHMAKINGRESPONSE = _descriptor.Descriptor(
  name='CancelMatchmakingResponse',
  full_name='pogoprotos.networking.responses.CancelMatchmakingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.CancelMatchmakingResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CANCELMATCHMAKINGRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=345,
)

_CANCELMATCHMAKINGRESPONSE.fields_by_name['result'].enum_type = _CANCELMATCHMAKINGRESPONSE_RESULT
_CANCELMATCHMAKINGRESPONSE_RESULT.containing_type = _CANCELMATCHMAKINGRESPONSE
DESCRIPTOR.message_types_by_name['CancelMatchmakingResponse'] = _CANCELMATCHMAKINGRESPONSE

CancelMatchmakingResponse = _reflection.GeneratedProtocolMessageType('CancelMatchmakingResponse', (_message.Message,), dict(
  DESCRIPTOR = _CANCELMATCHMAKINGRESPONSE,
  __module__ = 'pogoprotos.networking.responses.cancel_matchmaking_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CancelMatchmakingResponse)
  ))
_sym_db.RegisterMessage(CancelMatchmakingResponse)


# @@protoc_insertion_point(module_scope)
