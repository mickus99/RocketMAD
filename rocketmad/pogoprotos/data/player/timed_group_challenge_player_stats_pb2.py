# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/timed_group_challenge_player_stats.proto

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
  name='pogoprotos/data/player/timed_group_challenge_player_stats.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n?pogoprotos/data/player/timed_group_challenge_player_stats.proto\x12\x16pogoprotos.data.player\"\xcd\x01\n\x1eTimedGroupChallengePlayerStats\x12\x63\n\nchallenges\x18\x01 \x03(\x0b\x32O.pogoprotos.data.player.TimedGroupChallengePlayerStats.IndividualChallengeStats\x1a\x46\n\x18IndividualChallengeStats\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\t\x12\x14\n\x0cplayer_score\x18\x02 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TIMEDGROUPCHALLENGEPLAYERSTATS_INDIVIDUALCHALLENGESTATS = _descriptor.Descriptor(
  name='IndividualChallengeStats',
  full_name='pogoprotos.data.player.TimedGroupChallengePlayerStats.IndividualChallengeStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='pogoprotos.data.player.TimedGroupChallengePlayerStats.IndividualChallengeStats.challenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_score', full_name='pogoprotos.data.player.TimedGroupChallengePlayerStats.IndividualChallengeStats.player_score', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=227,
  serialized_end=297,
)

_TIMEDGROUPCHALLENGEPLAYERSTATS = _descriptor.Descriptor(
  name='TimedGroupChallengePlayerStats',
  full_name='pogoprotos.data.player.TimedGroupChallengePlayerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenges', full_name='pogoprotos.data.player.TimedGroupChallengePlayerStats.challenges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TIMEDGROUPCHALLENGEPLAYERSTATS_INDIVIDUALCHALLENGESTATS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=297,
)

_TIMEDGROUPCHALLENGEPLAYERSTATS_INDIVIDUALCHALLENGESTATS.containing_type = _TIMEDGROUPCHALLENGEPLAYERSTATS
_TIMEDGROUPCHALLENGEPLAYERSTATS.fields_by_name['challenges'].message_type = _TIMEDGROUPCHALLENGEPLAYERSTATS_INDIVIDUALCHALLENGESTATS
DESCRIPTOR.message_types_by_name['TimedGroupChallengePlayerStats'] = _TIMEDGROUPCHALLENGEPLAYERSTATS

TimedGroupChallengePlayerStats = _reflection.GeneratedProtocolMessageType('TimedGroupChallengePlayerStats', (_message.Message,), dict(

  IndividualChallengeStats = _reflection.GeneratedProtocolMessageType('IndividualChallengeStats', (_message.Message,), dict(
    DESCRIPTOR = _TIMEDGROUPCHALLENGEPLAYERSTATS_INDIVIDUALCHALLENGESTATS,
    __module__ = 'pogoprotos.data.player.timed_group_challenge_player_stats_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.player.TimedGroupChallengePlayerStats.IndividualChallengeStats)
    ))
  ,
  DESCRIPTOR = _TIMEDGROUPCHALLENGEPLAYERSTATS,
  __module__ = 'pogoprotos.data.player.timed_group_challenge_player_stats_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.TimedGroupChallengePlayerStats)
  ))
_sym_db.RegisterMessage(TimedGroupChallengePlayerStats)
_sym_db.RegisterMessage(TimedGroupChallengePlayerStats.IndividualChallengeStats)


# @@protoc_insertion_point(module_scope)
