# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/ar_mapping_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/ar_mapping_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-pogoprotos/settings/ar_mapping_settings.proto\x12\x13pogoprotos.settings\"\x8e\x08\n\x11\x41rMappingSettings\x12 \n\x18min_hours_between_prompt\x18\x01 \x01(\x05\x12\x1e\n\x16max_video_time_seconds\x18\x02 \x01(\x05\x12\"\n\x1apreview_video_bitrate_kbps\x18\x03 \x01(\x05\x12!\n\x19preview_video_deadline_ms\x18\x04 \x01(\x05\x12#\n\x1bresearch_video_bitrate_kbps\x18\x05 \x01(\x05\x12\"\n\x1aresearch_video_deadline_ms\x18\x06 \x01(\x05\x12\x1e\n\x16min_video_time_seconds\x18\x07 \x01(\x05\x12\x1e\n\x16preview_frame_rate_fps\x18\x08 \x01(\x05\x12\x1e\n\x16preview_frames_to_jump\x18\t \x01(\x05\x12\'\n\x1fmax_upload_chunk_rejected_count\x18\n \x01(\x05\x12 \n\x18\x61rdk_desired_accuracy_mm\x18\x0b \x01(\x05\x12\x1f\n\x17\x61rdk_update_distance_mm\x18\x0c \x01(\x05\x12$\n\x1cmax_pending_upload_kilobytes\x18\r \x01(\x05\x12\x1f\n\x17\x65nable_sponsor_poi_scan\x18\x0e \x01(\x08\x12 \n\x18min_disk_space_needed_mb\x18\x0f \x01(\x05\x12\x1f\n\x17scan_validation_enabled\x18\x10 \x01(\x08\x12%\n\x1dscan_validation_start_delay_s\x18\x11 \x01(\x02\x12,\n$scan_validation_lumens_min_threshold\x18\x12 \x01(\x02\x12/\n\'scan_validation_lumens_smoothing_factor\x18\x13 \x01(\x02\x12/\n\'scan_validation_average_pixel_threshold\x18\x14 \x01(\x02\x12\x36\n.scan_validation_average_pixel_smoothing_factor\x18\x15 \x01(\x02\x12\x32\n*scan_validation_speed_min_threshold_mper_s\x18\x16 \x01(\x02\x12\x32\n*scan_validation_speed_max_threshold_mper_s\x18\x17 \x01(\x02\x12.\n&scan_validation_speed_smoothing_factor\x18\x18 \x01(\x02\x12*\n\"scan_validation_max_warning_time_s\x18\x19 \x01(\x02\x12\x1e\n\x16\x61r_recorder_v2_enabled\x18\x1a \x01(\x08\x62\x06proto3')
)




_ARMAPPINGSETTINGS = _descriptor.Descriptor(
  name='ArMappingSettings',
  full_name='pogoprotos.settings.ArMappingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_hours_between_prompt', full_name='pogoprotos.settings.ArMappingSettings.min_hours_between_prompt', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_video_time_seconds', full_name='pogoprotos.settings.ArMappingSettings.max_video_time_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_video_bitrate_kbps', full_name='pogoprotos.settings.ArMappingSettings.preview_video_bitrate_kbps', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_video_deadline_ms', full_name='pogoprotos.settings.ArMappingSettings.preview_video_deadline_ms', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='research_video_bitrate_kbps', full_name='pogoprotos.settings.ArMappingSettings.research_video_bitrate_kbps', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='research_video_deadline_ms', full_name='pogoprotos.settings.ArMappingSettings.research_video_deadline_ms', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_video_time_seconds', full_name='pogoprotos.settings.ArMappingSettings.min_video_time_seconds', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_frame_rate_fps', full_name='pogoprotos.settings.ArMappingSettings.preview_frame_rate_fps', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_frames_to_jump', full_name='pogoprotos.settings.ArMappingSettings.preview_frames_to_jump', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_upload_chunk_rejected_count', full_name='pogoprotos.settings.ArMappingSettings.max_upload_chunk_rejected_count', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ardk_desired_accuracy_mm', full_name='pogoprotos.settings.ArMappingSettings.ardk_desired_accuracy_mm', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ardk_update_distance_mm', full_name='pogoprotos.settings.ArMappingSettings.ardk_update_distance_mm', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_pending_upload_kilobytes', full_name='pogoprotos.settings.ArMappingSettings.max_pending_upload_kilobytes', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_sponsor_poi_scan', full_name='pogoprotos.settings.ArMappingSettings.enable_sponsor_poi_scan', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_disk_space_needed_mb', full_name='pogoprotos.settings.ArMappingSettings.min_disk_space_needed_mb', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_enabled', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_enabled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_start_delay_s', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_start_delay_s', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_lumens_min_threshold', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_lumens_min_threshold', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_lumens_smoothing_factor', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_lumens_smoothing_factor', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_average_pixel_threshold', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_average_pixel_threshold', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_average_pixel_smoothing_factor', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_average_pixel_smoothing_factor', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_speed_min_threshold_mper_s', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_speed_min_threshold_mper_s', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_speed_max_threshold_mper_s', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_speed_max_threshold_mper_s', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_speed_smoothing_factor', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_speed_smoothing_factor', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_validation_max_warning_time_s', full_name='pogoprotos.settings.ArMappingSettings.scan_validation_max_warning_time_s', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ar_recorder_v2_enabled', full_name='pogoprotos.settings.ArMappingSettings.ar_recorder_v2_enabled', index=25,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=71,
  serialized_end=1109,
)

DESCRIPTOR.message_types_by_name['ArMappingSettings'] = _ARMAPPINGSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArMappingSettings = _reflection.GeneratedProtocolMessageType('ArMappingSettings', (_message.Message,), dict(
  DESCRIPTOR = _ARMAPPINGSETTINGS,
  __module__ = 'pogoprotos.settings.ar_mapping_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.ArMappingSettings)
  ))
_sym_db.RegisterMessage(ArMappingSettings)


# @@protoc_insertion_point(module_scope)
