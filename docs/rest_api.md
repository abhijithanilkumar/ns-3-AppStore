# Module Details
Returns json data about a module app name.

- **URL**

	/backend/api/install/:name/:version

- **Method**

	```GET```

- **URL Params**

 	**Required:** 
 	
 	```name=[string]```
 
 	**Optional**
 
 	```version=[float]```

 - **Response:**
 	- Success Response 
 		- **Code:** 200
 		- **Content:**
 	```json
 	{
	    "name": "ns3-gym",
	    "app_type": "M",
	    "coderepo": "https://github.com/tkn-tub/ns3-gym",
	    "version": "0.1",
	    "ns": "3.29",
	    "bakefile_url": "/media/release_files/ns3-gym_fWyo1Cs_LaB4ehm.xml",
	    "message": "Module: ns3-gym with version: 0.1 found on the ns-3 AppStore."
	}
	```

	- Error Response
		- **Code:** 404
		- **Content:**
	```json
	{
	    "detail": "Not found."
	}
	```

	OR

	- **Code:** 429 Too Many Requests
	- **Content:**
	```json
	{
    	"detail": "Request was throttled. Expected available in 86399 seconds."
	}
	```


# Search API
Returns array of json with modules having substring as passed

- **URL**

	/backend/api/search/?q=[:name]

- **Method**

	```GET```

- **URL Params**

 	**Required:** 
 	
 	```name=[string]```


- Response:
 	- Success Response:
 		- **Code:** 200
 		- **Content:**
 	```json
 	[
	    {
	        "app": {
	            "name": "ns3-gym",
	            "title": "ns3-gym: OpenAI Gym integration",
	            "abstract": "The Playground for Reinforcement Learning in Networking Research"
	        },
	        "version": "0.2"
	    }
	]
	```

	- Error Response
		- **Code:** 404
		- **Content:**
	```json
	[ ]
	```

	OR

	- **Code:** 429 Too Many Requests
	- **Content:**
	```json
	{
    	"detail": "Request was throttled. Expected available in 86399 seconds."
	}
	```