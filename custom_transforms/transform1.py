import sys
from maltego_trx.entities import IPAddress
from maltego_trx.maltego import UIM_TYPES, MaltegoMsg, MaltegoTransform

class CustomTransform(MaltegoTransform):
    def __init__(self):
        super().__init__()

    def do_transform(self, request, response):
        # Example: Add hardcoded IP addresses as output
        response.addEntity(IPAddress, "192.168.0.1")
        response.addEntity(IPAddress, "8.8.8.8")
        return response

if __name__ == "__main__":
    CustomTransform().run(sys.argv)

