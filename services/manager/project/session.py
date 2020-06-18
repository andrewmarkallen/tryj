import docker


class Session:
    """Represents a docker session"""
    client = docker.from_env()

    def __init__(self, uuid):
        self.id = uuid
        self.socket = None
        self.create_resources()

    def create_resources(self):
        try:
            self.container = self.client.containers.create(
                'sandbox:1.0',
                command='sleep 10000',
                auto_remove=False,
                name=str(self.id)
            )
            self.container.start()
            _, self.socket = self.container.exec_run(
                'ijconsole',
                stdout=True,
                stdin=True,
                socket=True
            )
        except Exception as e:
            print(e)

    def write(self, data):
        print(data)
        self.socket._sock.sendall(bytes(data, 'utf-8'))
        print('sent')
        response = str(self.socket._sock.recv(16384))
        print(response)
        return response
