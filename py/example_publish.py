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

	di = {
		"header": {
			"timestamp": 1234
		},
		"stations": [
			{
				"id": "1234",
				"timestamp": 1234,
				"dataList": [
					{
						"type": Type.PM10,
						"value": 123
					}
				]
			}
		]
	}
	
	try:
		m.registerToPublish(geospace)
	except MeshRPCException as e:
		print(e.getMessage())
		exit()
	
	for i in range(100):
		try:
			m.publish(geospace, di)
		except MeshRPCException as e:
			print(e.getMessage())
			exit()
		time.sleep(2)

if "__main__" == __name__:
    main(sys.argv)