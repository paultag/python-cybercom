# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: primitives.proto

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
  name='primitives.proto',
  package='cybercom',
  syntax='proto3',
  serialized_pb=_b('\n\x10primitives.proto\x12\x08\x63ybercom\"\x12\n\x03\x43SR\x12\x0b\n\x03\x64\x65r\x18\x01 \x01(\x0c\"\x1a\n\x0b\x43\x65rtificate\x12\x0b\n\x03\x64\x65r\x18\x01 \x01(\x0c\x42\x04Z\x02pbb\x06proto3')
)




_CSR = _descriptor.Descriptor(
  name='CSR',
  full_name='cybercom.CSR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='der', full_name='cybercom.CSR.der', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=30,
  serialized_end=48,
)


_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='cybercom.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='der', full_name='cybercom.Certificate.der', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=50,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['CSR'] = _CSR
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CSR = _reflection.GeneratedProtocolMessageType('CSR', (_message.Message,), dict(
  DESCRIPTOR = _CSR,
  __module__ = 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cybercom.CSR)
  ))
_sym_db.RegisterMessage(CSR)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATE,
  __module__ = 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cybercom.Certificate)
  ))
_sym_db.RegisterMessage(Certificate)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\002pb'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
