import time
import threading

from mesh_air_quality.main import MeshAirQuality

geospace = [
    '/in/ncr'
]

def main():

    c = MeshAirQuality('rpc.pravah.io:5555')

    feed = c.subscribe(geospace)

    threading.Thread(target=fetch_data, args=(feed,)).start()
    
    """ time.sleep(4)
    print('unsub')

    c.unsubscribe(geospace) """

def fetch_data(feed):
    for m, c in feed:
        #pass
        print(m)

if '__main__' == __name__:
    main()