# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/set_lobby_visibility_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.raid import lobby_pb2 as pogoprotos_dot_data_dot_raid_dot_lobby__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/set_lobby_visibility_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nCpogoprotos/networking/responses/set_lobby_visibility_response.proto\x12\x1fpogoprotos.networking.responses\x1a pogoprotos/data/raid/lobby.proto\"\x92\x02\n\x1aSetLobbyVisibilityResponse\x12R\n\x06result\x18\x01 \x01(\x0e\x32\x42.pogoprotos.networking.responses.SetLobbyVisibilityResponse.Result\x12*\n\x05lobby\x18\x02 \x01(\x0b\x32\x1b.pogoprotos.data.raid.Lobby\"t\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1b\n\x17\x45RROR_NOT_LOBBY_CREATOR\x10\x02\x12\x19\n\x15\x45RROR_LOBBY_NOT_FOUND\x10\x03\x12\x1a\n\x16\x45RROR_RAID_UNAVAILABLE\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_raid_dot_lobby__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SETLOBBYVISIBILITYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.SetLobbyVisibilityResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_LOBBY_CREATOR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LOBBY_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RAID_UNAVAILABLE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=297,
  serialized_end=413,
)
_sym_db.RegisterEnumDescriptor(_SETLOBBYVISIBILITYRESPONSE_RESULT)


_SETLOBBYVISIBILITYRESPONSE = _descriptor.Descriptor(
  name='SetLobbyVisibilityResponse',
  full_name='pogoprotos.networking.responses.SetLobbyVisibilityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.SetLobbyVisibilityResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lobby', full_name='pogoprotos.networking.responses.SetLobbyVisibilityResponse.lobby', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETLOBBYVISIBILITYRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=413,
)

_SETLOBBYVISIBILITYRESPONSE.fields_by_name['result'].enum_type = _SETLOBBYVISIBILITYRESPONSE_RESULT
_SETLOBBYVISIBILITYRESPONSE.fields_by_name['lobby'].message_type = pogoprotos_dot_data_dot_raid_dot_lobby__pb2._LOBBY
_SETLOBBYVISIBILITYRESPONSE_RESULT.containing_type = _SETLOBBYVISIBILITYRESPONSE
DESCRIPTOR.message_types_by_name['SetLobbyVisibilityResponse'] = _SETLOBBYVISIBILITYRESPONSE

SetLobbyVisibilityResponse = _reflection.GeneratedProtocolMessageType('SetLobbyVisibilityResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETLOBBYVISIBILITYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.set_lobby_visibility_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SetLobbyVisibilityResponse)
  ))
_sym_db.RegisterMessage(SetLobbyVisibilityResponse)


# @@protoc_insertion_point(module_scope)