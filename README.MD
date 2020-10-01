# Project Title

REST API for a metallics optimization service

## Getting Started

Fork or copy project folders, naviagate to root folder from where you can see app folder and run command **flask** run to run on local machine

To run web services on IP or DNS run below command
**flask run -h 0.0.0.0**

By default flask run web services on port 5000, to run services on different port execute command as below
**flask run -h 0.0.0.0 -p <port>**

### Prerequisites


* python3.7
* SQL database     (mssql server preferred)

### Installing

you need to initilazed for the database for first timefirst time. Please follow the steps below,
1. Navigate to root directory -> SMS-Project
2. update database and other configuration in configuration file placed in app/configs/production.cfg
3. download python library: pip install -r requirements.txt
2. Run command-> flask init-db

* This will create all the required tables in to database. If no database is configured, default configuration will run app sqlite db.

* Project installation not required.

### REST ENDPOINTS

1. http://<hostname:port>/chemical-elements
    * method: GET
    * Parameters: None
    * success: 200, will retrun list of all elements
2. http://<hostname:port>/commodity/<int:id>'
    * methods: GET, POST
    * Parameter = id
    * Headers:  
        >Key: Authorization   
        Value: JWT <JWT Token>  
    * Body: {  
        >"name": "some raw metals",  
        "inventory": 328.09,  
        "price": 12.05 
        }
3. http://<hostname:port>/chemical-composition
    * methods: POST
    * Headers:  
        Key: Authorization  
        Value: JWT <JWT Token>  
    * Boy:{  
       > "commodity_id": integer  
        "element_id": integer  
        "percentage": integer  
    }


4. http://<hostname:port>/chemical-composition/<int:id>
    * method: DELETE
    * Parameters:   
        >name: commodity_id  
        type: integer  
    * Headers:  
        >Key: Authorization  
        Value: JWT <JWT Token>

5. http://<hostname:port>/auth
    * method: POST
    * parameters: None  
    * Body:
       > "username": "dev"  
        "password": "dev@123"





## Authors

 Sudhanshu Kumar -  sudbkumar@gmail.com
