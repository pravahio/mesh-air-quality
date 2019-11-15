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