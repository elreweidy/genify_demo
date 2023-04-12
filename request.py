import requests
import json

url = "http://localhost:5000/predict"

# Sample data queries
sample1 = {"fecha_dato": ["2016-06-28", "2016-06-28"],
        "ncodpers": [15889, 1170544],
        "ind_empleado": ["F", "N"],
        "pais_residencia": ["ES", "ES"],
        "sexo": ["V", "H"],
        "age": [56, 36],
        "fecha_alta": ["1995-01-16", "2013-08-28"],
        "ind_nuevo": [0, 0],
        "antiguedad": [256, 34],
        "indrel": [1, 1],
        "ult_fec_cli_1t": ["", ""],
        "indrel_1mes": ["1", "1"],
        "tiprel_1mes": ["A", "I"],
        "indresi": ["S", "S"],
        "indext": ["N", "N"],
        "conyuemp": ["N", ""],
        "canal_entrada": ["KAT", "KAT"],
        "indfall": [0, 0],
        "tipodom": [1, 1],
        "cod_prov": [28, 3],
        "nomprov": ["MADRID", "ALICANTE"],
        "ind_actividad_cliente": [1, 0],
        "renta": [326124.90, None],
        "segmento": ["01 - TOP", "02 - PARTICULARES"]
       }

sample2 = {
    "fecha_dato": ["2016-06-28", "2016-06-28"],
    "ncodpers": [1170545, 1170547],
    "ind_empleado": ["N", "N"],
    "pais_residencia": ["ES", "ES"],
    "sexo": ["V", "H"],
    "age": [22, 22],
    "fecha_alta": ["2013-08-28", "2013-08-28"],
    "ind_nuevo": [0, 0],
    "antiguedad": [34, 34],
    "indrel": [1, 1],
    "ult_fec_cli_1t": ["", ""],
    "indrel_1mes": ["1", "1"],
    "tiprel_1mes": ["A", "I"],
    "indresi": ["S", "S"],
    "indext": ["N", "N"],
    "conyuemp": ["", ""],
    "canal_entrada": ["KHE", "KHE"],
    "indfall": [0, 0],
    "tipodom": [1, 1],
    "cod_prov": [15, 8],
    "nomprov": ["CORUÑA, A", "BARCELONA"],
    "ind_actividad_cliente": [1, 1],
    "renta": [None, 148402.98],
    "segmento": ["03 - UNIVERSITARIO", "03 - UNIVERSITARIO"]
}

sample3 = {
    "fecha_dato": ["2016-06-28", "2016-06-28"],
    "ncodpers": [1170544, 15889],
    "ind_empleado": ["N", "F"],
    "pais_residencia": ["ES", "ES"],
    "sexo": ["H", "V"],
    "age": [36, 56],
    "fecha_alta": ["2013-08-28", "1995-01-16"],
    "ind_nuevo": [0, 0],
    "antiguedad": [34, 256],
    "indrel": [1, 1],
    "ult_fec_cli_1t": ["", ""],
    "indrel_1mes": ["1", "1"],
    "tiprel_1mes": ["I", "A"],
    "indresi": ["S", "N"],
    "indext": ["N", "N"],
    "conyuemp": ["", "N"],
    "canal_entrada": ["KAT", "KAT"],
    "indfall": [0, 0],
    "tipodom": [1, 1],
    "cod_prov": [3, 28],
    "nomprov": ["ALICANTE", "MADRID"],
    "ind_actividad_cliente": [0, 1],
    "renta": [None, 326124.90],
    "segmento": ["02 - PARTICULARES", "01 - TOP"]
}

# Convert data to JSON format
data = json.dumps(sample3)
print(data)
# Send POST request
response = requests.post(url, data=data, headers={"Content-Type": "application/json"})

# Print response
print(response.json())
