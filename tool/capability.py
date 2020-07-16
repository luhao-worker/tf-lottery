from tensorflow.python.client import device_lib as _device_lib
local_device_protos = _device_lib.list_local_devices()
print(local_device_protos)