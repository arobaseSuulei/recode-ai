def get_meteo(city:str)->int:
    """ get a weather of a city """
    return 36

GET_WEATHER_TOOL={
    "type":"function",
    "name":"meteo",
    "description":"Get the weather of a city"
    "parameters":{
        "type":"object",
        "properties":{
            "city":{
                "type":"string",
                "description":"the name of the city",
            }
        },
        "required":["city"],
        "additionalProperties":False
    }
}