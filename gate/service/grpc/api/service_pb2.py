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
  serialized_pb=_b('\n#gate/service/grpc/api/service.proto\x12\x15gate.service.grpc.api\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"H\n\x0bServiceInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\t\x12\x19\n\x11require_principal\x18\x03 \x01(\x08\"\r\n\x0bInitRequest\"D\n\x0cInitResponse\x12\x34\n\x08services\x18\x01 \x03(\x0b\x32\".gate.service.grpc.api.ServiceInfo\"i\n\x0eInstanceConfig\x12\x15\n\rmax_send_size\x18\x01 \x01(\x05\x12\x13\n\x0bprocess_key\x18\x02 \x01(\x0c\x12\x14\n\x0cprincipal_id\x18\x03 \x01(\t\x12\x15\n\rinstance_uuid\x18\x04 \x01(\x0c\"\\\n\x15\x43reateInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x06\x63onfig\x18\x02 \x01(\x0b\x32%.gate.service.grpc.api.InstanceConfig\"$\n\x16\x43reateInstanceResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"o\n\x16RestoreInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x06\x63onfig\x18\x02 \x01(\x0b\x32%.gate.service.grpc.api.InstanceConfig\x12\x10\n\x08snapshot\x18\x03 \x01(\x0c\"4\n\x17RestoreInstanceResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x1c\n\x0eReceiveRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\")\n\rHandleRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x1c\n\x0eSuspendRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"A\n\x0fSnapshotRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x10\n\x08outgoing\x18\x02 \x01(\x0c\x12\x10\n\x08incoming\x18\x03 \x01(\x0c\"\x1d\n\x0fShutdownRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x32Y\n\x04Root\x12Q\n\x04Init\x12\".gate.service.grpc.api.InitRequest\x1a#.gate.service.grpc.api.InitResponse\"\x00\x32\xee\x01\n\x07Service\x12o\n\x0e\x43reateInstance\x12,.gate.service.grpc.api.CreateInstanceRequest\x1a-.gate.service.grpc.api.CreateInstanceResponse\"\x00\x12r\n\x0fRestoreInstance\x12-.gate.service.grpc.api.RestoreInstanceRequest\x1a..gate.service.grpc.api.RestoreInstanceResponse\"\x00\x32\x94\x03\n\x08Instance\x12Q\n\x07Receive\x12%.gate.service.grpc.api.ReceiveRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x30\x01\x12H\n\x06Handle\x12$.gate.service.grpc.api.HandleRequest\x1a\x16.google.protobuf.Empty\"\x00\x12L\n\x08Shutdown\x12&.gate.service.grpc.api.ShutdownRequest\x1a\x16.google.protobuf.Empty\"\x00\x12J\n\x07Suspend\x12%.gate.service.grpc.api.SuspendRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x08Snapshot\x12&.gate.service.grpc.api.SnapshotRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x42%Z#gate.computer/gate/service/grpc/apib\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SERVICEINFO = _descriptor.Descriptor(
  name='ServiceInfo',
  full_name='gate.service.grpc.api.ServiceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gate.service.grpc.api.ServiceInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='gate.service.grpc.api.ServiceInfo.revision', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='require_principal', full_name='gate.service.grpc.api.ServiceInfo.require_principal', index=2,
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
  serialized_end=195,
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
  serialized_start=197,
  serialized_end=210,
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
  serialized_start=212,
  serialized_end=280,
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
  serialized_start=282,
  serialized_end=387,
)


_CREATEINSTANCEREQUEST = _descriptor.Descriptor(
  name='CreateInstanceRequest',
  full_name='gate.service.grpc.api.CreateInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gate.service.grpc.api.CreateInstanceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='gate.service.grpc.api.CreateInstanceRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=389,
  serialized_end=481,
)


_CREATEINSTANCERESPONSE = _descriptor.Descriptor(
  name='CreateInstanceResponse',
  full_name='gate.service.grpc.api.CreateInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.CreateInstanceResponse.id', index=0,
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
  serialized_start=483,
  serialized_end=519,
)


_RESTOREINSTANCEREQUEST = _descriptor.Descriptor(
  name='RestoreInstanceRequest',
  full_name='gate.service.grpc.api.RestoreInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gate.service.grpc.api.RestoreInstanceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='gate.service.grpc.api.RestoreInstanceRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='gate.service.grpc.api.RestoreInstanceRequest.snapshot', index=2,
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
  serialized_start=521,
  serialized_end=632,
)


_RESTOREINSTANCERESPONSE = _descriptor.Descriptor(
  name='RestoreInstanceResponse',
  full_name='gate.service.grpc.api.RestoreInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gate.service.grpc.api.RestoreInstanceResponse.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='gate.service.grpc.api.RestoreInstanceResponse.error', index=1,
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
  serialized_start=634,
  serialized_end=686,
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
  serialized_start=688,
  serialized_end=716,
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
  serialized_start=718,
  serialized_end=759,
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
  serialized_start=761,
  serialized_end=789,
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
  serialized_start=791,
  serialized_end=856,
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
  serialized_start=858,
  serialized_end=887,
)

_INITRESPONSE.fields_by_name['services'].message_type = _SERVICEINFO
_CREATEINSTANCEREQUEST.fields_by_name['config'].message_type = _INSTANCECONFIG
_RESTOREINSTANCEREQUEST.fields_by_name['config'].message_type = _INSTANCECONFIG
DESCRIPTOR.message_types_by_name['ServiceInfo'] = _SERVICEINFO
DESCRIPTOR.message_types_by_name['InitRequest'] = _INITREQUEST
DESCRIPTOR.message_types_by_name['InitResponse'] = _INITRESPONSE
DESCRIPTOR.message_types_by_name['InstanceConfig'] = _INSTANCECONFIG
DESCRIPTOR.message_types_by_name['CreateInstanceRequest'] = _CREATEINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['CreateInstanceResponse'] = _CREATEINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['RestoreInstanceRequest'] = _RESTOREINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['RestoreInstanceResponse'] = _RESTOREINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ReceiveRequest'] = _RECEIVEREQUEST
DESCRIPTOR.message_types_by_name['HandleRequest'] = _HANDLEREQUEST
DESCRIPTOR.message_types_by_name['SuspendRequest'] = _SUSPENDREQUEST
DESCRIPTOR.message_types_by_name['SnapshotRequest'] = _SNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['ShutdownRequest'] = _SHUTDOWNREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceInfo = _reflection.GeneratedProtocolMessageType('ServiceInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEINFO,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.ServiceInfo)
  ))
_sym_db.RegisterMessage(ServiceInfo)

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

CreateInstanceRequest = _reflection.GeneratedProtocolMessageType('CreateInstanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINSTANCEREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.CreateInstanceRequest)
  ))
_sym_db.RegisterMessage(CreateInstanceRequest)

CreateInstanceResponse = _reflection.GeneratedProtocolMessageType('CreateInstanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINSTANCERESPONSE,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.CreateInstanceResponse)
  ))
_sym_db.RegisterMessage(CreateInstanceResponse)

RestoreInstanceRequest = _reflection.GeneratedProtocolMessageType('RestoreInstanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESTOREINSTANCEREQUEST,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.RestoreInstanceRequest)
  ))
_sym_db.RegisterMessage(RestoreInstanceRequest)

RestoreInstanceResponse = _reflection.GeneratedProtocolMessageType('RestoreInstanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESTOREINSTANCERESPONSE,
  __module__ = 'gate.service.grpc.api.service_pb2'
  # @@protoc_insertion_point(class_scope:gate.service.grpc.api.RestoreInstanceResponse)
  ))
_sym_db.RegisterMessage(RestoreInstanceResponse)

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
  serialized_start=889,
  serialized_end=978,
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


_SERVICE = _descriptor.ServiceDescriptor(
  name='Service',
  full_name='gate.service.grpc.api.Service',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=981,
  serialized_end=1219,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateInstance',
    full_name='gate.service.grpc.api.Service.CreateInstance',
    index=0,
    containing_service=None,
    input_type=_CREATEINSTANCEREQUEST,
    output_type=_CREATEINSTANCERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RestoreInstance',
    full_name='gate.service.grpc.api.Service.RestoreInstance',
    index=1,
    containing_service=None,
    input_type=_RESTOREINSTANCEREQUEST,
    output_type=_RESTOREINSTANCERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['Service'] = _SERVICE


_INSTANCE = _descriptor.ServiceDescriptor(
  name='Instance',
  full_name='gate.service.grpc.api.Instance',
  file=DESCRIPTOR,
  index=2,
  options=None,
  serialized_start=1222,
  serialized_end=1626,
  methods=[
  _descriptor.MethodDescriptor(
    name='Receive',
    full_name='gate.service.grpc.api.Instance.Receive',
    index=0,
    containing_service=None,
    input_type=_RECEIVEREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Handle',
    full_name='gate.service.grpc.api.Instance.Handle',
    index=1,
    containing_service=None,
    input_type=_HANDLEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Shutdown',
    full_name='gate.service.grpc.api.Instance.Shutdown',
    index=2,
    containing_service=None,
    input_type=_SHUTDOWNREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Suspend',
    full_name='gate.service.grpc.api.Instance.Suspend',
    index=3,
    containing_service=None,
    input_type=_SUSPENDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Snapshot',
    full_name='gate.service.grpc.api.Instance.Snapshot',
    index=4,
    containing_service=None,
    input_type=_SNAPSHOTREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSTANCE)

DESCRIPTOR.services_by_name['Instance'] = _INSTANCE

# @@protoc_insertion_point(module_scope)
