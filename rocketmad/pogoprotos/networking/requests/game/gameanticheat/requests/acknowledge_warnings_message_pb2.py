# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gameanticheat/requests/acknowledge_warnings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import platform_warning_type_pb2 as pogoprotos_dot_enums_dot_platform__warning__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gameanticheat/requests/acknowledge_warnings_message.proto',
  package='pogoprotos.networking.requests.game.gameanticheat.requests',
  syntax='proto3',
  serialized_pb=_b('\n]pogoprotos/networking/requests/game/gameanticheat/requests/acknowledge_warnings_message.proto\x12:pogoprotos.networking.requests.game.gameanticheat.requests\x1a,pogoprotos/enums/platform_warning_type.proto\"T\n\x1a\x41\x63knowledgeWarningsMessage\x12\x36\n\x07warning\x18\x01 \x03(\x0e\x32%.pogoprotos.enums.PlatformWarningTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_platform__warning__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACKNOWLEDGEWARNINGSMESSAGE = _descriptor.Descriptor(
  name='AcknowledgeWarningsMessage',
  full_name='pogoprotos.networking.requests.game.gameanticheat.requests.AcknowledgeWarningsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='warning', full_name='pogoprotos.networking.requests.game.gameanticheat.requests.AcknowledgeWarningsMessage.warning', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=203,
  serialized_end=287,
)

_ACKNOWLEDGEWARNINGSMESSAGE.fields_by_name['warning'].enum_type = pogoprotos_dot_enums_dot_platform__warning__type__pb2._PLATFORMWARNINGTYPE
DESCRIPTOR.message_types_by_name['AcknowledgeWarningsMessage'] = _ACKNOWLEDGEWARNINGSMESSAGE

AcknowledgeWarningsMessage = _reflection.GeneratedProtocolMessageType('AcknowledgeWarningsMessage', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEWARNINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gameanticheat.requests.acknowledge_warnings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gameanticheat.requests.AcknowledgeWarningsMessage)
  ))
_sym_db.RegisterMessage(AcknowledgeWarningsMessage)


# @@protoc_insertion_point(module_scope)
