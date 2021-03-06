# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/pokemon_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import pokemon_move_pb2 as pogoprotos_dot_enums_dot_pokemon__move__pb2
from pogoprotos.enums import holo_pokemon_egg_type_pb2 as pogoprotos_dot_enums_dot_holo__pokemon__egg__type__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.data.combat import pokemon_combat_stats_pb2 as pogoprotos_dot_data_dot_combat_dot_pokemon__combat__stats__pb2
from pogoprotos.data.quests import client_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_client__quest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/pokemon_data.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n\"pogoprotos/data/pokemon_data.proto\x12\x0fpogoprotos.data\x1a%pogoprotos/data/pokemon_display.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a#pogoprotos/enums/pokemon_move.proto\x1a,pogoprotos/enums/holo_pokemon_egg_type.proto\x1a\'pogoprotos/inventory/item/item_id.proto\x1a\x31pogoprotos/data/combat/pokemon_combat_stats.proto\x1a)pogoprotos/data/quests/client_quest.proto\"\xf0\r\n\x0bPokemonData\x12\n\n\x02id\x18\x01 \x01(\x06\x12/\n\npokemon_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\n\n\x02\x63p\x18\x03 \x01(\x05\x12\x0f\n\x07stamina\x18\x04 \x01(\x05\x12\x13\n\x0bstamina_max\x18\x05 \x01(\x05\x12-\n\x06move_1\x18\x06 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12-\n\x06move_2\x18\x07 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x18\n\x10\x64\x65ployed_fort_id\x18\x08 \x01(\t\x12\x12\n\nowner_name\x18\t \x01(\t\x12\x0e\n\x06is_egg\x18\n \x01(\x08\x12\x1c\n\x14\x65gg_km_walked_target\x18\x0b \x01(\x01\x12\x1b\n\x13\x65gg_km_walked_start\x18\x0c \x01(\x01\x12\x0e\n\x06origin\x18\x0e \x01(\x05\x12\x10\n\x08height_m\x18\x0f \x01(\x02\x12\x11\n\tweight_kg\x18\x10 \x01(\x02\x12\x19\n\x11individual_attack\x18\x11 \x01(\x05\x12\x1a\n\x12individual_defense\x18\x12 \x01(\x05\x12\x1a\n\x12individual_stamina\x18\x13 \x01(\x05\x12\x15\n\rcp_multiplier\x18\x14 \x01(\x02\x12\x33\n\x08pokeball\x18\x15 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x18\n\x10\x63\x61ptured_cell_id\x18\x16 \x01(\x04\x12\x18\n\x10\x62\x61ttles_attacked\x18\x17 \x01(\x05\x12\x18\n\x10\x62\x61ttles_defended\x18\x18 \x01(\x05\x12\x18\n\x10\x65gg_incubator_id\x18\x19 \x01(\t\x12\x18\n\x10\x63reation_time_ms\x18\x1a \x01(\x04\x12\x14\n\x0cnum_upgrades\x18\x1b \x01(\x05\x12 \n\x18\x61\x64\x64itional_cp_multiplier\x18\x1c \x01(\x02\x12\x10\n\x08\x66\x61vorite\x18\x1d \x01(\x05\x12\x10\n\x08nickname\x18\x1e \x01(\t\x12\x11\n\tfrom_fort\x18\x1f \x01(\x05\x12\x1b\n\x13\x62uddy_candy_awarded\x18  \x01(\x05\x12\x1d\n\x15\x62uddy_total_km_walked\x18! \x01(\x02\x12\x1a\n\x12\x64isplay_pokemon_id\x18\" \x01(\x05\x12\x12\n\ndisplay_cp\x18# \x01(\x05\x12\x38\n\x0fpokemon_display\x18$ \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x0e\n\x06is_bad\x18% \x01(\x08\x12\x18\n\x10hatched_from_egg\x18& \x01(\x08\x12\x16\n\x0e\x63oins_returned\x18\' \x01(\x05\x12\x1c\n\x14\x64\x65ployed_duration_ms\x18( \x01(\x03\x12&\n\x1e\x64\x65ployed_returned_timestamp_ms\x18) \x01(\x03\x12$\n\x1c\x63p_multiplier_before_trading\x18* \x01(\x02\x12#\n\x1btrading_original_owner_hash\x18+ \x01(\x05\x12\x1f\n\x17original_owner_nickname\x18, \x01(\t\x12\x16\n\x0etraded_time_ms\x18- \x01(\x03\x12\x10\n\x08is_lucky\x18. \x01(\x08\x12-\n\x06move_3\x18/ \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x44\n\x10pvp_combat_stats\x18\x30 \x01(\x0b\x32*.pogoprotos.data.combat.PokemonCombatStats\x12\x44\n\x10npc_combat_stats\x18\x31 \x01(\x0b\x32*.pogoprotos.data.combat.PokemonCombatStats\x12#\n\x1bmove2_is_purified_exclusive\x18\x32 \x01(\x08\x12\"\n\x1alimited_pokemon_identifier\x18\x33 \x01(\t\x12\x16\n\x0epre_boosted_cp\x18\x34 \x01(\x05\x12,\n$pre_boosted_additional_cp_multiplier\x18\x35 \x01(\x02\x12\x1f\n\x17\x64\x65ployed_gym_lat_degree\x18\x37 \x01(\x01\x12\x1f\n\x17\x64\x65ployed_gym_lng_degree\x18\x38 \x01(\x01\x12\x36\n\x08\x65gg_type\x18: \x01(\x0e\x32$.pogoprotos.enums.HoloPokemonEggType\x12N\n!quest_buddy_evolution_requirement\x18> \x03(\x0b\x32#.pogoprotos.data.quests.ClientQuestb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__move__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_holo__pokemon__egg__type__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_pokemon__combat__stats__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_client__quest__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEMONDATA = _descriptor.Descriptor(
  name='PokemonData',
  full_name='pogoprotos.data.PokemonData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.data.PokemonData.id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.PokemonData.pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp', full_name='pogoprotos.data.PokemonData.cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='pogoprotos.data.PokemonData.stamina', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina_max', full_name='pogoprotos.data.PokemonData.stamina_max', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_1', full_name='pogoprotos.data.PokemonData.move_1', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_2', full_name='pogoprotos.data.PokemonData.move_2', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_fort_id', full_name='pogoprotos.data.PokemonData.deployed_fort_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_name', full_name='pogoprotos.data.PokemonData.owner_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_egg', full_name='pogoprotos.data.PokemonData.is_egg', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_km_walked_target', full_name='pogoprotos.data.PokemonData.egg_km_walked_target', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_km_walked_start', full_name='pogoprotos.data.PokemonData.egg_km_walked_start', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='pogoprotos.data.PokemonData.origin', index=12,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_m', full_name='pogoprotos.data.PokemonData.height_m', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_kg', full_name='pogoprotos.data.PokemonData.weight_kg', index=14,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_attack', full_name='pogoprotos.data.PokemonData.individual_attack', index=15,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_defense', full_name='pogoprotos.data.PokemonData.individual_defense', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_stamina', full_name='pogoprotos.data.PokemonData.individual_stamina', index=17,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp_multiplier', full_name='pogoprotos.data.PokemonData.cp_multiplier', index=18,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='pogoprotos.data.PokemonData.pokeball', index=19,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_cell_id', full_name='pogoprotos.data.PokemonData.captured_cell_id', index=20,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_attacked', full_name='pogoprotos.data.PokemonData.battles_attacked', index=21,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_defended', full_name='pogoprotos.data.PokemonData.battles_defended', index=22,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubator_id', full_name='pogoprotos.data.PokemonData.egg_incubator_id', index=23,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time_ms', full_name='pogoprotos.data.PokemonData.creation_time_ms', index=24,
      number=26, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_upgrades', full_name='pogoprotos.data.PokemonData.num_upgrades', index=25,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_cp_multiplier', full_name='pogoprotos.data.PokemonData.additional_cp_multiplier', index=26,
      number=28, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favorite', full_name='pogoprotos.data.PokemonData.favorite', index=27,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='pogoprotos.data.PokemonData.nickname', index=28,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_fort', full_name='pogoprotos.data.PokemonData.from_fort', index=29,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_candy_awarded', full_name='pogoprotos.data.PokemonData.buddy_candy_awarded', index=30,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_total_km_walked', full_name='pogoprotos.data.PokemonData.buddy_total_km_walked', index=31,
      number=33, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_pokemon_id', full_name='pogoprotos.data.PokemonData.display_pokemon_id', index=32,
      number=34, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_cp', full_name='pogoprotos.data.PokemonData.display_cp', index=33,
      number=35, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.PokemonData.pokemon_display', index=34,
      number=36, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_bad', full_name='pogoprotos.data.PokemonData.is_bad', index=35,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hatched_from_egg', full_name='pogoprotos.data.PokemonData.hatched_from_egg', index=36,
      number=38, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coins_returned', full_name='pogoprotos.data.PokemonData.coins_returned', index=37,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_duration_ms', full_name='pogoprotos.data.PokemonData.deployed_duration_ms', index=38,
      number=40, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_returned_timestamp_ms', full_name='pogoprotos.data.PokemonData.deployed_returned_timestamp_ms', index=39,
      number=41, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp_multiplier_before_trading', full_name='pogoprotos.data.PokemonData.cp_multiplier_before_trading', index=40,
      number=42, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trading_original_owner_hash', full_name='pogoprotos.data.PokemonData.trading_original_owner_hash', index=41,
      number=43, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_owner_nickname', full_name='pogoprotos.data.PokemonData.original_owner_nickname', index=42,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traded_time_ms', full_name='pogoprotos.data.PokemonData.traded_time_ms', index=43,
      number=45, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_lucky', full_name='pogoprotos.data.PokemonData.is_lucky', index=44,
      number=46, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_3', full_name='pogoprotos.data.PokemonData.move_3', index=45,
      number=47, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_combat_stats', full_name='pogoprotos.data.PokemonData.pvp_combat_stats', index=46,
      number=48, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='npc_combat_stats', full_name='pogoprotos.data.PokemonData.npc_combat_stats', index=47,
      number=49, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move2_is_purified_exclusive', full_name='pogoprotos.data.PokemonData.move2_is_purified_exclusive', index=48,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limited_pokemon_identifier', full_name='pogoprotos.data.PokemonData.limited_pokemon_identifier', index=49,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_boosted_cp', full_name='pogoprotos.data.PokemonData.pre_boosted_cp', index=50,
      number=52, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_boosted_additional_cp_multiplier', full_name='pogoprotos.data.PokemonData.pre_boosted_additional_cp_multiplier', index=51,
      number=53, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_gym_lat_degree', full_name='pogoprotos.data.PokemonData.deployed_gym_lat_degree', index=52,
      number=55, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_gym_lng_degree', full_name='pogoprotos.data.PokemonData.deployed_gym_lng_degree', index=53,
      number=56, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_type', full_name='pogoprotos.data.PokemonData.egg_type', index=54,
      number=58, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_buddy_evolution_requirement', full_name='pogoprotos.data.PokemonData.quest_buddy_evolution_requirement', index=55,
      number=62, type=11, cpp_type=10, label=3,
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
  serialized_start=348,
  serialized_end=2124,
)

_POKEMONDATA.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONDATA.fields_by_name['move_1'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONDATA.fields_by_name['move_2'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONDATA.fields_by_name['pokeball'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_POKEMONDATA.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_POKEMONDATA.fields_by_name['move_3'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONDATA.fields_by_name['pvp_combat_stats'].message_type = pogoprotos_dot_data_dot_combat_dot_pokemon__combat__stats__pb2._POKEMONCOMBATSTATS
_POKEMONDATA.fields_by_name['npc_combat_stats'].message_type = pogoprotos_dot_data_dot_combat_dot_pokemon__combat__stats__pb2._POKEMONCOMBATSTATS
_POKEMONDATA.fields_by_name['egg_type'].enum_type = pogoprotos_dot_enums_dot_holo__pokemon__egg__type__pb2._HOLOPOKEMONEGGTYPE
_POKEMONDATA.fields_by_name['quest_buddy_evolution_requirement'].message_type = pogoprotos_dot_data_dot_quests_dot_client__quest__pb2._CLIENTQUEST
DESCRIPTOR.message_types_by_name['PokemonData'] = _POKEMONDATA

PokemonData = _reflection.GeneratedProtocolMessageType('PokemonData', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONDATA,
  __module__ = 'pogoprotos.data.pokemon_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.PokemonData)
  ))
_sym_db.RegisterMessage(PokemonData)


# @@protoc_insertion_point(module_scope)
