# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/check_share_ex_raid_pass_message.proto

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
  name='pogoprotos/networking/requests/messages/check_share_ex_raid_pass_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nNpogoprotos/networking/requests/messages/check_share_ex_raid_pass_message.proto\x12\'pogoprotos.networking.requests.messages\"T\n\x1b\x43heckShareExRaidPassMessage\x12\x11\n\tfriend_id\x18\x01 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x11\n\traid_seed\x18\x03 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKSHAREEXRAIDPASSMESSAGE = _descriptor.Descriptor(
  name='CheckShareExRaidPassMessage',
  full_name='pogoprotos.networking.requests.messages.CheckShareExRaidPassMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friend_id', full_name='pogoprotos.networking.requests.messages.CheckShareExRaidPassMessage.friend_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.networking.requests.messages.CheckShareExRaidPassMessage.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_seed', full_name='pogoprotos.networking.requests.messages.CheckShareExRaidPassMessage.raid_seed', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['CheckShareExRaidPassMessage'] = _CHECKSHAREEXRAIDPASSMESSAGE

CheckShareExRaidPassMessage = _reflection.GeneratedProtocolMessageType('CheckShareExRaidPassMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHECKSHAREEXRAIDPASSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.check_share_ex_raid_pass_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.CheckShareExRaidPassMessage)
  ))
_sym_db.RegisterMessage(CheckShareExRaidPassMessage)


# @@protoc_insertion_point(module_scope)
