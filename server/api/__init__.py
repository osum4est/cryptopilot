from socksync import socksync
from socksync.groups import SockSyncVariable, SockSyncFunction
from socksync.sockets import SockSyncSocket

var = SockSyncVariable[str]("message", "")


@SockSyncFunction.function(False)
def start_message(**kwargs):
    if "message" in kwargs:
        send_message(message=kwargs["message"])
        send_message(message=kwargs["message"])
        send_message(message="Done!")
        var.value = kwargs["message"]
        return 0
    else:
        send_message(message="Please provide a message!")
        return 1


@SockSyncFunction.function(True)
def send_message(**kwargs):
    pass


start_message_func = SockSyncFunction("start_message", start_message)
send_message_func = SockSyncFunction("send_message", send_message)


def new_connection(socket: SockSyncSocket):
    socket.register_variable(var)
    socket.register_function(start_message_func)
    socket.register_function(send_message_func)

    socket.subscribe(var)
    socket.subscribe(start_message_func)

# TODO: Test with single client to make sure it blocks
# TODO: Some form of timeout in case of bad client, other bad client precautions

socksync.on_new_connection = new_connection
