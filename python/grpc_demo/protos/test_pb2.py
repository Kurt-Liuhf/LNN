# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\x12\x04test\"/\n\x0esurfaceRequest\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\"\x1b\n\x0csurfaceReply\x12\x0b\n\x03res\x18\x01 \x01(\x05\"\x0f\n\rvolumeRequest\"\r\n\x0bvolumeReply2y\n\x0cmathServices\x12\x35\n\x07surface\x12\x14.test.surfaceRequest\x1a\x12.test.surfaceReply\"\x00\x12\x32\n\x06volume\x12\x13.test.volumeRequest\x1a\x11.test.volumeReply\"\x00\x62\x06proto3')
)




_SURFACEREQUEST = _descriptor.Descriptor(
  name='surfaceRequest',
  full_name='test.surfaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='test.surfaceRequest.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='test.surfaceRequest.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=20,
  serialized_end=67,
)


_SURFACEREPLY = _descriptor.Descriptor(
  name='surfaceReply',
  full_name='test.surfaceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='test.surfaceReply.res', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=96,
)


_VOLUMEREQUEST = _descriptor.Descriptor(
  name='volumeRequest',
  full_name='test.volumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=98,
  serialized_end=113,
)


_VOLUMEREPLY = _descriptor.Descriptor(
  name='volumeReply',
  full_name='test.volumeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=115,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['surfaceRequest'] = _SURFACEREQUEST
DESCRIPTOR.message_types_by_name['surfaceReply'] = _SURFACEREPLY
DESCRIPTOR.message_types_by_name['volumeRequest'] = _VOLUMEREQUEST
DESCRIPTOR.message_types_by_name['volumeReply'] = _VOLUMEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

surfaceRequest = _reflection.GeneratedProtocolMessageType('surfaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _SURFACEREQUEST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.surfaceRequest)
  ))
_sym_db.RegisterMessage(surfaceRequest)

surfaceReply = _reflection.GeneratedProtocolMessageType('surfaceReply', (_message.Message,), dict(
  DESCRIPTOR = _SURFACEREPLY,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.surfaceReply)
  ))
_sym_db.RegisterMessage(surfaceReply)

volumeRequest = _reflection.GeneratedProtocolMessageType('volumeRequest', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMEREQUEST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.volumeRequest)
  ))
_sym_db.RegisterMessage(volumeRequest)

volumeReply = _reflection.GeneratedProtocolMessageType('volumeReply', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMEREPLY,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.volumeReply)
  ))
_sym_db.RegisterMessage(volumeReply)



_MATHSERVICES = _descriptor.ServiceDescriptor(
  name='mathServices',
  full_name='test.mathServices',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=130,
  serialized_end=251,
  methods=[
  _descriptor.MethodDescriptor(
    name='surface',
    full_name='test.mathServices.surface',
    index=0,
    containing_service=None,
    input_type=_SURFACEREQUEST,
    output_type=_SURFACEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='volume',
    full_name='test.mathServices.volume',
    index=1,
    containing_service=None,
    input_type=_VOLUMEREQUEST,
    output_type=_VOLUMEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MATHSERVICES)

DESCRIPTOR.services_by_name['mathServices'] = _MATHSERVICES

# @@protoc_insertion_point(module_scope)
