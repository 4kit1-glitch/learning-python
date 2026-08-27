
data = {
    "cpu_model_name": "11th Gen Intel(R) Core(TM) i3-1115G4 @ 3.00GHz",
    "cores": 4,
    "usage": "27.45%",
    "load_avg": [
        "0.780",
        "0.980",
        "0.810"
    ],
    "uptime": [
        "134795.50",
        "2246",
        "37",
        "1",
        "0",
        "440675.99"
    ],
    "core_info": {
        "most_used_core": "cpu2",
        "least_used_core": "cpu3",
        "cores_usage": {
        "cpu3": "12.87%",
        "cpu2": "23.76%",
        "cpu1": "10.78%",
        "cpu0": "14.70%"
        },
        "cores_speed": "N/A"
  },
    "process_info": {
        "running_procs": "1",
        "total_procs": "1359"
    },
    "nixto": {
        "nancy": {
            "namibia": [
                10,
                20
            ],

        },
    },
    "country_info": [
        {
            "cameroon": {
                "population": 10
            } 
        }
    ]
}

rule1 = "usage"
rule2 = "load_avg.1"
rule3 = "core_info.cores_usage"
rule4 = "process_info.running_procs"
rule5 = "country_info.0.cameroon.population"

def disolve_data(data: dict, sub_source: any) -> any:
    """ breaks data subsections and nests """
    return data[sub_source]
def get_list_value(data: list, index: int):
    """ returns the specified item in the given index """
    return data[index]

def resolve(data: dict, source: str) -> any:
    """ gets required data provided by source"""
    objects = source.split(".")
    for obj in objects:
        if obj.isdigit():
            data = get_list_value(data, int(obj))
            continue
        data = disolve_data(data, obj)
    return data



def odds():
    return 6,7

a,b = odds()

print(a, b)

