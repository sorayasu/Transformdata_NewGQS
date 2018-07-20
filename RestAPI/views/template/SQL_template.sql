#patient
select
    CASE WHEN rf_type.ValueCode = 'NATID' THEN 'NID' 
         WHEN rf_type.ValueCode = 'PASID' THEN 'MRN' 
         WHEN rf_type.ValueCode = 'PSPNM' THEN 'PPN' 
         ELSE 'TMP' 
    END as identifier__type,
    CASE WHEN pid.identifier IS NOT NULL OR LEN(pid.identifier) > 1 THEN pid.identifier 
         ELSE NULL 
    END identifier__value,
    '0'+SUBSTRING(pid.identifier,1, 2) identifier__facility,
    pid.activefrom identifier__start,
    pid.activeto 'identifier__end',
    NULL name__suffix,
    rf_title.description name__prefix,
    CASE WHEN p.middlename = '' THEN NULL 
         ELSE p.middlename 
    END name__middle_name,
    p.surname name__family_name,
    p.forename name__given_name,
    rf_commu.valuecode name__language,
    CASE WHEN addr.CITTYUID IS NOT NULL THEN 
        ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.CITTYUID) 
         ELSE NULL 
    END address__district,
    isnull(addr.line1,'') + ' ' + isnull(addr.line2,'') + ' ' + isnull(addr.line3,'') + ' ' + isnull(addr.line4,'') address__line,
    CASE WHEN addr.STATEUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.STATEUID) 
         ELSE NULL 
    END address__state_desc,
    CASE WHEN addr.CNTRYUID IS NOT NULL THEN 
         ( SELECT TOP 1 ValueCode FROM dbo.ReferenceValue WHERE UID = addr.CNTRYUID) 
         ELSE NULL 
    END address__country,
    CASE WHEN addr.Pincode='999999' THEN NULL 
         ELSE addr.Pincode 
    END address__zipcode,
    CASE WHEN addr.AREAUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM ReferenceValue WHERE UID = addr.AREAUID) 
         ELSE NULL 
    END address__city,
    rf_commu.valuecode communication__commu_language,
    CASE WHEN rf_commu.statusflag = 'A' THEN 'True' 
         ELSE 'False' 
    END communication__commu_preferred,
    CASE WHEN poc.cntypuid = 1 THEN 'phone' 
         WHEN poc.cntypuid = 2 THEN 'phone' 
         WHEN poc.cntypuid = 3 THEN 'email' 
         ELSE NULL 
    END contact__system,
    RTRIM(LTRIM(REPLACE( poc.line1 , '-' , '' ))) contact__value,
    (SELECT TOP 1 description FROM referencevalue WHERE uid = p.VIPTPUID AND StatusFlag = 'A') extension__vip_type,
    CAST(p.uid AS VARCHAR) row_id,
    CAST(p.BirthDttm AS DATE) birth_date,
    CASE WHEN pdd.uid IS NOT NULL THEN 'True' 
         ELSE 'False' 
    END deceased,
    CASE WHEN p.SEXXXUID = '55631' THEN 'F' WHEN p.SEXXXUID = '55630' THEN 'M' 
         ELSE NULL 
    END gender,
    CASE WHEN(pdd.DeathDttm IS NOT NULL) AND(pdd.DeathTime IS NOT NULL) THEN(CAST(CONVERT(CHAR(10), pdd.DeathDttm, 126) + ' ' + SUBSTRING(CONVERT(CHAR(20), pdd.deathTime, 126), 12, 8) AS DATETIME)) 
         ELSE NULL 
    END deceased_datetime,
    rf_nation.ValueCode nationality,
    rf_reli.description religion,
    CASE WHEN p.MARRYUID IS NULL OR p.MARRYUID = '0' THEN 'Unknown' 
         ELSE rf_marital.Description 
    END marital_status,
    'BKH' organization__code_name,
	'048' organization__code_number,
    'N/A' organization__name
from Patient p
    LEFT JOIN ReferenceValue rf_nation ON rf_nation.uid = p.NATNLUID
    LEFT JOIN PatientDeceasedDetail pdd ON pdd.patientuid = p.uid
    LEFT JOIN ReferenceValue rf_reli ON rf_reli.uid = p.RELGNUID 
    LEFT JOIN referencevalue rf_marital ON rf_marital.uid = p.MARRYUID 
    LEFT JOIN ReferenceValue rf_title ON rf_title.uid = p.titleuid
    LEFT JOIN ReferenceValue rf_commu ON rf_commu.uid = p.spokluid
    LEFT JOIN PatientID pid ON pid.patientuid = p.uid AND pid.statusflag = 'A' 
    LEFT JOIN ReferenceValue rf_type ON rf_type.uid = pid.pitypuid 
    LEFT JOIN patientaddress addr ON addr.patientuid = p.uid 
    LEFT JOIN PatientOtherContact poc ON poc.patientuid = p.uid AND poc.statusflag = 'A' AND poc.line1 <> '' 
WHERE pid.identifier <> '' AND p.pasid = '48-14-000010'

#Practitioner
SELECT          
	CASE WHEN (ss_user.SSUSR_initials IS NOT NULL OR ss_user.SSUSR_initials <> '') AND (cp.code IS NOT NULL AND cp.code <> '') THEN 'employee_id+his_code'
		 WHEN (ss_user.SSUSR_initials IS NOT NULL OR ss_user.SSUSR_initials <> '') AND (cp.code IS NULL AND cp.code = '') THEN 'employee_id' 
		 WHEN (ss_user.SSUSR_initials IS NULL OR ss_user.SSUSR_initials = '') AND (cp.code IS NOT NULL AND cp.code <> '') THEN 'his_code' 
		 ELSE 'employee_id' 
		 END identifier__type, 
    CASE WHEN ss_user.SSUSR_initials IS NOT NULL AND (cp.code IS NOT NULL AND cp.code <> '') THEN ss_user.SSUSR_initials + '+' + cp.code 
    	 WHEN ss_user.SSUSR_initials IS NOT NULL AND (cp.code IS NULL AND cp.code = '') THEN ss_user.SSUSR_initials 
    	 WHEN ss_user.SSUSR_initials IS NULL AND (cp.code IS NOT NULL AND cp.code <> '') THEN cp.code 
     	 ELSE ss_user.SSUSR_initials 
    END identifier__value,
    CASE WHEN cp.statusflag = 'A' THEN 'True' 
         ELSE 'False' 
    END active__active,
    CASE WHEN cp.titleuid = '0' THEN NULL ELSE (SELECT TOP 1 valuecode FROM ReferenceValue WHERE uid = cp.titleuid) END name__title,
    LTRIM(RTRIM(cp.forename)) name__given_name,
    NULL name__middle_name,
    LTRIM(RTRIM(cp.surname)) name__family_name,
    s.uid AS specialty__specialty_code,
    s.name AS specialty__specialty_desc,
    CASE WHEN cp.statusflag = 'A' THEN 'True' 
    	 ELSE 'False' 
    END active,
    CASE WHEN cp.titleuid = '0' THEN NULL 
    	 ELSE (SELECT TOP 1 valuecode FROM ReferenceValue WHERE uid = cp.titleuid) 
    END name__title,
    LTRIM(RTRIM(cp.forename)) name__given_name,
    NULL name__middle_name,
    LTRIM(RTRIM(cp.surname)) name__family_name,
    CAST(cp.activefrom AS DATETIME) period__start_date,
    CAST(cp.activeto AS DATETIME)   period__end_date,
    rf_role.valuecode role__code,
    rf_role.Description role__desc,
    'BCONN' qualification__system,
    cp.qualification qualification__code,
    cp.qualification qualification__display,
    cp.licenseno license,
	'BCONN' location__enloc_id_loc_system,
	loc.Code location__enloc_id_loc_value,
	loc.Code location__enloc_id_loc_type,
	'official' location__enloc_id_loc_use,
	'HL7' location__enloc_phy_loc_system,
	'wa' location__enloc_phy_loc_code,
	'Ward' location__enloc_phy_loc_display,
	loc.Name location__enloc_loc_name,
	loc.Description location__enloc_loc_desc,
	loc.LocationURL location__enloc_loc_addr
FROM Careprovider cp 
     LEFT JOIN referencevalue rf_role ON rf_role.uid = cp.cptypuid
     LEFT JOIN CareproviderSpecialty cps ON cps.careprovideruid = cp.uid AND cps.StatusFlag = 'A' 
     LEFT JOIN Speciality s ON cps.SpecialtyUID = s.uid 
     LEFT JOIN location loc ON loc.code = cp.middlename 
     INNER JOIN Login login ON cp.uid = login.CareproviderUID 
     LEFT JOIN ss_user ss_user ON login.loginname = ss_user.SSUSR_initials 
WHERE ss_user.SSUSR_initials IS NOT NULL
           AND login.StatusFlag = 'A'
           AND ss_user.SSUSR_initials = '048140361'
        
#Order
select 
      pod.uid row_id,
      po.ordernumber order_number,
      pvid.identifier encounter,
      log.loginname physician,
      CASE WHEN pod.IdentifyingType IN ('ORDERITEM','ORDITEM') THEN oci.code 
      	   WHEN pod.IdentifyingType IN ('REQUESTDETAIL') THEN rd.requestitemcode  
      	   WHEN pod.IdentifyingType IN ('REQUESTITEM') THEN ri.itemcode  
      	   WHEN pod.IdentifyingType IN ('DRUGCATALOGITEM') THEN dgi.code 
      	   WHEN pod.IdentifyingType IN ('MEDICATION') THEN im.code 
      	   WHEN pod.IdentifyingType IN ('ServiceCharge') THEN bei.name 
      	   WHEN pod.IdentifyingType IN ('BillableEvent','BillR2C') THEN bi.code 
      	   ELSE NULL 
       END OrderItem__code,
       CASE WHEN pod.IdentifyingType IN ('ORDERITEM','ORDITEM') THEN oci.name 
			WHEN pod.IdentifyingType IN ('REQUESTDETAIL') THEN rd.requestitemname  
			WHEN pod.IdentifyingType IN ('REQUESTITEM') THEN ri.displyname  
			WHEN pod.IdentifyingType IN ('DRUGCATALOGITEM') THEN dgi.description 
			WHEN pod.IdentifyingType IN ('MEDICATION') THEN im.name  
			WHEN pod.IdentifyingType IN ('ServiceCharge') THEN bei.name  
			WHEN pod.IdentifyingType IN ('BillableEvent','BillR2C') THEN bi.description 
			ELSE NULL 
		END OrderItem__name,
        pod.IdentifyingUID OrderItemType__identifier,
        CASE WHEN pod.IdentifyingType IN ('ORDERITEM','ORDITEM') THEN 'OrderCatalogItem'  
        	 WHEN pod.IdentifyingType IN ('REQUESTDETAIL') THEN pod.IdentifyingType 
        	 WHEN pod.IdentifyingType IN ('REQUESTITEM') THEN pod.IdentifyingType 
        	 WHEN pod.IdentifyingType IN ('DRUGCATALOGITEM') THEN 'DrugCatalogItem' 
        	 WHEN pod.IdentifyingType IN ('MEDICATION') THEN 'ItemMaster' 
        	 WHEN pod.IdentifyingType IN ('ServiceCharge') THEN 'BillableEventItem' 
        	 WHEN pod.IdentifyingType IN ('BillableEvent','BillR2C') THEN 'BillableItem' 
        	 ELSE NULL 
        END OrderItemType__identifier_type,
        rf_status.ValueCode OrderStatus__code,
        rf_status.Description OrderStatus__display,
        pod.startdttm OrderPeriod__start,
        pod.enddttm AS OrderPeriod__end,
        rf_cate.ValueCode OrderCategory__code,
        rf_cate.Description OrderCategory__display
FROM PatientOrderDetail pod 
     JOIN PatientOrder po ON po.uid = pod.PatientOrderUID 
	 JOIN Patient p ON p.uid = po.PatientUID 
	 JOIN PatientVisit pv ON pv.uid = po.PatientVisitUID 
	 JOIN PatientVisitID pvid ON pv.uid = pvid.PatientVisitUID 
     LEFT JOIN ReferenceValue rf_cate ON rf_cate.uid = pod.OrderCategoryUID 
     LEFT JOIN ReferenceValue rf_status ON rf_status.uid = pod.ORDSTUID 
     LEFT JOIN OrderCatalogItem oci ON oci.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('ORDERITEM','ORDITEM')
     LEFT JOIN REQUESTDETAIL rd ON rd.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('REQUESTDETAIL')
     LEFT JOIN RequestItem ri ON ri.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('REQUESTITEM')
     LEFT JOIN DrugCatalogItem dgi ON dgi.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('DRUGCATALOGITEM')
     LEFT JOIN ItemMaster im ON im.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('MEDICATION')
     LEFT JOIN BillableEventItem bei ON bei.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('ServiceCharge')
     LEFT JOIN Login log ON pod.careprovideruid = log.careprovideruid
     LEFT JOIN BillableItem bi ON bi.uid = pod.IdentifyingUID and pod.IdentifyingType IN ('BillableEvent','BillR2C') 
WHERE pod.careprovideruid <> 0 AND p.pasid = '48-14-000001' AND pvid.identifier = 'O48-15-015283'
     ORDER by order_number

#observation
->>>VitalSign
SELECT 
	pvid.identifier observation__encounter ,
    (select top 1 pasid from patient where uid = por.patientuid) observation__patient,
    CAST(por.uid AS VARCHAR) + '|' + CAST(item.uid AS VARCHAR) observation__order_result_item_uid,
    NULLIF(RTRIM(LTRIM(item.ResultValue)),'') observation__value,
    (SELECT TOP 1 rf.description FROM ReferenceValue rf WHERE rf.uid = item.UOMUID) observation__unit,
    NULLIF(RTRIM(LTRIM(item.ReferenceRange)), '') observation__value_range,
     CASE WHEN item.statusflag = 'A' THEN 'final' 
   		  WHEN item.statusflag = 'D' THEN 'cancelled'
          ELSE NULL 
    END observation__status,
    item.resultdttm observation__issued,
    NULL observation__interpretation,
    'vital-signs' category__code,
    'Vital Signs' category__text,
    CASE WHEN REPLACE(LOWER(resultitemname), ' ', '_') LIKE 'vision%' THEN LEFT(REPLACE(LOWER(resultitemname), ' ', '_'), 9) 
         ELSE REPLACE(LOWER(resultitemname), ' ', '_') 
    END code__setcode,
    item.resultitemname code__set_desc,
    NULL code__testcode,
    NULL code__test_desc
from PatientOrderResult por 
    JOIN PatientOrderResultItem item ON item.ResultValue <> '' AND item.OrderResultItemUID = por.uid
    JOIN PatientVisitID pvid ON pvid.PatientVisitUID = por.PatientVisitUID
WHERE por.OrderCatalogItemUID in (select uid from OrderCatalogitem where name like '%Vital Sign%')
      AND por.PatientVisitUID = (SELECT TOP 1 PatientVisitUID FROM PatientVisitID where identifier = 'O48-15-015283')

-->>>Laboratory
SELECT
       'laboratory' category__code,
       'Laboratory' category__text,
       reqitem.ItemCode code__setcode,
       reqitem.DisplyName code__set_desc,
       reitem.Code code__testcode,
       reitem.DisplyName code__test_desc,
       re.uid order_result_item_uid,
       recomp.ResultValue value,
       (SELECT TOP 1 rf.description FROM ReferenceValue rf WHERE rf.uid = reitem.UnitofMeasure) unit,
       recomp.ReferenceRange value_range,
       CASE WHEN re.statusflag = 'A' THEN 'final' ELSE 'registered' END status,
       re.ResultEnteredDttm issued,
       CASE WHEN recomp.IsAbnormal IN('L', 'H') THEN recomp.IsAbnormal
            WHEN recomp.IsAbnormal NOT IN('L', 'H') AND recomp.ReferenceRange <> '' THEN 'N'
            WHEN recomp.ResultValue = 'Negative' THEN 'NEG'
            WHEN recomp.ResultValue = 'Positive' THEN 'POS'
            ELSE ''
        END interpretion
FROM Result re 
        LEFT JOIN RequestItem reqitem ON reqitem.ItemCode = re.RequestItemCode AND reqitem.StatusFlag = 'A' 
        LEFT JOIN ResultComponent recomp ON recomp.ResultUID = re.uid AND recomp.ResultItemName NOT IN('Formatted Result', 'Reference Range') AND recomp.StatusFlag = 'A' 
        JOIN ResultItem reitem ON recomp.ResultItemUID = reitem.uid AND reitem.StatusFlag = 'A' 
        JOIN Patient p ON p.uid = re.PatientUID 
        JOIN PatientVisit pv ON pv.uid = re.PatientVisitUID 
        JOIN PatientVisitID pvid ON pvid.PatientVisitUID = pv.uid 
WHERE re.StatusFlag = 'A' AND len(re.RequestItemCode)=4 
       AND re.RequestItemCode NOT LIKE 'G%'
       AND re.Requestitemcode NOT LIKE 'R%'
       AND p.pasid = '48-14-000001'
       AND pvid.identifier = 'O48-15-015283'

-->>>Radiology
SELECT
      'imaging' Category__code,
      'Imaging' Category__text,
      reqitem.ItemCode code__setcode,
      reqitem.DisplyName code__set_desc,
      reitem.Code testccode__testcodeode,
      reitem.DisplyName code__test_desc,
      re.uid order_result_item_uid,
      CAST(retext.TextualValue AS NVARCHAR(4000)) value,
      null unit,
      null value_range,
      CASE WHEN re.statusflag = 'A' THEN 'final' ELSE 'registered' END status,
      re.ResultEnteredDttm issued,
      null interpretation
from Result re 
    LEFT JOIN RequestItem reqitem ON reqitem.ItemCode = re.RequestItemCode AND reqitem.StatusFlag = 'A'
    LEFT JOIN ResultComponent recomp ON recomp.ResultUID = re.uid AND recomp.ResultItemName NOT IN('Formatted Result', 'Reference Range') 
    	 AND recomp.StatusFlag = 'A'
    LEFT JOIN ResultTextual retext ON retext.ResultComponentUID = recomp.uid AND retext.StatusFlag = 'A'
    JOIN ResultItem reitem ON recomp.ResultItemUID = reitem.uid AND reitem.StatusFlag = 'A'
    JOIN Patient p ON p.uid = re.PatientUID 
    JOIN PatientVisit pv ON pv.uid = re.PatientVisitUID 
    JOIN PatientVisitID pvid ON pvid.PatientVisitUID = pv.uid
WHERE re.StatusFlag = 'A' 
    AND re.RadiologistUID IS NOT NULL
    AND p.pasid = '48-14-000001'
    AND pvid.identifier = 'O48-15-015283'

-->>>PhysicalExam
select pid.identifier observation__encounter,
       p.pasid observation__patient,
       pex.uid observation__order_result_item_uid,
       CAST(pex.TextualValue AS NVARCHAR(4000)) observation__value,
       NULL observation__unit,
       NULL observation__value_range,
       NULL observation__status,
       pex.CWhen observation__issued,
       null observation__interpretation,
       'exam' category__code,
       'Exam' tcategory__ext,
       'physical_Exam' code__setcode,
       'Physical Examination' code__set_desc,
       NULL code__testcode,
       NULL code__test_desc
from BDMSASTEMRPhysicalExam pex
      LEFT JOIN Patient p on p.UID = pex.PatientUID 
      LEFT JOIN PatientVisitID pid on pid.PatientVisitUID = pex.PatientVisitUID 
WHERE pid.identifier = 'O48-15-015283'



select
	CAST(brm.uid AS VARCHAR(100)) identifier,
	brm.ReferralNote description,
	(SELECT TOP 1 Name FROM BDMSReferrer WHERE UID = brm.BDMSReferrerUID) requester,
	p.pasid patient_id,
	pvid.identifier encounter_id
from BDMSReferralMaster brm JOIN Patient p ON p.UID = brm.PatientUID 
	JOIN PatientVisit pv ON pv.uid = brm.PatientVisitUID AND pv.StatusFlag = 'A' 
	JOIN PatientVisitID pvid ON pvid.PatientVisitUID = pv.uid AND pvid.StatusFlag = 'A' 
WHERE brm.StatusFlag ='A' 
	AND p.PASID = '48-15-003475' AND pvid.identifier = 'E48-15-001215'


#encounter
select 
			pvid.identifier identifier,
            rf_status.valuecode status,
            rf_class.valuecode class,
            rf_type.valuecode type,
            CASE WHEN p.isemergency = 'Y' THEN 'True' ELSE 'False' END is_urgency,
            (SELECT TOP 1 Description FROM ReferenceValue WHERE UID = pae.ARRMDUID AND DomainCode = 'ARRMD' AND StatusFlag = 'A') admit_source,
            p.pasid patient,
            rf_service.code service_provider__code,
            rf_service.name service_provider__name,
            rf_service.description service_provider_description,
            NULL encounter_location__start,
            'BCONN' encounter_location__enloc_id_loc_system, 
			rf_location.Code encounter_location__enloc_id_loc_value, 
			'Location.Code' encounter_location__enloc_id_loc_type, 
			'official' encounter_location__enloc_id_loc_use,
            'HL7' encounter_location__enloc_phy_loc_system, 
			'wa' encounter_location__enloc_phy_loc_code, 
			'Ward' encounter_location__enloc_phy_loc_display,
            rf_location.Name encounter_location__enloc_loc_name, 
			rf_location.Description encounter_location__enloc_loc_desc, 
			rf_location.LocationURL encounter_location__enloc_loc_addr,
            pv.startdttm period__start,
            pv.enddttm period__end,
            (SELECT TOP 1 log.loginname FROM Login log WHERE cp.uid = log.careprovideruid ORDER BY log.LastAccessedDTTM DESC) participants__practitioner,
            CASE WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL1' AND StatusFlag = 'A') THEN '1' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL2' AND StatusFlag = 'A') THEN '2' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL3' AND StatusFlag = 'A') THEN '3' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL4' AND StatusFlag = 'A') THEN '4' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL5' AND StatusFlag = 'A') THEN '5' 
                 ELSE NULL
			END priority__code,
            CASE WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL1' AND StatusFlag = 'A') THEN 'Super Red'
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL2' AND StatusFlag = 'A') THEN 'Red' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL3' AND StatusFlag = 'A') THEN 'Yellow' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL4' AND StatusFlag = 'A') THEN 'Green' 
                 WHEN pae.EMGCDUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGLEVL' AND ValueCode = 'LVL5' AND StatusFlag = 'A') THEN 'White' 
            ELSE NULL 
			END priority__display,
            'BCONN' priority__system_source,
            CASE WHEN pae.EMGTPUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGTYP' AND ValueCode = 'NONTRU' AND StatusFlag = 'A') THEN 'False'
                 WHEN pae.EMGTPUID = (SELECT TOP 1 UID FROM ReferenceValue WHERE DomainCode = 'EMGTYP' AND ValueCode = 'TRUMA' AND StatusFlag = 'A') THEN 'True'
                 ELSE NULL 
            END extension__is_trauma,
            de.MedicalDischargeDttm extension__medical_discharge_datetime,
            de.ActualDischargeDttm extension__discharge_datetime,
            (SELECT TOP 1 Description FROM ReferenceValue WHERE UID = de.DSCSTUID AND StatusFlag = 'A') extension__discharge_condition,
            (SELECT TOP 1 Description FROM ReferenceValue WHERE UID = de.DSHTYPUID AND StatusFlag = 'A') extension__discharge_type,
            'BCONN' identifier_list__system,'official' identifier_list__use,
            CASE WHEN left(identifier, 1) = 'E' THEN 'emergency' 
            	 WHEN left(identifier, 1) = 'I' THEN 'inpatient' 
            	 WHEN left(identifier, 1) = 'O' THEN 'outpatient' 
            	 ELSE 'identifier_' + left(identifier, 1) 
            END identifier_list__type,
            pvid.identifier identifier_list__value
from PatientVisit pv 
	JOIN Patient p ON p.UID = pv.PatientUID 
	JOIN PatientVisitID pvid ON pvid.PatientVisitUID = pv.UID 
	LEFT JOIN PatientAEAdmission pae ON pv.UID = pae.PatientVisitUID AND pae.StatusFlag = 'A' 
	LEFT JOIN AdmissionEvent ae ON pvid.PatientVisitUID = ae.PatientVisitUID AND ae.StatusFlag = 'A' 
	LEFT JOIN DischargeEvent de ON de.AdmissionEventUID = ae.UID AND de.StatusFlag = 'A' 
	LEFT JOIN ReferenceValue rf_status ON rf_status.UID = pv.enstauid 
	LEFT JOIN ReferenceValue rf_class ON rf_class.UID = pv.entypuid 
	LEFT JOIN ReferenceValue rf_type ON rf_type.UID = pv.vistyuid 
	LEFT JOIN Careprovider cp ON cp.uid = pv.careprovideruid 
	LEFT JOIN Location rf_location ON rf_location.uid = pv.LocationUID 
	LEFT JOIN service rf_service ON rf_service.uid = pv.serviceuid 
WHERE pvid.identifier = 'E48-15-001215' 
ORDER BY pv.enddttm DESC;


SELECT top 10
	'Patient' resource_type,
    CASE WHEN rf_type.ValueCode = 'NATID' THEN 'NID' 
         WHEN rf_type.ValueCode = 'PASID' THEN 'MRN' 
         WHEN rf_type.ValueCode = 'PSPNM' THEN 'PPN' 
         ELSE 'TMP' 
    END as identifier__type,
    CASE WHEN pid.identifier IS NOT NULL OR LEN(pid.identifier) > 1 THEN pid.identifier 
         ELSE NULL 
    END identifier__value,
    '0'+SUBSTRING(pid.identifier,1, 2) identifier__facility,
    pid.activefrom identifier__start,
    pid.activeto 'identifier__end',
    NULL name__suffix,
    rf_title.description name__prefix,
    CASE WHEN p.middlename = '' THEN NULL 
         ELSE p.middlename 
    END name__middle_name,
    p.surname name__family_name,
    p.forename name__given_name,
    rf_commu.valuecode name__language,
    CASE WHEN addr.CITTYUID IS NOT NULL THEN 
        ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.CITTYUID) 
         ELSE NULL 
    END address__district,
    isnull(addr.line1,'') + ' ' + isnull(addr.line2,'') + ' ' + isnull(addr.line3,'') + ' ' + isnull(addr.line4,'') address__line,
    CASE WHEN addr.STATEUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.STATEUID) 
         ELSE NULL 
    END address__state_desc,
    CASE WHEN addr.CNTRYUID IS NOT NULL THEN 
         ( SELECT TOP 1 ValueCode FROM dbo.ReferenceValue WHERE UID = addr.CNTRYUID) 
         ELSE NULL 
    END address__country,
    CASE WHEN addr.Pincode='999999' THEN NULL 
         ELSE addr.Pincode 
    END address__zipcode,
    CASE WHEN addr.AREAUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM ReferenceValue WHERE UID = addr.AREAUID) 
         ELSE NULL 
    END address__city,
    rf_commu.valuecode communication__commu_language,
    CASE WHEN rf_commu.statusflag = 'A' THEN 'True' 
         ELSE 'False' 
    END communication__commu_preferred,
    CASE WHEN poc.cntypuid = 1 THEN 'phone' 
         WHEN poc.cntypuid = 2 THEN 'phone' 
         WHEN poc.cntypuid = 3 THEN 'email' 
         ELSE NULL 
    END contact__system,
    RTRIM(LTRIM(REPLACE( poc.line1 , '-' , '' ))) contact__value,
    (SELECT TOP 1 description FROM referencevalue WHERE uid = p.VIPTPUID AND StatusFlag = 'A') extension__vip_type,
    CAST(p.uid AS VARCHAR) row_id,
    CAST(p.BirthDttm AS DATE) birth_date,
    CASE WHEN pdd.uid IS NOT NULL THEN 'True' 
         ELSE 'False' 
    END deceased,
    CASE WHEN p.SEXXXUID = '55631' THEN 'F' WHEN p.SEXXXUID = '55630' THEN 'M' 
         ELSE NULL 
    END gender,
    CASE WHEN(pdd.DeathDttm IS NOT NULL) AND(pdd.DeathTime IS NOT NULL) THEN(CAST(CONVERT(CHAR(10), pdd.DeathDttm, 126) + ' ' + SUBSTRING(CONVERT(CHAR(20), pdd.deathTime, 126), 12, 8) AS DATETIME)) 
         ELSE NULL 
    END deceased_datetime,
    rf_nation.ValueCode nationality,
    rf_reli.description religion,
    CASE WHEN p.MARRYUID IS NULL OR p.MARRYUID = '0' THEN 'Unknown' 
         ELSE rf_marital.Description 
    END marital_status
from Patient p
LEFT JOIN ReferenceValue rf_nation ON rf_nation.uid = p.NATNLUID
LEFT JOIN PatientDeceasedDetail pdd ON pdd.patientuid = p.uid
LEFT JOIN ReferenceValue rf_reli ON rf_reli.uid = p.RELGNUID 
LEFT JOIN referencevalue rf_marital ON rf_marital.uid = p.MARRYUID 
LEFT JOIN ReferenceValue rf_title ON rf_title.uid = p.titleuid
LEFT JOIN ReferenceValue rf_commu ON rf_commu.uid = p.spokluid
LEFT JOIN PatientID pid ON pid.patientuid = p.uid AND pid.statusflag = 'A' 
LEFT JOIN ReferenceValue rf_type ON rf_type.uid = pid.pitypuid 
LEFT JOIN patientaddress addr ON addr.patientuid = p.uid 
LEFT JOIN PatientOtherContact poc ON poc.patientuid = p.uid AND poc.statusflag = 'A' AND poc.line1 <> '' 
WHERE pid.identifier <> '' AND p.pasid = '48-14-000010'


SELECT top 10
       CASE WHEN rf_type.ValueCode = 'NATID' THEN 'NID' 
         WHEN rf_type.ValueCode = 'PASID' THEN 'MRN' 
         WHEN rf_type.ValueCode = 'PSPNM' THEN 'PPN' 
         ELSE 'TMP' 
    END as identifier__type,
    CASE WHEN pid.identifier IS NOT NULL OR LEN(pid.identifier) > 1 THEN pid.identifier 
         ELSE NULL 
    END identifier__value,
    '0'+SUBSTRING(pid.identifier,1, 2) identifier__facility,
    pid.activefrom identifier__start,
    pid.activeto 'identifier__end',
    NULL name__suffix,
    rf_title.description name__prefix,
    CASE WHEN p.middlename = '' THEN NULL 
         ELSE p.middlename 
    END name__middle_name,
    p.surname name__family_name,
    p.forename name__given_name,
    rf_commu.valuecode name__language,
    CASE WHEN addr.CITTYUID IS NOT NULL THEN 
        ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.CITTYUID) 
         ELSE NULL 
    END address__district,
    isnull(addr.line1,'') + ' ' + isnull(addr.line2,'') + ' ' + isnull(addr.line3,'') + ' ' + isnull(addr.line4,'') address__line,
    CASE WHEN addr.STATEUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.STATEUID) 
         ELSE NULL 
    END address__state_desc,
    CASE WHEN addr.CNTRYUID IS NOT NULL THEN 
         ( SELECT TOP 1 ValueCode FROM dbo.ReferenceValue WHERE UID = addr.CNTRYUID) 
         ELSE NULL 
    END address__country,
    CASE WHEN addr.Pincode='999999' THEN NULL 
         ELSE addr.Pincode 
    END address__zipcode,
    CASE WHEN addr.AREAUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM ReferenceValue WHERE UID = addr.AREAUID) 
         ELSE NULL 
    END address__city,
    rf_commu.valuecode communication__commu_language,
    CASE WHEN rf_commu.statusflag = 'A' THEN 'True' 
         ELSE 'False' 
    END communication__commu_preferred,
    CASE WHEN poc.cntypuid = 1 THEN 'phone' 
         WHEN poc.cntypuid = 2 THEN 'phone' 
         WHEN poc.cntypuid = 3 THEN 'email' 
         ELSE NULL 
    END contact__system,
    RTRIM(LTRIM(REPLACE( poc.line1 , '-' , '' ))) contact__value,
    (SELECT TOP 1 description FROM referencevalue WHERE uid = p.VIPTPUID AND StatusFlag = 'A') extension__vip_type,
    CAST(p.uid AS VARCHAR) row_id,
    CAST(p.BirthDttm AS DATE) birth_date,
    CASE WHEN pdd.uid IS NOT NULL THEN 'True' 
         ELSE 'False' 
    END deceased,
    CASE WHEN p.SEXXXUID = '55631' THEN 'F' WHEN p.SEXXXUID = '55630' THEN 'M' 
         ELSE NULL 
    END gender,
    CASE WHEN(pdd.DeathDttm IS NOT NULL) AND(pdd.DeathTime IS NOT NULL) THEN(CAST(CONVERT(CHAR(10), pdd.DeathDttm, 126) + ' ' + SUBSTRING(CONVERT(CHAR(20), pdd.deathTime, 126), 12, 8) AS DATETIME)) 
         ELSE NULL 
    END deceased_datetime,
    rf_nation.ValueCode nationality,
    rf_reli.description religion,
    CASE WHEN p.MARRYUID IS NULL OR p.MARRYUID = '0' THEN 'Unknown' 
         ELSE rf_marital.Description 
    END marital_status
from Patient p
LEFT JOIN ReferenceValue rf_nation ON rf_nation.uid = p.NATNLUID
LEFT JOIN PatientDeceasedDetail pdd ON pdd.patientuid = p.uid
LEFT JOIN ReferenceValue rf_reli ON rf_reli.uid = p.RELGNUID 
LEFT JOIN referencevalue rf_marital ON rf_marital.uid = p.MARRYUID 
LEFT JOIN ReferenceValue rf_title ON rf_title.uid = p.titleuid
LEFT JOIN ReferenceValue rf_commu ON rf_commu.uid = p.spokluid
LEFT JOIN PatientID pid ON pid.patientuid = p.uid AND pid.statusflag = 'A' 
LEFT JOIN ReferenceValue rf_type ON rf_type.uid = pid.pitypuid 
LEFT JOIN patientaddress addr ON addr.patientuid = p.uid 
LEFT JOIN PatientOtherContact poc ON poc.patientuid = p.uid AND poc.statusflag = 'A' AND poc.line1 <> '' 
WHERE pid.identifier <> '' AND p.pasid = '48-14-000010'


SELECT top 10
       CASE WHEN rf_type.ValueCode = 'NATID' THEN 'NID' 
         WHEN rf_type.ValueCode = 'PASID' THEN 'MRN' 
         WHEN rf_type.ValueCode = 'PSPNM' THEN 'PPN' 
         ELSE 'TMP' 
    END as identifier__type,
    CASE WHEN pid.identifier IS NOT NULL OR LEN(pid.identifier) > 1 THEN pid.identifier 
         ELSE NULL 
    END identifier__value,
    '0'+SUBSTRING(pid.identifier,1, 2) identifier__facility,
    pid.activefrom identifier__start,
    pid.activeto 'identifier__end',
    NULL name__suffix,
    rf_title.description name__prefix,
    CASE WHEN p.middlename = '' THEN NULL 
         ELSE p.middlename 
    END name__middle_name,
    p.surname name__family_name,
    p.forename name__given_name,
    rf_commu.valuecode name__language,
    CASE WHEN addr.CITTYUID IS NOT NULL THEN 
        ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.CITTYUID) 
         ELSE NULL 
    END address__district,
    isnull(addr.line1,'') + ' ' + isnull(addr.line2,'') + ' ' + isnull(addr.line3,'') + ' ' + isnull(addr.line4,'') address__line,
    CASE WHEN addr.STATEUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM dbo.ReferenceValue WHERE UID = addr.STATEUID) 
         ELSE NULL 
    END address__state_desc,
    CASE WHEN addr.CNTRYUID IS NOT NULL THEN 
         ( SELECT TOP 1 ValueCode FROM dbo.ReferenceValue WHERE UID = addr.CNTRYUID) 
         ELSE NULL 
    END address__country,
    CASE WHEN addr.Pincode='999999' THEN NULL 
         ELSE addr.Pincode 
    END address__zipcode,
    CASE WHEN addr.AREAUID IS NOT NULL THEN 
         ( SELECT TOP 1 Description FROM ReferenceValue WHERE UID = addr.AREAUID) 
         ELSE NULL 
    END address__city,
    rf_commu.valuecode communication__commu_language,
    CASE WHEN rf_commu.statusflag = 'A' THEN 'True' 
         ELSE 'False' 
    END communication__commu_preferred,
    CASE WHEN poc.cntypuid = 1 THEN 'phone' 
         WHEN poc.cntypuid = 2 THEN 'phone' 
         WHEN poc.cntypuid = 3 THEN 'email' 
         ELSE NULL 
    END contact__system,
    RTRIM(LTRIM(REPLACE( poc.line1 , '-' , '' ))) contact__value,
    (SELECT TOP 1 description FROM referencevalue WHERE uid = p.VIPTPUID AND StatusFlag = 'A') extension__vip_type,
    CAST(p.uid AS VARCHAR) row_id,
    CAST(p.BirthDttm AS DATE) birth_date,
    CASE WHEN pdd.uid IS NOT NULL THEN 'True' 
         ELSE 'False' 
    END deceased,
    CASE WHEN p.SEXXXUID = '55631' THEN 'F' WHEN p.SEXXXUID = '55630' THEN 'M' 
         ELSE NULL 
    END gender,
    CASE WHEN(pdd.DeathDttm IS NOT NULL) AND(pdd.DeathTime IS NOT NULL) THEN(CAST(CONVERT(CHAR(10), pdd.DeathDttm, 126) + ' ' + SUBSTRING(CONVERT(CHAR(20), pdd.deathTime, 126), 12, 8) AS DATETIME)) 
         ELSE NULL 
    END deceased_datetime,
    rf_nation.ValueCode nationality,
    rf_reli.description religion,
    CASE WHEN p.MARRYUID IS NULL OR p.MARRYUID = '0' THEN 'Unknown' 
         ELSE rf_marital.Description 
    END marital_status
from Patient p
LEFT JOIN ReferenceValue rf_nation ON rf_nation.uid = p.NATNLUID
LEFT JOIN PatientDeceasedDetail pdd ON pdd.patientuid = p.uid
LEFT JOIN ReferenceValue rf_reli ON rf_reli.uid = p.RELGNUID 
LEFT JOIN referencevalue rf_marital ON rf_marital.uid = p.MARRYUID 
LEFT JOIN ReferenceValue rf_title ON rf_title.uid = p.titleuid
LEFT JOIN ReferenceValue rf_commu ON rf_commu.uid = p.spokluid
LEFT JOIN PatientID pid ON pid.patientuid = p.uid AND pid.statusflag = 'A' 
LEFT JOIN ReferenceValue rf_type ON rf_type.uid = pid.pitypuid 
LEFT JOIN patientaddress addr ON addr.patientuid = p.uid 
LEFT JOIN PatientOtherContact poc ON poc.patientuid = p.uid AND poc.statusflag = 'A' AND poc.line1 <> '' 
WHERE pid.identifier <> '' AND p.pasid = '48-14-000010'


#hisuser
SELECT 
        lg.LoginName username,
        lg.Password password,
        cp.LicenseNo license,
        lg.StatusFlag status_flag,
        'BCONN' source,
        cp.Qualification role
from Login lg JOIN Careprovider cp ON lg.LoginName = cp.Code 
WHERE lg.LoginName IS NOT NULL AND lg.LoginName != '' 
     AND cp.LicenseNo IS NOT NULL AND cp.LicenseNo != ''

#diagnosis
SELECT
	(SELECT TOP 1 ReferenceValue.ValueCode FROM ReferenceValue WHERE ReferenceValue.UID = pprob.SEVTYUID AND ReferenceValue.StatusFlag='A') data__severity,
	'null' data__body_site,
	pprob.RecordedDttm data__asserted_date,
	p.pasid data__patient,
	pvid.Identifier data__encounter,
	CASE WHEN pprob.statusFlag = 'A' AND pprob.ClosureDttm IS NULL THEN 'active' 
		 WHEN pprob.statusFlag = 'A' AND pprob.ClosureDttm IS NOT NULL THEN 'resolved' 
		 ELSE NULL 
	END data__clinical_status,
	ISNULL((SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.CERTYUID AND ReferenceValue.StatusFlag='A'), 'unknown') data__verification_status,
	(SELECT TOP 1 ss_user.SSUSR_initials identifier FROM careprovider cp INNER JOIN Login login ON cp.uid = login.CareproviderUID INNER JOIN ss_user ss_user ON login.loginname = ss_user.SSUSR_initials WHERE cp.uid = pprob.RecordedBy) data__asserter,
	prob.code data__codes__code__coding__code,
	prob.Name data__codes__code__coding__display,
	(SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = prob.CDTYPUID AND ReferenceValue.StatusFlag='A') data__codes__code__coding__system,
	prob.Name data__codes__code__text,
	pprob.OnsetDttm data__code__onset_datetime,
	NULL data__code__onset_duration,
	NULL data__code__onset_unit,
	(SELECT TOP 1 ReferenceValue.ValueCode FROM ReferenceValue WHERE ReferenceValue.UID = pprob.DIAGTYPUID AND ReferenceValue.StatusFlag='A') data__category__0__category__coding__code,
	(SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.DIAGTYPUID AND ReferenceValue.StatusFlag='A') data__category__0__category__coding__display,
	'BCONN' data__category__0__category__coding__system,
	(SELECT TOP 1 ReferenceValue.Description FROM ReferenceValue WHERE ReferenceValue.UID = pprob.DIAGTYPUID AND ReferenceValue.StatusFlag='A') data__category__0__category__text,
	'diagnosis' data__category__1__category__coding__code,
	'Diagnosis' data__category__1__category__coding__display,
	'HL7' data__category__1__category__coding__system,
	'Diagnosis' data__category__1__category__text,
	'BCONN'  data__identifier__system,
	'PatientProblemUID'  data__identifier__type,
	'official'  data__identifier__use,
	CAST(pprob.uid AS VARCHAR(100))  data__identifier__value,
	'Comment' data__note__title,
    pprob.ClosureComments data__note__text
FROM PatientProblem pprob 
	JOIN Problem prob ON pprob.ProblemUID = prob.uid 
	JOIN Patient p ON p.uid = pprob.PatientUID 
	JOIN PatientVisit pv ON pv.uid = pprob.PatientVisitUID 
	JOIN PatientVisitId pvid ON pvid.PatientVisitUID = pv.uid 
WHERE p.pasid = '48-14-000019' AND pvid.Identifier = 'O48-14-000010'

#O04-14-116766

#MEDICATION
SELECT pa.paadm_admno                       context, 
       oei.oeori_prn                        subject, 
       'TC'                                 status_system, 
       NULL                                 status_code, 
       NULL                                 status_display, 
       'TC'                                 identifiers__system, 
       'OEORD_RowId'                        identifiers__type, 
       'official'                           identifiers__use, 
       Cast(oe.oeord_rowid AS VARCHAR(100)) identifiers__value, 
       'Medication'							contained__resource_type,
	   'TC'                                 contained__ingredient__coding__system, 
       aim.arcim_generic_dr                 contained__ingredient__coding__code, 
       aim.arcim_genericdesc                contained__ingredient__coding__display,
       aim.arcim_genericdesc                contained__ingredient__text, 
       'TC'                                 contained__code__coding_system, 
       dm.phcd_code                         contained__code__coding__code, 
       dm.phcd_name                         contained__code__coding__display,
       dm.phcd_name                         contained__code__text,
       NULL									contained__from,
       'TC'                                 contained__route__coding__system, 
       ar.admr_code                         contained__route__coding__code, 
       ar.admr_desc                         contained__route__coding__display, 
       ar.admr_desc                         contained__route__text, 
       NULL									contained__method,
       Ltrim(Rtrim(dm.phcd_labelname2))     contained__instruction_text, 
       Ltrim(Rtrim(dm.phcd_labelname1))     contained__instruction_text_local, 
       'TC'                                 info_status_system, 
       oes.ostat_code                       info_status_code, 
       oes.ostat_desc                       info_status_display, 
       oei.oeori_labeltext                  patient_instruction, 
       oei.oeori_phqtyord                   quantity, 
       oei.oeori_doseqty                    dose_quantity 
FROM   oe_order oe 
       INNER JOIN oe_orditem oei 
               ON oe.oeord_rowid = oei.oeori_oeord_parref 
       INNER JOIN oec_orderstatus oes 
               ON oes.ostat_rowid = oei.oeori_itemstat_dr 
       INNER JOIN pa_adm pa 
               ON pa.paadm_rowid = oe.oeord_adm_dr 
       INNER JOIN arc_itmmast aim 
               ON aim.arcim_rowid = oei.oeori_itmmast_dr 
       INNER JOIN phc_drgmast dm 
               ON aim.arcim_code = dm.phcd_code 
       LEFT JOIN phc_generic gen 
              ON dm.phcd_generic_dr = gen.phcge_rowid 
       LEFT JOIN phc_instruc inst 
              ON inst.phcin_rowid = oei.oeori_instr_dr 
       LEFT JOIN phc_administrationroute ar 
              ON ar.admr_rowid = oei.oeori_adminroute_dr 
WHERE  oei.oeori_categ_dr = 1 
       AND oei.oeori_billed = 'P' 
       AND oes.ostat_code IN( 'E', 'V' ) 
       AND pa.paadm_admno = 'I02-17-000021' 


