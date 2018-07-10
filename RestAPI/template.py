

Patient = {
	"site":"b-connect",
	"sql":"select CASE WHEN rf_type.ValueCode = 'NATID' THEN 'NID' WHEN rf_type.ValueCode = 'PASID' THEN 'MRN' WHEN rf_type.ValueCode = 'PSPNM' THEN 'PPN' ELSE 'TMP' END as identifier__type,CASE WHEN pid.identifier IS NOT NULL OR LEN(pid.identifier) > 1 THEN pid.identifier ELSE NULL END identifier__value,'0'+SUBSTRING(pid.identifier,1, 2) identifier__facility,pid.activefrom identifier__start,pid.activeto 'identifier__end',NULL name__suffix,rf_title.description name__prefix,CASE WHEN p.middlename = '' THEN NULL ELSE p.middlename END name__middle_name,p.surname name__family_name,p.forename name__given_name,rf_commu.valuecode name__language,CASE WHEN addr.CITTYUID IS NOT NULL THEN ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.CITTYUID) ELSE NULL END address__district,isnull(addr.line1,'') + ' ' + isnull(addr.line2,'') + ' ' + isnull(addr.line3,'') + ' ' + isnull(addr.line4,'') address__line,CASE WHEN addr.STATEUID IS NOT NULL THEN ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.STATEUID) ELSE NULL END address__state_desc,CASE WHEN addr.CNTRYUID IS NOT NULL THEN ( SELECT TOP 1 ValueCode FROM dbo.ReferenceValue WHERE UID = addr.CNTRYUID) ELSE NULL END address__country,CASE WHEN addr.Pincode='999999' THEN NULL  ELSE addr.Pincode END address__zipcode,CASE WHEN addr.AREAUID IS NOT NULL THEN ( SELECT TOP 1 Description FROM ReferenceValue WHERE UID = addr.AREAUID) ELSE NULL END address__city,rf_commu.valuecode communication__commu_language,CASE WHEN rf_commu.statusflag = 'A' THEN 'True' ELSE 'False' END communication__commu_preferred,CASE WHEN poc.cntypuid = 1 THEN 'phone' WHEN poc.cntypuid = 2 THEN 'phone' WHEN poc.cntypuid = 3 THEN 'email' ELSE NULL END contact__system,RTRIM(LTRIM(REPLACE( poc.line1 , '-' , '' ))) contact__value,(SELECT TOP 1 description FROM referencevalue WHERE uid = p.VIPTPUID AND StatusFlag = 'A') extension__vip_type,CAST(p.uid AS VARCHAR) row_id,CAST(p.BirthDttm AS DATE) birth_date,CASE WHEN pdd.uid IS NOT NULL THEN 'True' ELSE 'False' END deceased,CASE WHEN p.SEXXXUID = '55631' THEN 'F' WHEN p.SEXXXUID = '55630' THEN 'M' ELSE NULL END gender,CASE WHEN(pdd.DeathDttm IS NOT NULL) AND(pdd.DeathTime IS NOT NULL) THEN(CAST(CONVERT(CHAR(10), pdd.DeathDttm, 126) + ' ' + SUBSTRING(CONVERT(CHAR(20), pdd.deathTime, 126), 12, 8) AS DATETIME)) ELSE NULL END deceased_datetime,rf_nation.ValueCode nationality, rf_reli.description religion,CASE WHEN p.MARRYUID IS NULL OR p.MARRYUID = '0' THEN 'Unknown' ELSE rf_marital.Description END marital_status,'BKH' organization__code_name,'048' organization__code_number,'N/A' organization__name from Patient p LEFT JOIN ReferenceValue rf_nation ON rf_nation.uid = p.NATNLUID LEFT JOIN PatientDeceasedDetail pdd ON pdd.patientuid = p.uid LEFT JOIN ReferenceValue rf_reli ON rf_reli.uid = p.RELGNUID LEFT JOIN referencevalue rf_marital ON rf_marital.uid = p.MARRYUID LEFT JOIN ReferenceValue rf_title ON rf_title.uid = p.titleuid LEFT JOIN ReferenceValue rf_commu ON rf_commu.uid = p.spokluid LEFT JOIN PatientID pid ON pid.patientuid = p.uid AND pid.statusflag = 'A'  LEFT JOIN ReferenceValue rf_type ON rf_type.uid = pid.pitypuid LEFT JOIN patientaddress addr ON addr.patientuid = p.uid LEFT JOIN PatientOtherContact poc ON poc.patientuid = p.uid AND poc.statusflag = 'A' AND poc.line1 <> ''  WHERE pid.identifier <> '' AND p.pasid = '48-14-000010'",
	"config":{
		"formatt_list":["code","route","text","organization"],
		"format_list_null":[]
	}
}

Practitioner = {
	"site":"b-connect",
	"sql":"SELECT CASE WHEN (ss_user.SSUSR_initials IS NOT NULL OR ss_user.SSUSR_initials <> '') AND (cp.code IS NOT NULL AND cp.code <> '') THEN 'employee_id+his_code' WHEN (ss_user.SSUSR_initials IS NOT NULL OR ss_user.SSUSR_initials <> '') AND (cp.code IS NULL AND cp.code = '') THEN 'employee_id'  WHEN (ss_user.SSUSR_initials IS NULL OR ss_user.SSUSR_initials = '') AND (cp.code IS NOT NULL AND cp.code <> '') THEN 'his_code'  ELSE 'employee_id'  END identifier__type,  CASE WHEN ss_user.SSUSR_initials IS NOT NULL AND (cp.code IS NOT NULL AND cp.code <> '') THEN ss_user.SSUSR_initials + '+' + cp.code  WHEN ss_user.SSUSR_initials IS NOT NULL AND (cp.code IS NULL AND cp.code = '') THEN ss_user.SSUSR_initials  WHEN ss_user.SSUSR_initials IS NULL AND (cp.code IS NOT NULL AND cp.code <> '') THEN cp.code  ELSE ss_user.SSUSR_initials  END identifier__value, CASE WHEN cp.statusflag = 'A' THEN 'True'  ELSE 'False'  END active__active, CASE WHEN cp.titleuid = '0' THEN NULL ELSE (SELECT TOP 1 valuecode FROM ReferenceValue WHERE uid = cp.titleuid) END name__title, LTRIM(RTRIM(cp.forename)) name__given_name, NULL name__middle_name, LTRIM(RTRIM(cp.surname)) name__family_name, s.uid AS specialty__specialty_code, s.name AS specialty__specialty_desc, CASE WHEN cp.statusflag = 'A' THEN 'True' ELSE 'False' END active, CASE WHEN cp.titleuid = '0' THEN NULL ELSE (SELECT TOP 1 valuecode FROM ReferenceValue WHERE uid = cp.titleuid)  END name__title, LTRIM(RTRIM(cp.forename)) name__given_name, NULL name__middle_name, LTRIM(RTRIM(cp.surname)) name__family_name, CAST(cp.activefrom AS DATETIME) period__start_date, CAST(cp.activeto AS DATETIME) period__end_date, rf_role.valuecode role__code, rf_role.Description role__desc, 'BCONN' qualification__system, cp.qualification qualification__code, cp.qualification qualification__display, cp.licenseno license, 'BCONN' location__enloc_id_loc_system, loc.Code location__enloc_id_loc_value, loc.Code location__enloc_id_loc_type, 'official' location__enloc_id_loc_use, 'HL7' location__enloc_phy_loc_system, 'wa' location__enloc_phy_loc_code, 'Ward' location__enloc_phy_loc_display, loc.Name location__enloc_loc_name, loc.Description location__enloc_loc_desc, loc.LocationURL location__enloc_loc_addr FROM Careprovider cp LEFT JOIN referencevalue rf_role ON rf_role.uid = cp.cptypuid  LEFT JOIN CareproviderSpecialty cps ON cps.careprovideruid = cp.uid AND cps.StatusFlag = 'A' LEFT JOIN Speciality s ON cps.SpecialtyUID = s.uid LEFT JOIN location loc ON loc.code = cp.middlename INNER JOIN Login login ON cp.uid = login.CareproviderUID LEFT JOIN ss_user ss_user ON login.loginname = ss_user.SSUSR_initials WHERE ss_user.SSUSR_initials IS NOT NULL AND login.StatusFlag = 'A' AND ss_user.SSUSR_initials = '048140361'",
	"config":{
		"formatt_list":["qualification"],
		"format_list_null":[]
	}
}


observation = {
    "site":"b-connect",
    "sql":"SELECT pvid.identifier data__observation__encounter , (select top 1 pasid from patient where uid = por.patientuid) data__observation__patient, CAST(por.uid AS VARCHAR) + '|' + CAST(item.uid AS VARCHAR) data__observation__order_result_item_uid, NULLIF(RTRIM(LTRIM(item.ResultValue)),'') data__observation__value, (SELECT TOP 1 rf.description FROM ReferenceValue rf WHERE rf.uid = item.UOMUID) data__observation__unit, NULLIF(RTRIM(LTRIM(item.ReferenceRange)), '') data__observation__value_range, CASE WHEN item.statusflag = 'A' THEN 'final'  WHEN item.statusflag = 'D' THEN 'cancelled'  ELSE NULL END data__observation__status, item.resultdttm data__observation__issued, NULL data__observation__interpretation, 'vital-signs' data__category__code, 'Vital Signs' data__category__text, CASE WHEN REPLACE(LOWER(resultitemname), ' ', '_') LIKE 'vision%' THEN LEFT(REPLACE(LOWER(resultitemname), ' ', '_'), 9)  ELSE REPLACE(LOWER(resultitemname), ' ', '_') END data__code__setcode, item.resultitemname data__code__set_desc, NULL data__code__testcode, NULL data__code__test_desc from PatientOrderResult por JOIN PatientOrderResultItem item ON item.ResultValue <> '' AND item.OrderResultItemUID = por.uid JOIN PatientVisitID pvid ON pvid.PatientVisitUID = por.PatientVisitUID WHERE por.OrderCatalogItemUID in (select uid from OrderCatalogitem where name like '%Vital Sign%')  AND por.PatientVisitUID = (SELECT TOP 1 PatientVisitUID FROM PatientVisitID where identifier = 'O48-15-015283')",
    "config":{
        "formatt_list":["observation"],
        "format_list_null":[]
    }
}

Laboratory = {
    "site":"b-connect",
    "sql":"SELECT 'data' data__category__code, 'data' data__category__text, reqitem.ItemCode data__code__setcode, reqitem.DisplyName data__code__set_desc, reitem.Code data__code__testcode, reitem.DisplyName data__code__test_desc, re.uid data__order_result_item_uid, recomp.ResultValue data__value, (SELECT TOP 1 rf.description FROM ReferenceValue rf WHERE rf.uid = reitem.UnitofMeasure) data__unit, recomp.ReferenceRange data__value_range, CASE WHEN re.statusflag = 'A' THEN 'final' ELSE 'registered' END data__status, re.ResultEnteredDttm data__issued, CASE WHEN recomp.IsAbnormal IN('L', 'H') THEN recomp.IsAbnormal WHEN recomp.IsAbnormal NOT IN('L', 'H') AND recomp.ReferenceRange <> '' THEN 'N' WHEN recomp.ResultValue = 'Negative' THEN 'NEG' WHEN recomp.ResultValue = 'Positive' THEN 'POS' ELSE '' END data__interpretion FROM Result re  LEFT JOIN RequestItem reqitem ON reqitem.ItemCode = re.RequestItemCode AND reqitem.StatusFlag = 'A'  LEFT JOIN ResultComponent recomp ON recomp.ResultUID = re.uid AND recomp.ResultItemName NOT IN('Formatted Result', 'Reference Range') AND recomp.StatusFlag = 'A'  JOIN ResultItem reitem ON recomp.ResultItemUID = reitem.uid AND reitem.StatusFlag = 'A'  JOIN Patient p ON p.uid = re.PatientUID  JOIN PatientVisit pv ON pv.uid = re.PatientVisitUID  JOIN PatientVisitID pvid ON pvid.PatientVisitUID = pv.uid  WHERE re.StatusFlag = 'A' AND len(re.RequestItemCode)=4  AND re.RequestItemCode NOT LIKE 'G%' AND re.Requestitemcode NOT LIKE 'R%' AND p.pasid = '48-14-000001' AND pvid.identifier = 'O48-15-015283'",
    "config":{
        "formatt_list":["category","code"],
        "format_list_null":[]
    }
}


Radiology ={
    "site":"b-connect",
    "sql":"SELECT 'imaging' data__Category__code, 'Imaging' data__Category__text, reqitem.ItemCode data__code__setcode, reqitem.DisplyName data__code__set_desc, reitem.Code data__code__testcode, reitem.DisplyName data__code__test_desc, re.uid data__order_result_item_uid, CAST(retext.TextualValue AS NVARCHAR(4000)) data__value, null data__unit, null data__value_range, CASE WHEN re.statusflag = 'A' THEN 'final' ELSE 'registered' END data__status, re.ResultEnteredDttm data__issued, null data__interpretation from Result re  LEFT JOIN RequestItem reqitem ON reqitem.ItemCode = re.RequestItemCode AND reqitem.StatusFlag = 'A' LEFT JOIN ResultComponent recomp ON recomp.ResultUID = re.uid AND recomp.ResultItemName NOT IN('Formatted Result', 'Reference Range')  AND recomp.StatusFlag = 'A' LEFT JOIN ResultTextual retext ON retext.ResultComponentUID = recomp.uid AND retext.StatusFlag = 'A' JOIN ResultItem reitem ON recomp.ResultItemUID = reitem.uid AND reitem.StatusFlag = 'A' JOIN Patient p ON p.uid = re.PatientUID  JOIN PatientVisit pv ON pv.uid = re.PatientVisitUID  JOIN PatientVisitID pvid ON pvid.PatientVisitUID = pv.uid WHERE re.StatusFlag = 'A'  AND re.RadiologistUID IS NOT NULL AND p.pasid = '48-14-000001' AND pvid.identifier = 'O48-15-015283'",
    "config":{
        "formatt_list":["Category","code"],
        "format_list_null":[]
    }
}

PhysicalExam = {
    "site":"b-connect",
    "sql":"select pid.identifier data__observation__encounter, p.pasid data__observation__patient, pex.uid data__observation__order_result_item_uid, CAST(pex.TextualValue AS NVARCHAR(4000)) data__observation__value, NULL data__observation__unit, NULL data__observation__value_range, NULL data__observation__status, pex.CWhen data__observation__issued, null data__observation__interpretation, 'exam' data__category__code, 'Exam' data__category__ext, 'physical_Exam' data__code__setcode, 'Physical Examination' data__code__set_desc, NULL data__code__testcode, NULL data__code__test_desc from BDMSASTEMRPhysicalExam pex LEFT JOIN Patient p on p.UID = pex.PatientUID  LEFT JOIN PatientVisitID pid on pid.PatientVisitUID = pex.PatientVisitUID  WHERE pid.identifier = 'O48-15-015283'",
    "config":{
        "formatt_list":["observation"],
        "format_list_null":[]
    }
}

Diagnosis = {
	"site":"b-connect",
	"template" : "",
	"sql":"SELECT (SELECT TOP 1 ReferenceValue.ValueCode FROM ReferenceValue WHERE ReferenceValue.UID = pprob.SEVTYUID AND ReferenceValue.StatusFlag='A') data__severity__code, (SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.SEVTYUID AND ReferenceValue.StatusFlag='A') data__severity__display,  'BCONN' data__severity__system, CASE WHEN LEN(LTRIM(RTRIM(pprob.BodySite))) > 0 THEN pprob.BodySite ELSE NULL END data__body_site__code, CASE WHEN LEN(LTRIM(RTRIM(pprob.BodySite))) > 0 THEN pprob.BodySite ELSE NULL END data__body_site__display, 'BCONN' data__body_site__system, pprob.RecordedDttm data__condition__asserted_date, p.pasid data__condition__patient, pvid.Identifier data__condition__encounter, CASE WHEN pprob.statusFlag = 'A' AND pprob.ClosureDttm IS NULL THEN 'active'  WHEN pprob.statusFlag = 'A' AND pprob.ClosureDttm IS NOT NULL THEN 'resolved'  ELSE NULL END data__condition__clinical_status, ISNULL((SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.CERTYUID AND ReferenceValue.StatusFlag='A'), 'unknown') data__condition__verification_status, (SELECT TOP 1 ss_user.SSUSR_initials identifier FROM careprovider cp  INNER JOIN Login login ON cp.uid = login.CareproviderUID  INNER JOIN ss_user ss_user ON login.loginname = ss_user.SSUSR_initials  WHERE cp.uid = pprob.RecordedBy) data__condition__asserter, prob.code data__codes__code__coding__code, prob.Name data__codes__code__coding__display, (SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = prob.CDTYPUID AND ReferenceValue.StatusFlag='A') data__codes__code__coding__system, prob.Name data__codes__code__text, pprob.OnsetDttm data__codes__onset_datetime, NULL data__codes__onset_duration, NULL data__codes__onset_unit, (SELECT TOP 1 ReferenceValue.ValueCode FROM ReferenceValue WHERE ReferenceValue.UID = pprob.DIAGTYPUID AND ReferenceValue.StatusFlag='A') data__category__0__category__coding__code, (SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.DIAGTYPUID AND ReferenceValue.StatusFlag='A') data__category__0__category__coding__display, 'BCONN' data__category__0__category__coding__system, (SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.DIAGTYPUID AND ReferenceValue.StatusFlag='A') data__category__0__category__text, 'diagnosis' data__category__1__category__coding__code, 'Diagnosis' data__category__1__category__coding__display, 'HL7' data__category__1__category__coding__system, 'Diagnosis' data__category__1__category__text, 'BCONN'  data__identifier__system, 'PatientProblemUID'  data__identifier__type, 'official'  data__identifier__use, CAST(pprob.uid AS VARCHAR(100))  data__identifier__value,'Comment' data__note__title,pprob.ClosureComments data__note__text FROM PatientProblem pprob  JOIN Problem prob ON pprob.ProblemUID = prob.uid  JOIN Patient p ON p.uid = pprob.PatientUID  JOIN PatientVisit pv ON pv.uid = pprob.PatientVisitUID  JOIN PatientVisitId pvid ON pvid.PatientVisitUID = pv.uid  WHERE p.pasid = '48-14-000019' AND pvid.Identifier = 'O48-14-000010'",
	"config":{
		"formatt_list":["severity","body_site","condition","code"],
		"format_list_null":["note"]
	}
}