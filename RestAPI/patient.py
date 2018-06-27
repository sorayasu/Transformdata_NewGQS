from models import patient, patientattachment
from collections import OrderedDict
from confighelper import HMSConfigHelper
from sitefinder import SiteFinder

try:
    hms_config = HMSConfigHelper.get_instance()
    source = hms_config.get_hms_settings('settings')['source']
    finder = SiteFinder()
    facility_code = hms_config.get_hms_settings('settings', 'facility_code')
    facility = finder.find(key="bu", value=facility_code)

except Exception as e:
    raise Exception('Could not load hms setting.json')
if source == 'BCONN':
    
    template = {
        "Patient": {
            "identifier": [{
                "type": "CASE WHEN rf_type.ValueCode = 'NATID' THEN 'NID' WHEN rf_type.ValueCode = 'PASID' THEN 'MRN' WHEN rf_type.ValueCode = 'PSPNM' THEN 'PPN' ELSE 'TMP' END type",
                "value": "CASE WHEN pid.identifier IS NOT NULL OR LEN(pid.identifier) > 1 THEN pid.identifier ELSE NULL END 'value'",
                "facility": "'{0}' facility".format(hms_config.get_hms_settings('settings', 'facility_code')),
                "start": "pid.activefrom",
                "end": "pid.activeto"
            }],
            "name": [{
                "suffix": "NULL suffix",
                "prefix": "rf_title.description",
                "middle_name": "CASE WHEN p.middlename = '' THEN NULL ELSE p.middlename END middle_name",
                "family_name": "p.surname family_name",
                "given_name": "p.forename given_name",
                "language": "rf_commu.valuecode"
            }],
            "address": [{
                "district": "CASE WHEN addr.CITTYUID IS NOT NULL THEN ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.CITTYUID) ELSE NULL END district",
                "line": "isnull(addr.line1,'') + ' ' + isnull(addr.line2,'') + ' ' + isnull(addr.line3,'') + ' ' + isnull(addr.line4,'') line",
                "state": "CASE WHEN addr.STATEUID IS NOT NULL THEN ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.STATEUID) ELSE NULL END state_desc",
                "country": "CASE WHEN addr.CNTRYUID IS NOT NULL THEN ( SELECT TOP 1 ValueCode FROM dbo.ReferenceValue WHERE UID = addr.CNTRYUID) ELSE NULL END country",
                "postcode": "CASE WHEN addr.Pincode='999999' THEN NULL ELSE addr.Pincode END zipcode",
                "city": "CASE WHEN addr.AREAUID IS NOT NULL THEN ( SELECT TOP 1 Description FROM ReferenceValue WHERE UID = addr.AREAUID) ELSE NULL END city"
            }],
            "communication": [{
                "language": "rf_commu.valuecode commu_language",
                "preferred": "CASE WHEN rf_commu.statusflag = 'A' THEN 'True' ELSE 'False' END preferred"
            }],
            "contact": [{
                "system": "CASE WHEN poc.cntypuid = 1 THEN 'phone' WHEN poc.cntypuid = 2 THEN 'phone' WHEN poc.cntypuid = 3 THEN 'email' ELSE NULL END contact_system",
                "value": "RTRIM(LTRIM(REPLACE( poc.line1 , '-' , '' ))) contact_value"
            }],
            "extension": [{
                "vip_type": "(SELECT TOP 1 description FROM referencevalue WHERE uid = p.VIPTPUID AND StatusFlag = 'A') vip_type"
                # "registration_date": "p.registrationdttm"
            }],
            "row_id": "'{0}-' + CAST(p.uid AS VARCHAR) row_id".format(facility['bu'][1:3]),
            "birth_date": "CAST(p.BirthDttm AS DATE) birth_date",
            "deceased": "CASE WHEN pdd.uid IS NOT NULL THEN 'True' ELSE 'False' END deceased",
            "gender": "CASE WHEN p.SEXXXUID = '55631' THEN 'F' WHEN p.SEXXXUID = '55630' THEN 'M' ELSE NULL END gender",
            "deceased_datetime": "CASE WHEN(pdd.DeathDttm IS NOT NULL) AND(pdd.DeathTime IS NOT NULL) THEN(CAST(CONVERT(CHAR(10), pdd.DeathDttm, 126) + ' ' + SUBSTRING(CONVERT(CHAR(20), pdd.deathTime, 126), 12, 8) AS DATETIME)) ELSE NULL END deceased_datetime ",
            "nationality": "rf_nation.ValueCode nationality",
            "religion": "rf_reli.description religion",
            "marital_status": "CASE WHEN p.MARRYUID IS NULL OR p.MARRYUID = '0' THEN 'Unknown' ELSE rf_marital.Description END marital_status",
            "organization": {
                "code_number": "'{0}' org_code_number".format(facility['bu']),
                "code_name": "'{0}' org_code_name".format(facility['site']),
                "name": "'{0}' org_name".format(facility['name'])
            }
        },
        "PatientImage": {
            "content_type": "'image/jpeg' content_type",
            #"image_hex": "SUBSTRING(master.dbo.fn_varbintohexstr(pi.imagecontent), 3, 9999999999) image_hex",
            "image_hex": "pi.imagecontent image_hex",
            #"date": "pi.MWhen",
            "patient": "p.pasid"
        }
    }

    gw_models = {
        "Patient": OrderedDict((
            ("organization", patient.PatientOrganization),
            ("domain", patient.Patient),
            ("identifier", patient.PatientIdentifier),
            ("name", patient.PatientName),
            ("address", patient.PatientAddress),
            ("communication", patient.PatientCommunication),
            ("contact", patient.PatientContact),
            ("extension", patient.PatientExtension)
        )),
        "PatientImage": OrderedDict((
            ("domain", patientattachment.PatientAttachment),
        ))
    }

    models = {
        "Patient": {
            "template": template['Patient'],
            "table": "Patient p " +
                        "LEFT JOIN ReferenceValue rf_nation ON rf_nation.uid = p.NATNLUID " +
                        "LEFT JOIN PatientDeceasedDetail pdd ON pdd.patientuid = p.uid " +
                        "LEFT JOIN ReferenceValue rf_reli ON rf_reli.uid = p.RELGNUID " +
                        "LEFT JOIN referencevalue rf_marital ON rf_marital.uid = p.MARRYUID " +
                        "LEFT JOIN ReferenceValue rf_title ON rf_title.uid = p.titleuid " +
                        "LEFT JOIN ReferenceValue rf_commu ON rf_commu.uid = p.spokluid " +
                        "LEFT JOIN PatientID pid ON pid.patientuid = p.uid AND pid.statusflag = 'A' " +
                        "LEFT JOIN ReferenceValue rf_type ON rf_type.uid = pid.pitypuid " +
                        "LEFT JOIN patientaddress addr ON addr.patientuid = p.uid " +
                        "LEFT JOIN PatientOtherContact poc ON poc.patientuid = p.uid AND poc.statusflag = 'A' AND poc.line1 <> '' " +
                    "WHERE pid.identifier <> '' AND p.pasid = '{0}';",
            "gw_models": gw_models['Patient'],
            "adapter": "his_b-connect",
        },
        "PatientImage": {
            "template": template['PatientImage'],
            "table": "PatientImage pi " +
                "INNER JOIN Patient p ON pi.PatientUID = p.UID " +
                "WHERE pi.StatusFlag = 'A' AND p.pasid = '{0}'",
            "gw_models": gw_models['PatientImage'],
            "adapter": "his_b-connect",
        }
    }



template_patient_bi = {
    "Patient_BI": {

        "organization": {
            "code_name": "39",
            "code_number": "40",
            "name": "41"
        },

        "patient": {
            "row_id": "31",
            "birth_date": "32",
            "deceased": "33",
            "gender": "34",
            "deceased_datetime": "35",
            "nationality": "36",
            "religion": "37",
            "marital_status": "38"
        },

        "identifier": [{
            "type": "1",
            "value": "2",
            "facility": "3",
            "start": "4",
            "end": "5"
        }, {
            "type": "6",
            "value": "7",
            "facility": "8",
            "start": "9",
            "end": "10"
        }, {
            "type": "11",
            "value": "12",
            "facility": "13",
            "start": "14",
            "end": "15"
        }],
        "name": [{
            "suffix": "16",
            "prefix": "17",
            "middle_name": "18",
            "family_name": "19",
            "given_name": "20"
        }, {
            "suffix": "43",
            "prefix": "44",
            "middle_name": "45",
            "family_name": "46",
            "given_name": "47"
        }],
        "address": {
            "district": "21",
            "line": "22",
            "state": "23",
            "country": "24",
            "postcode": "25",
            "city": "26"
        },
        "communication": [{
            "language": "27",
            "preferred": "28"
        }],

        "extension": {
            "vip_type": "29"
        },
        "patientrowid": "42"
    }
}

config = {
    "Default": {
        "is_reduce": False
    }
}

models_patient_bi = {
    "Patient_BI": {
        "template": template_patient_bi['Patient_BI'],
        "table": "FROM patient_master_bmc t WHERE activeStatus <> 'N'",
        "gw_models": OrderedDict((
            ("patient", patient.Patient),
            ("identifier", patient.PatientIdentifier),
            ("name", patient.PatientName),
            ("address", patient.PatientAddress),
            ("communication", patient.PatientCommunication),
            ("contact", patient.PatientContact),
            ("extension", patient.PatientExtension)
        )),
        "config": config['Default'],
        "adapter": "his_bi"
    }
}
