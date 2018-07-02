import unittest
from random import Random
import json
from jsonschema import validate
from Tranformdata import union, join_row, get_raw_patient_json
import json

with open('data/Practitioner.json', 'r') as f:
        schema_data1 = f.read()
in_data = json.loads(schema_data1)
with open('data/out_Practitioner.json', 'r') as f:
        schema_data2= f.read()
data = json.loads(schema_data2)
with open('data/schema_Practitioner.json', 'r') as f:
        schema_data3= f.read()
schemaa = json.loads(schema_data3)

class Test_Tranformdata(unittest.TestCase):
        
    #     # print(data)
        def test_assertEqual(self):
            act = get_raw_patient_json(in_data)
            self.assertEqual(data, act)

        def test_validate(self):
            act = get_raw_patient_json(in_data)
            validate(act, schemaa)

if __name__ == '__main__':
    unittest.main()