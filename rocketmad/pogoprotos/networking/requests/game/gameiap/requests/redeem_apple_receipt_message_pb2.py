# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gameiap/requests/redeem_apple_receipt_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gameiap/requests/redeem_apple_receipt_message.proto',
  package='pogoprotos.networking.requests.game.gameiap.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nWpogoprotos/networking/requests/game/gameiap/requests/redeem_apple_receipt_message.proto\x12\x34pogoprotos.networking.requests.game.gameiap.requests\"z\n\x19RedeemAppleReceiptMessage\x12\x0f\n\x07receipt\x18\x01 \x01(\t\x12\x19\n\x11purchase_currency\x18\x02 \x01(\t\x12\x15\n\rprice_paid_e6\x18\x03 \x01(\x05\x12\x1a\n\x12price_paid_e6_long\x18\x04 \x01(\x03\x62\x06proto3')
)




_REDEEMAPPLERECEIPTMESSAGE = _descriptor.Descriptor(
  name='RedeemAppleReceiptMessage',
  full_name='pogoprotos.networking.requests.game.gameiap.requests.RedeemAppleReceiptMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='receipt', full_name='pogoprotos.networking.requests.game.gameiap.requests.RedeemAppleReceiptMessage.receipt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='purchase_currency', full_name='pogoprotos.networking.requests.game.gameiap.requests.RedeemAppleReceiptMessage.purchase_currency', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_paid_e6', full_name='pogoprotos.networking.requests.game.gameiap.requests.RedeemAppleReceiptMessage.price_paid_e6', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_paid_e6_long', full_name='pogoprotos.networking.requests.game.gameiap.requests.RedeemAppleReceiptMessage.price_paid_e6_long', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=145,
  serialized_end=267,
)

DESCRIPTOR.message_types_by_name['RedeemAppleReceiptMessage'] = _REDEEMAPPLERECEIPTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemAppleReceiptMessage = _reflection.GeneratedProtocolMessageType('RedeemAppleReceiptMessage', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMAPPLERECEIPTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gameiap.requests.redeem_apple_receipt_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gameiap.requests.RedeemAppleReceiptMessage)
  ))
_sym_db.RegisterMessage(RedeemAppleReceiptMessage)


# @@protoc_insertion_point(module_scope)
