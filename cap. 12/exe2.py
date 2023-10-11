import json

"""
Exemplo de como o json funciona
"""

jsonString = '''{
    "arrayOfNums":[
        {"number": 0}, {"number": 1}, {"number":  2}
    ],
    "arrayOfFruits":[
        {"fruit": "apple"}, {"fruit": "banana"}, {"fruit": "pear"}
    ]
}'''

data = json.loads(jsonString)

print(data['arrayOfNums'])
print(data['arrayOfNums'][1])
print(data['arrayOfNums'][1]['number'] + data['arrayOfNums'][2]['number'])
print(data['arrayOfFruits'][2]['fruit'])
