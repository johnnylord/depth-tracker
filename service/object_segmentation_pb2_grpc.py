# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import message.object_segmentation_pb2 as object__segmentation__pb2


class SegmentationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SegmentObjects = channel.unary_unary(
                '/godeye_service.object_segmentation.Segmentation/SegmentObjects',
                request_serializer=object__segmentation__pb2.SegmentRequest.SerializeToString,
                response_deserializer=object__segmentation__pb2.SegmentResponse.FromString,
                )


class SegmentationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SegmentObjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SegmentationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SegmentObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.SegmentObjects,
                    request_deserializer=object__segmentation__pb2.SegmentRequest.FromString,
                    response_serializer=object__segmentation__pb2.SegmentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'godeye_service.object_segmentation.Segmentation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Segmentation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SegmentObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/godeye_service.object_segmentation.Segmentation/SegmentObjects',
            object__segmentation__pb2.SegmentRequest.SerializeToString,
            object__segmentation__pb2.SegmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
