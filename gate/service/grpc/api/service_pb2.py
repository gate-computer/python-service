# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gate/service/grpc/api/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gate/service/grpc/api/service.proto',
  package='gate.service.grpc.api',
  syntax='proto3',
  serialized_pb=_b('\n#gate/service/grpc/api/service.proto\x12\x15gate.service.grpc.api\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"D\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\t\x12\x19\n\x11require_principal\x18\x03 \x01(\x08\"\r\n\x0bInitRequest\"@\n\x0cInitResponse\x12\x30\n\x08services\x18\x01 \x03(\x0b\x32\x1e.gate.service.grpc.api.Service\"i\n\x0eInstanceConfig\x12\x15\n\rmax_send_size\x18\x01 \x01(\x05\x12\x13\n\x0bprocess_key\x18\x02 \x01(\x0c\x12\x14\n\x0cprincipal_id\x18\x03 \x01(\t\x12\x15\n\rinstance_uuid\x18\x04 \x01(\x0c\"n\n\rCreateRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x35\n\x06\x63onfig\x18\x02 \x01(\x0b\x32%.gate.service.grpc.api.InstanceConfig\x12\x10\n\x08snapshot\x18\x03 \x01(\x0c\"7\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x19\n\x11restoration_error\x18\x02 \x01(\t\"\x1c\n\x0eReceiveRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\")\n\rHandleRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x1c\n\x0eSuspendRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"A\n\x0fSnapshotRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x10\n\x08outgoing\x18\x02 \x01(\x0c\x12\x10\n\x08incoming\x18\x03 \x01(\x0c\"\x1d\n\x0fShutdownRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x32Y\n\x04Root\x12Q\n\x04Init\x12\".gate.service.grpc.api.InitRequest\x1a#.gate.service.grpc.api.InitResponse\"\x00\x32\xed\x03\n\x08Instance\x12W\n\x06\x43reate\x12$.gate.service.grpc.api.CreateRequest\x1a%.gate.service.grpc.api.CreateResponse\"\x00\x12Q\n\x07Receive\x12%.gate.service.grpc.api.ReceiveRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x30\x01\x12H\n\x06Handle\x12$.gate.service.grpc.api.HandleRequest\x1a\x16.google.protobuf.Empty\"\x00\x12L\n\x08Shutdown\x12&.gate.service.grpc.api.ShutdownRequest\x1a\x16.google.protobuf.Empty\"\x00\x12J\n\x07Suspend\x12%.gate.service.grpc.api.SuspendRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x08Snapshot\x12&.gate.service.grpc.api.SnapshotRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x42%Z#gate.computer/gate/service/grpc/apib\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='gate.service.grpc.api.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gate.service.grpc.api.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='gate.service.grpc.api.Service.revision', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='require_principal', full_name='gate.service.grpc.api.Service.require_principal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_end=191,
)


_INITREQUEST = _descriptor.Descriptor(
  name='InitRequest',
  full_name='gate.service.grpc.api.InitRequest',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=206,
)


_INITRESPONSE = _descriptor.Descriptor(
  name='InitResponse',
  full_name='gate.service.grpc.api.InitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='gate.service.grpc.api.InitResponse.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=208,
  serialized_end=272,
)


_INSTANCECONFIG = _descriptor.Descriptor(
  name='InstanceConfig',
  full_name='gate.service.grpc.api.InstanceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_send_size', full_name='gate.service.grpc.api.InstanceConfig.max_send_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_key', full_name='gate.service.grpc.api.InstanceConfig.process_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='principal_id', full_name='gate.service.grpc.api.InstanceConfig.principal_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_uuid', full_name='gate.service.grpc.api.InstanceConfig.instance_uuid', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=274,
  serialized_end=379,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='gate.service.grpc.api.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='gate.service.grpc.api.CreateRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='gate.service.grpc.api.CreateRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='gate.service.grpc.api.CreateRequest.snapshot', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=381,
  serialized_end=491,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='gate.service.grpc.api.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.CreateResponse.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restoration_error', full_name='gate.service.grpc.api.CreateResponse.restoration_error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=493,
  serialized_end=548,
)


_RECEIVEREQUEST = _descriptor.Descriptor(
  name='ReceiveRequest',
  full_name='gate.service.grpc.api.ReceiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.ReceiveRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=550,
  serialized_end=578,
)


_HANDLEREQUEST = _descriptor.Descriptor(
  name='HandleRequest',
  full_name='gate.service.grpc.api.HandleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.HandleRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gate.service.grpc.api.HandleRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=580,
  serialized_end=621,
)


_SUSPENDREQUEST = _descriptor.Descriptor(
  name='SuspendRequest',
  full_name='gate.service.grpc.api.SuspendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.SuspendRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=623,
  serialized_end=651,
)


_SNAPSHOTREQUEST = _descriptor.Descriptor(
  name='SnapshotRequest',
  full_name='gate.service.grpc.api.SnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.SnapshotRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outgoing', full_name='gate.service.grpc.api.SnapshotRequest.outgoing', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incoming', full_name='gate.service.grpc.api.SnapshotRequest.incoming', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=653,
  serialized_end=718,
)


_SHUTDOWNREQUEST = _descriptor.Descriptor(
  name='ShutdownRequest',
  full_name='gate.service.grpc.api.ShutdownRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.ShutdownRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=720,
  serialized_end=749,
)

_INITRESPONSE.fields_by_name['services'].message_type = _SERVICE
_CREATEREQUEST.fields_by_name['config'].message_type = _INSTANCECONFIG
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['InitRequest'] = _INITREQUEST
DESCRIPTOR.message_types_by_name['InitResponse'] = _INITRESPONSE
DESCRIPTOR.message_types_by_name['InstanceConfig'] = _INSTANCECONFIG
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['ReceiveRequest'] = _RECEIVEREQUEST
DESCRIPTOR.message_types_by_name['HandleRequest'] = _HANDLEREQUEST
DESCRIPTOR.message_types_by_name['SuspendRequest'] = _SUSPENDREQUEST
DESCRIPTOR.message_types_by_name['SnapshotRequest'] = _SNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['ShutdownRequest'] = _SHUTDOWNREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), dict(
  DESCRIPTOR = _SERVICE,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.Service)
  ))
_sym_db.RegisterMessage(Service)

InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.InitRequest)
  ))
_sym_db.RegisterMessage(InitRequest)

InitResponse = _reflection.GeneratedProtocolMessageType('InitResponse', (_message.Message,), dict(
  DESCRIPTOR = _INITRESPONSE,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.InitResponse)
  ))
_sym_db.RegisterMessage(InitResponse)

InstanceConfig = _reflection.GeneratedProtocolMessageType('InstanceConfig', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCECONFIG,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.InstanceConfig)
  ))
_sym_db.RegisterMessage(InstanceConfig)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESPONSE,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.CreateResponse)
  ))
_sym_db.RegisterMessage(CreateResponse)

ReceiveRequest = _reflection.GeneratedProtocolMessageType('ReceiveRequest', (_message.Message,), dict(
  DESCRIPTOR = _RECEIVEREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.ReceiveRequest)
  ))
_sym_db.RegisterMessage(ReceiveRequest)

HandleRequest = _reflection.GeneratedProtocolMessageType('HandleRequest', (_message.Message,), dict(
  DESCRIPTOR = _HANDLEREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.HandleRequest)
  ))
_sym_db.RegisterMessage(HandleRequest)

SuspendRequest = _reflection.GeneratedProtocolMessageType('SuspendRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUSPENDREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.SuspendRequest)
  ))
_sym_db.RegisterMessage(SuspendRequest)

SnapshotRequest = _reflection.GeneratedProtocolMessageType('SnapshotRequest', (_message.Message,), dict(
  DESCRIPTOR = _SNAPSHOTREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.SnapshotRequest)
  ))
_sym_db.RegisterMessage(SnapshotRequest)

ShutdownRequest = _reflection.GeneratedProtocolMessageType('ShutdownRequest', (_message.Message,), dict(
  DESCRIPTOR = _SHUTDOWNREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.ShutdownRequest)
  ))
_sym_db.RegisterMessage(ShutdownRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z#gate.computer/gate/service/grpc/api'))

_ROOT = _descriptor.ServiceDescriptor(
  name='Root',
  full_name='gate.service.grpc.api.Root',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=751,
  serialized_end=840,
  methods=[
  _descriptor.MethodDescriptor(
    name='Init',
    full_name='gate.service.grpc.api.Root.Init',
    index=0,
    containing_service=None,
    input_type=_INITREQUEST,
    output_type=_INITRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROOT)

DESCRIPTOR.services_by_name['Root'] = _ROOT


_INSTANCE = _descriptor.ServiceDescriptor(
  name='Instance',
  full_name='gate.service.grpc.api.Instance',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=843,
  serialized_end=1336,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='gate.service.grpc.api.Instance.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Receive',
    full_name='gate.service.grpc.api.Instance.Receive',
    index=1,
    containing_service=None,
    input_type=_RECEIVEREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Handle',
    full_name='gate.service.grpc.api.Instance.Handle',
    index=2,
    containing_service=None,
    input_type=_HANDLEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Shutdown',
    full_name='gate.service.grpc.api.Instance.Shutdown',
    index=3,
    containing_service=None,
    input_type=_SHUTDOWNREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Suspend',
    full_name='gate.service.grpc.api.Instance.Suspend',
    index=4,
    containing_service=None,
    input_type=_SUSPENDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Snapshot',
    full_name='gate.service.grpc.api.Instance.Snapshot',
    index=5,
    containing_service=None,
    input_type=_SNAPSHOTREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSTANCE)

DESCRIPTOR.services_by_name['Instance'] = _INSTANCE

# @@protoc_insertion_point(module_scope)
