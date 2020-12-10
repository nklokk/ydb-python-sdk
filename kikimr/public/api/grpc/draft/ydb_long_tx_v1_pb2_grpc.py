# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos.draft import ydb_long_tx_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2


class LongTxServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.BeginTx = channel.unary_unary(
        '/Ydb.LongTx.V1.LongTxService/BeginTx',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.BeginTxRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.BeginTxResponse.FromString,
        )
    self.CommitTx = channel.unary_unary(
        '/Ydb.LongTx.V1.LongTxService/CommitTx',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.CommitTxRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.CommitTxResponse.FromString,
        )
    self.Write = channel.unary_unary(
        '/Ydb.LongTx.V1.LongTxService/Write',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.WriteRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.WriteResponse.FromString,
        )
    self.Read = channel.unary_unary(
        '/Ydb.LongTx.V1.LongTxService/Read',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.ReadRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.ReadResponse.FromString,
        )


class LongTxServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def BeginTx(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CommitTx(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Write(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    """rpc ResolveNodes(ResolveNodesRequest) returns (stream ResolveNodesResponse);
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LongTxServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'BeginTx': grpc.unary_unary_rpc_method_handler(
          servicer.BeginTx,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.BeginTxRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.BeginTxResponse.SerializeToString,
      ),
      'CommitTx': grpc.unary_unary_rpc_method_handler(
          servicer.CommitTx,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.CommitTxRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.CommitTxResponse.SerializeToString,
      ),
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.WriteRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.WriteResponse.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.ReadRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_ydb__long__tx__pb2.ReadResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.LongTx.V1.LongTxService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
