from protos import test_pb2
import time

class MathHandler(object):

    def surface(self, request, context):
        width = request.width
        height = request.height
        # for i in range(1000):
        #     continue
        print(f"surface(): {width=}, {height=}")
        return test_pb2.surfaceReply(res=width*height)

    def volume(self, width, height):
        for i in range(1000000):
            continue
        return width * height
