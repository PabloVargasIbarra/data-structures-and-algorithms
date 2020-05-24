# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def push(self, a):
        if self.__max_stack and a < self.__max_stack[-1]:
            self.__max_stack.append(self.__max_stack[-1])
        else:
            self.__max_stack.append(a)
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__max_stack.pop()

    def max_value(self):
        assert(len(self.__max_stack))
        return self.__max_stack[-1]


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def process(self, request):
        while self.finish_time_:
            if request.arrived_at >= self.finish_time_[0]:
                self.finish_time_.pop(0)
            else:
                break

        if len(self.finish_time_) >= self.size:
            return Response(True, -1)
        else:
            if len(self.finish_time_) == 0:
                self.finish_time_.append(request.arrived_at + request.time_to_process)
                return Response(False, request.arrived_at)
            else:
                last_finish_time = self.finish_time_[-1]
                if request.arrived_at >= last_finish_time:
                    self.finish_time_.append(request.arrived_at + request.time_to_process)
                    return Response(False, request.arrived_at)
                else:
                    self.finish_time_.append(last_finish_time + request.time_to_process)
                    return Response(False, last_finish_time)

    def process_requests(self, requests):
        responses = []
        for request in requests:
            responses.append(self.process(request))
        return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = buffer.process_requests(requests)
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
