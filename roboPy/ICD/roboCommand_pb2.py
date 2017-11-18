# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: roboCommand.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='roboCommand.proto',
  package='roboICD',
  serialized_pb='\n\x11roboCommand.proto\x12\x07roboICD\"=\n\x08Lighting\x12\x0b\n\x03\x63\x61m\x18\x01 \x02(\x08\x12\x12\n\ngreenLight\x18\x02 \x02(\x08\x12\x10\n\x08redLight\x18\x03 \x02(\x08\"p\n\x0e\x43ommandRequest\x12\x14\n\x0cportMotorSpd\x18\x01 \x01(\x05\x12\x14\n\x0cstarMotorSpd\x18\x02 \x01(\x05\x12#\n\x08lightCmd\x18\x03 \x01(\x0b\x32\x11.roboICD.Lighting\x12\r\n\x05\x63\x61mOn\x18\x04 \x01(\x08\"Y\n\x0f\x43ommandResponse\x12\x10\n\x08received\x18\x01 \x02(\x08\x12%\n\nlightState\x18\x02 \x02(\x0b\x32\x11.roboICD.Lighting\x12\r\n\x05\x63\x61mOn\x18\x03 \x02(\x08\x32N\n\x0e\x43ommandService\x12<\n\x07\x43ommand\x12\x17.roboICD.CommandRequest\x1a\x18.roboICD.CommandResponseB5\n-com.googlecode.protobuf.socketrpc.robocontrol\x88\x01\x01\x90\x01\x01')




_LIGHTING = _descriptor.Descriptor(
  name='Lighting',
  full_name='roboICD.Lighting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cam', full_name='roboICD.Lighting.cam', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='greenLight', full_name='roboICD.Lighting.greenLight', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='redLight', full_name='roboICD.Lighting.redLight', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  serialized_start=30,
  serialized_end=91,
)


_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='roboICD.CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='portMotorSpd', full_name='roboICD.CommandRequest.portMotorSpd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='starMotorSpd', full_name='roboICD.CommandRequest.starMotorSpd', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lightCmd', full_name='roboICD.CommandRequest.lightCmd', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camOn', full_name='roboICD.CommandRequest.camOn', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  serialized_start=93,
  serialized_end=205,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='roboICD.CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='received', full_name='roboICD.CommandResponse.received', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lightState', full_name='roboICD.CommandResponse.lightState', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camOn', full_name='roboICD.CommandResponse.camOn', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  serialized_start=207,
  serialized_end=296,
)

_COMMANDREQUEST.fields_by_name['lightCmd'].message_type = _LIGHTING
_COMMANDRESPONSE.fields_by_name['lightState'].message_type = _LIGHTING
DESCRIPTOR.message_types_by_name['Lighting'] = _LIGHTING
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE

class Lighting(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LIGHTING

  # @@protoc_insertion_point(class_scope:roboICD.Lighting)

class CommandRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMANDREQUEST

  # @@protoc_insertion_point(class_scope:roboICD.CommandRequest)

class CommandResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMANDRESPONSE

  # @@protoc_insertion_point(class_scope:roboICD.CommandResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n-com.googlecode.protobuf.socketrpc.robocontrol\210\001\001\220\001\001')

_COMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='CommandService',
  full_name='roboICD.CommandService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=298,
  serialized_end=376,
  methods=[
  _descriptor.MethodDescriptor(
    name='Command',
    full_name='roboICD.CommandService.Command',
    index=0,
    containing_service=None,
    input_type=_COMMANDREQUEST,
    output_type=_COMMANDRESPONSE,
    options=None,
  ),
])

class CommandService(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _COMMANDSERVICE
class CommandService_Stub(CommandService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _COMMANDSERVICE

# @@protoc_insertion_point(module_scope)