# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/claim_vs_seeker_rewards_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/claim_vs_seeker_rewards_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/responses/claim_vs_seeker_rewards_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x1fpogoprotos/inventory/loot.proto\"\xc1\x02\n\x1c\x43laimVsSeekerRewardsResponse\x12T\n\x06result\x18\x01 \x01(\x0e\x32\x44.pogoprotos.networking.responses.ClaimVsSeekerRewardsResponse.Result\x12+\n\x07rewards\x18\x02 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\"\x9d\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x18\n\x14\x45RROR_REDEEM_POKEMON\x10\x02\x12%\n!ERROR_PLAYER_NOT_ENOUGH_VICTORIES\x10\x03\x12 \n\x1c\x45RROR_REWARD_ALREADY_CLAIMED\x10\x04\x12\x18\n\x14\x45RROR_INVENTORY_FULL\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CLAIMVSSEEKERREWARDSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.ClaimVsSeekerRewardsResponse.Result',
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
      name='ERROR_REDEEM_POKEMON', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_ENOUGH_VICTORIES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_REWARD_ALREADY_CLAIMED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVENTORY_FULL', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=305,
  serialized_end=462,
)
_sym_db.RegisterEnumDescriptor(_CLAIMVSSEEKERREWARDSRESPONSE_RESULT)


_CLAIMVSSEEKERREWARDSRESPONSE = _descriptor.Descriptor(
  name='ClaimVsSeekerRewardsResponse',
  full_name='pogoprotos.networking.responses.ClaimVsSeekerRewardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.ClaimVsSeekerRewardsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='pogoprotos.networking.responses.ClaimVsSeekerRewardsResponse.rewards', index=1,
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
    _CLAIMVSSEEKERREWARDSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=462,
)

_CLAIMVSSEEKERREWARDSRESPONSE.fields_by_name['result'].enum_type = _CLAIMVSSEEKERREWARDSRESPONSE_RESULT
_CLAIMVSSEEKERREWARDSRESPONSE.fields_by_name['rewards'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_CLAIMVSSEEKERREWARDSRESPONSE_RESULT.containing_type = _CLAIMVSSEEKERREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['ClaimVsSeekerRewardsResponse'] = _CLAIMVSSEEKERREWARDSRESPONSE

ClaimVsSeekerRewardsResponse = _reflection.GeneratedProtocolMessageType('ClaimVsSeekerRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMVSSEEKERREWARDSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.claim_vs_seeker_rewards_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ClaimVsSeekerRewardsResponse)
  ))
_sym_db.RegisterMessage(ClaimVsSeekerRewardsResponse)


# @@protoc_insertion_point(module_scope)
