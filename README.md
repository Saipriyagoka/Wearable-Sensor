# Wearable-Sensor

# Endpoints:
# vitals_input:
Method: POST

Sample input:
{
    "user_id": "saipriya",
    "timestamp": 1649144912,
    "heart_rate": 45,
    "respiration_rate": 18,
    "activity": 3
}

Sample Output:

Succes Status: 'Generated Succesfully'

Failed Status: 'Failed generating the values'


# vitals_output:
Method: GET

Sample input: (query Params)
"user_id": "saipriya"
"aggregate_min_level":  15/30/45/60

Sample Output:

Success output: 
{
    "avg_hr": {
        "0": 80.13381454747362,
        "1": 79.96335369239311
    },
    "avg_rr": {
        "0": 18.434203220433094,
        "1": 18.39200444197668
    },
    "max_hr": {
        "0": 100,
        "1": 100
    },
    "max_rr": {
        "0": 25,
        "1": 25
    },
    "min_hr": {
        "0": 45,
        "1": 60
    },
    "min_rr": {
        "0": 12,
        "1": 12
    },
    "seg_end": {
        "0": 1649146712,
        "1": 1649148512
    },
    "seg_start": {
        "0": 1649144912,
        "1": 1649146712
    },
    "user_id": {
        "0": "saipriya",
        "1": "saipriya"
    }
}

Failed Status: 'Not Processed values'
