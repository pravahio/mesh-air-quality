## Air Quality SDK for Pravah

### Python 

Installation
```bash
pip install mesh-air-quality
```

Usage
> To use the given examples you need to run pravah node on your local system. To know how to setup a node follow [these instructions](https://github.com/pravahio/go-mesh/blob/master/README.md).

Subscriber
```py
from mesh_air_quality.main import MeshAirQuality

geospace = [
   '/in/ncr',
]

def main():

   # Create a pravah client which support air quality standard.
   c = MeshAirQuality()

   # Subscribe to a set of geospace from which you want to consme data.
   feed = c.subscribe(geospace)

   # Iterating over `feed` is a blocking call.
   # `feed` will yield (message, channel) as and when a message arrives in the system.
   for m, c in feed:
      print(m)

if '__main__' == __name__:
   main()
```

Publisher
```py
import time 
import sys

from mesh_air_quality.main import *
from mesh_air_quality.defaults import Type
from mesh_air_quality import MeshRPCException

geospace = [
   '/in/ncr'
]

def main(argv):
   m = MeshAirQuality()

# Prepare data according to the air quality data standard.
# https://github.com/pravahio/mesh-air-quality/blob/master/air-quality.proto
   di = {
      "header": {
         "timestamp": 1573798217
      },
      "stations": [
         {
            "id": "IN/26353",
            "timestamp": 1573799342,
            "dataList": [
               {
                  "type": Type.PM10,
                  "value": 565
               }
            ]
         }
      ]
   }

   try:
      # Every publisher needs to register itself.
      # This step is needed for other subscribers to start accepting your data stream.
      m.registerToPublish(geospace)
   except MeshRPCException as e:
      print(e.getMessage())
      exit()

   # Publishing same dummy data 100 times. 
   for i in range(100):
      try:
         # Publish the data to the set of geospaces.
         # same data `di` is published to all sets within `geospace`
         m.publish(geospace, di)
      except MeshRPCException as e:
         print(e.getMessage())
         exit()
      time.sleep(2)

if "__main__" == __name__:
   main(sys.argv)
```

Here is the complete code to setup an [air quality publisher](py/example_publish.py).

> By default `MeshAirQauality()` dials to `127.0.0.1:5555` which is the default port on which pravah local node listens on but you can change it by passing a string argument to the class constructor.

