## Air Quality standard SDK for Pravah

### Python 

Installation
```bash
pip install mesh-air-quality
```

Usage
> To use the given example you need to run pravah node on your local system. To know how to setup a node follow [these instructions](https://github.com/pravahio/go-mesh/blob/master/README.md).

```py
from mesh_air_quality.main import MeshAirQuality

geospace = [
   '/in/ncr',
]

def main():

   c = MeshAirQuality()

   feed = c.subscribe(geospace)

   for f, t in feed:
      print(f)

if '__main__' == __name__:
   main()
```

> By default `MeshAirQauality()` dials to `127.0.0.1:5555` which is the default port on which pravah local node listens on but you can change it by passing a string argument to the class constructor.