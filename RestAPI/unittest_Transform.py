import os.path
import unittest
from unittest.mock import patch
import transformutil

config = {"format_unlist":["category"],"format_list_null":[]}
        
data_test_addlist =  {'category': {'coding': {'code': 'COMODIAG', 'display': 'Comorbidity', 'system': 'BCONN'}, 'text': 'Comorbidity'}}
data_test_flatten_json = {'data__severity__code': None, 'data__severity__display': None, 'data__severity__system': 'BCONN', 'data__body_site__code': None, 'data__body_site__display': None, 'data__body_site__system': 'BCONN', 'data__condition__asserted_date': '2014-10-01 13:48:03.657', 'data__condition__patient': '48-14-000019', 'data__condition__encounter': 'O48-14-000010', 'data__condition__clinical_status': 'active', 'data__condition__verification_status': 'unknown', 'data__condition__asserter': '048140334', 'data__codes__code__coding__code': 'B18.2', 'data__codes__code__coding__display': 'Chronic viral hepatitis C', 'data__codes__code__coding__system': 'ICD 10', 'data__codes__code__text': 'Chronic viral hepatitis C', 'data__codes__onset_datetime': '2014-10-01 00:00:00.0', 'data__codes__onset_duration': None, 'data__codes__onset_unit': None, 'data__category__0__category__coding__code': 'COMODIAG', 'data__category__0__category__coding__display': 'Comorbidity', 'data__category__0__category__coding__system': 'BCONN', 'data__category__0__category__text': 'Comorbidity', 'data__category__1__category__coding__code': 'diagnosis', 'data__category__1__category__coding__display': 'Diagnosis', 'data__category__1__category__coding__system': 'HL7', 'data__category__1__category__text': 'Diagnosis', 'data__identifier__system': 'BCONN', 'data__identifier__type': 'PatientProblemUID', 'data__identifier__use': 'official', 'data__identifier__value': '24', 'data__note__title': 'Comment', 'data__note__text': ''}
data_union_in = {'data': [{'severity': {'code': None, 'display': None, 'system': 'BCONN'}, 'body_site': {'code': None, 'display': None, 'system': 'BCONN'}, 'condition': {'asserted_date': '2014-10-01 13:00:29.783', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': None, 'verification_status': 'unknown', 'asserter': '048140334'}, 'codes': [{'code': {'coding': [{'code': 'Z00.0', 'display': 'General medical examination', 'system': 'ICD 10'}], 'text': 'General medical examination'}, 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'PRIMDIAG', 'display': 'Principal', 'system': 'BCONN'}], 'text': 'Principal'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}], 'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '13'}], 'note': [{'title': 'Comment', 'text': ''}]}]}
data_union_key = ('data', [{'severity': {'code': None, 'display': None, 'system': 'BCONN'}, 'body_site': {'code': None, 'display': None, 'system': 'BCONN'}, 'condition': {'asserted_date': '2014-10-01 13:20:35.55', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': 'active', 'verification_status': 'unknown', 'asserter': '048140334'}, 'codes': [{'code': {'coding': [{'code': 'I15.9', 'display': 'Secondary hypertension, unspecified', 'system': 'ICD 10'}], 'text': 'Secondary hypertension, unspecified'}, 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'PRIMDIAG', 'display': 'Principal', 'system': 'BCONN'}], 'text': 'Principal'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}], 'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '16'}], 'note': [{'title': 'Comment', 'text': ''}]}])
data_join_pre = {'data': [{'severity': {'code': None, 'display': None, 'system': 'BCONN'}, 'body_site': {'code': None, 'display': None, 'system': 'BCONN'}, 'condition': {'asserted_date': '2014-10-01 13:00:29.783', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': None, 'verification_status': 'unknown', 'asserter': '048140334'}, 'codes': [{'code': {'coding': [{'code': 'Z00.0', 'display': 'General medical examination', 'system': 'ICD 10'}], 'text': 'General medical examination'}, 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'PRIMDIAG', 'display': 'Principal', 'system': 'BCONN'}], 'text': 'Principal'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}], 'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '13'}], 'note': [{'title': 'Comment', 'text': ''}]}]}
data_join_current = {'data': [{'severity': {'code': None, 'display': None, 'system': 'BCONN'}, 'body_site': {'code': None, 'display': None, 'system': 'BCONN'}, 'condition': {'asserted_date': '2014-10-01 13:20:35.55', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': 'active', 'verification_status': 'unknown', 'asserter': '048140334'}, 'codes': [{'code': {'coding': [{'code': 'I15.9', 'display': 'Secondary hypertension, unspecified', 'system': 'ICD 10'}], 'text': 'Secondary hypertension, unspecified'}, 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'PRIMDIAG', 'display': 'Principal', 'system': 'BCONN'}], 'text': 'Principal'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}], 'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '16'}], 'note': [{'title': 'Comment', 'text': ''}]}]}


exp = {'category': {'coding': [{'code': 'COMODIAG', 'display': 'Comorbidity', 'system': 'BCONN'}], 'text': 'Comorbidity'}}
exp_json = {'data': [{'severity': [{'code': None, 'display': None, 'system': 'BCONN'}], 'body_site': [{'code': None, 'display': None, 'system': 'BCONN'}], 'condition': [{'asserted_date': '2014-10-01 13:48:03.657', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': 'active', 'verification_status': 'unknown', 'asserter': '048140334'}], 'codes': [{'code': [{'coding': [{'code': 'B18.2', 'display': 'Chronic viral hepatitis C', 'system': 'ICD 10'}], 'text': 'Chronic viral hepatitis C'}], 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'COMODIAG', 'display': 'Comorbidity', 'system': 'BCONN'}], 'text': 'Comorbidity'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}], 'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '24'}], 'note': [{'title': 'Comment', 'text': ''}]}]}
exp_union = {'data': [{'severity': {'code': None, 'display': None, 'system': 'BCONN'}, 'body_site': {'code': None, 'display': None, 'system': 'BCONN'}, 'condition': {'asserted_date': '2014-10-01 13:00:29.783', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': None, 'verification_status': 'unknown', 'asserter': '048140334'}, 'codes': [{'code': {'coding': [{'code': 'Z00.0', 'display': 'General medical examination', 'system': 'ICD 10'}], 'text': 'General medical examination'}, 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'PRIMDIAG', 'display': 'Principal', 'system': 'BCONN'}], 'text': 'Principal'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}],'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '13'}], 'note': [{'title': 'Comment', 'text': ''}]}, {'severity': {'code':None, 'display': None, 'system': 'BCONN'}, 'body_site': {'code': None, 'display': None, 'system': 'BCONN'}, 'condition': {'asserted_date': '2014-10-01 13:20:35.55', 'patient': '48-14-000019', 'encounter': 'O48-14-000010', 'clinical_status': 'active', 'verification_status': 'unknown', 'asserter': '048140334'}, 'codes': [{'code': {'coding': [{'code': 'I15.9', 'display': 'Secondary hypertension, unspecified', 'system': 'ICD 10'}], 'text': 'Secondary hypertension, unspecified'}, 'onset_datetime': '2014-10-01 00:00:00.0', 'onset_duration': None, 'onset_unit': None}], 'category': [{'category': {'coding': [{'code': 'PRIMDIAG', 'display': 'Principal', 'system': 'BCONN'}], 'text': 'Principal'}}, {'category': {'coding': [{'code': 'diagnosis', 'display': 'Diagnosis', 'system': 'HL7'}], 'text': 'Diagnosis'}}], 'identifier': [{'system': 'BCONN', 'type': 'PatientProblemUID', 'use': 'official', 'value': '16'}], 'note': [{'title': 'Comment', 'text': ''}]}]}

class Test_addlist(unittest.TestCase):
    
    def test_addlist(self):
        fn = transformutil.TransformUtil(config)
        # mock.return_value = exp
        # result = fn.addlist()
        result = fn.addlist(data_test_addlist)
        self.assertEqual(result, exp)

class Test_flatten_json(unittest.TestCase):

    def test_flatten_json(self):
        fn = transformutil.TransformUtil(config)
        result = fn.flatten_json(data_test_flatten_json)
        self.assertEqual(result,exp_json)

class Test_union(unittest.TestCase):
    
    def test_union(self):
        fn = transformutil.TransformUtil(config)
        result = fn.union(data_union_in,data_union_key)
        self.assertEqual(result,exp_union)

class Test_joinRow(unittest.TestCase):

    def test_join_row(self):
        fn = transformutil.TransformUtil(config)
        result = fn.join_row(data_join_pre,data_join_current)
        self.assertEqual(result,exp_union)

    def test_join_row_iswork(self):
        fn = transformutil.TransformUtil(config)
        result = fn.join_row(data_join_pre,data_join_current)
        self.assertFalse(result != exp_union)



if __name__ == '__main__':
    unittest.main()