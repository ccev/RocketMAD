# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/combat_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/combat_type.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/settings/master/combat_type.proto\x12\x1apogoprotos.settings.master\x1a#pogoprotos/enums/pokemon_type.proto\"\x99\x01\n\nCombatType\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12\x1c\n\x14nice_level_threshold\x18\x02 \x01(\x02\x12\x1d\n\x15great_level_threshold\x18\x03 \x01(\x02\x12!\n\x19\x65xcellent_level_threshold\x18\x04 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,])




_COMBATTYPE = _descriptor.Descriptor(
  name='CombatType',
  full_name='pogoprotos.settings.master.CombatType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.settings.master.CombatType.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nice_level_threshold', full_name='pogoprotos.settings.master.CombatType.nice_level_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='great_level_threshold', full_name='pogoprotos.settings.master.CombatType.great_level_threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='excellent_level_threshold', full_name='pogoprotos.settings.master.CombatType.excellent_level_threshold', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=267,
)

_COMBATTYPE.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
DESCRIPTOR.message_types_by_name['CombatType'] = _COMBATTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatType = _reflection.GeneratedProtocolMessageType('CombatType', (_message.Message,), dict(
  DESCRIPTOR = _COMBATTYPE,
  __module__ = 'pogoprotos.settings.master.combat_type_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatType)
  ))
_sym_db.RegisterMessage(CombatType)


# @@protoc_insertion_point(module_scope)
