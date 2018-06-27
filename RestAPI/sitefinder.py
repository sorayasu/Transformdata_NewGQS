# """
#         Author  : Supawat Bangprathaiya
#         Created : 14-Sep-2017
#         Version : 1.0
# """

# # from hmsutils.metasingleton import MetaSingleton
# class MetaSingleton(type):
#     _instances = {}
#     def __call__(cls, *args , **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(cls.__class__, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

# class SiteFinder(metaclass=MetaSingleton):
#     sites = [
#         {"group":7,"site":"CLOUD","name":"Amazon Web Services","thai_name": "อเมซอน เว็บ เซอร์วิส","bu": "999"},
#         {"group":7,"site":"HIE","name":"Hopital Information System","thai_name": "ระบบแลกเปลี่ยนข้อมูลระหว่างโรงพยาบาล", "bu": "000"},
#         {"group":None,"site":"BDMS","name":"Bangkok Dusit Medical Service","thai_name":"บริษัท กรุงเทพดุสิตเวชการ จำกัด (มหาชน)","bu":"026"},
#         {"group":1,"site":"BHQ","name":"Bangkok Hospital @ Headquarter","thai_name":"โรงพยาบาลกรุงเทพ ซอยศูนย์วิจัย","bu":"001"},
#         {"group":1,"site":"BHN","name":"Bangkok Hospital Hua Hin","thai_name":"โรงพยาบาลกรุงเทพหัวหิน","bu":"029"},
#         {"group":1,"site":"BCT","name":"Bangkok Hospital China Town","thai_name":"โรงพยาบาลกรุงเทพไชน่าทาวน์","bu":"046"},
#         {"group":1,"site":"BSN","name":"Bangkok Hospital Sanamchan","thai_name":"โรงพยาบาลกรุงเทพสนามจันทร์","bu":"063"},
#         {"group":1,"site":"MPH","name":"Muang Petch Hospital ","thai_name":"โรงพยาบาลเมืองเพชร","bu":"066"},
#         {"group":1,"site":"MRJ","name":"Muangraj Hospital","thai_name":"โรงพยาบาลเมืองราช","bu":"065"},
#         {"group":1,"site":"TPK","name":"Tepakorn Hospital","thai_name":"ร.พ. เทพากร","bu":"064"},
#         {"group":1,"site":"BIL","name":"Bangkok International Clinic Luangprabang","thai_name":"Bangkok International Clinic Luangprabang","bu":"049"},
#         {"group":1,"site":"BPR","name":"Bangkok Hospital Phetchaburi","thai_name": "โรงพยาบาลกรุงเทพเพชรบุรี", "bu":"066"},
#         {"group":2,"site":"SVH","name":"Samitivej Sukhumvit Hospital","thai_name":"โรงพยาบาลสมิติเวชสุขุมวิท","bu":"011"},
#         {"group":2,"site":"SNH","name":"Samitivej Srinakarin Hospital","thai_name":"โรงพยาบาลสมิติเวชศรีนครินทร์","bu":"012"},
#         {"group":2,"site":"SSH","name":"Samitivej Sriracha Hospital","thai_name":"โรงพยาบาลสมิติเวชศรีราชา","bu":"018"},
#         {"group":2,"site":"BNH","name":"BNH Hospital","thai_name":"โรงพยาบาลบีเอนเอช","bu":"009"},
#         {"group":2,"site":"STH","name":"Samitivej Thonburi Hospital","thai_name":"โรงพยาบาลสมิติเวชธนบุรี","bu":"045"},
#         {"group":2,"site":"SCH","name":"Samitivej Chonburi Hospital","thai_name":"โรงพยาบาลสมิติเวชชลบุรี","bu":"058"},
#         {"group":3,"site":"BPH","name":"Bangkok Hospital Pattaya","thai_name":"โรงพยาบาลกรุงเทพพัทยา","bu":"002"},
#         {"group":3,"site":"BRH","name":"Bangkok Hospital Rayong","thai_name":"โรงพยาบาลกรุงเทพระยอง","bu":"015"},
#         {"group":3,"site":"BCH","name":"Bangkok Hospital Chantaburi","thai_name":"โรงพยาบาลกรุงเทพจันทบุรี","bu":"004"},
#         {"group":3,"site":"BTH","name":"Bangkok Hospital Trat","thai_name":"โรงพยาบาลกรุงเทพตราด","bu":"006"},
#         {"group":3,"site":"SRH","name":"Sri Rayong Hospital","thai_name":"โรงพยาบาลศรีระยอง","bu":"039"},
#         {"group":3,"site":"JTN","name":"Jomtien Hospital","thai_name":"โรงพยาบาลจอมเทียน","bu":"059"},
#         {"group":4,"site":"BCM","name":"Bangkok Hospital Chiangmai","thai_name":"โรงพยาบาลกรุงเทพเชียงใหม่","bu":"036"},
#         {"group":4,"site":"BKH","name":"Bangkok Hospital Ratchasima","thai_name":"โรงพยาบาลกรุงเทพราชสีมา","bu":"021"},
#         {"group":4,"site":"BHP","name":"Bangkok Hospital Pakchong","thai_name":"โรงพยาบาลกรุงเทพปากช่อง","bu":"035"},
#         {"group":4,"site":"BUD","name":"Bangkok Hospital Udon","thai_name":"โรงพยาบาลกรุงเทพอุดร","bu":"038"},
#         {"group":4,"site":"BPL","name":"Bangkok Hospital Phitsanulok","thai_name":"โรงพยาบาลกรุงเทพพิษณุโลก","bu":"050"},
#         {"group":4,"site":"BKN","name":"Bangkok Hospital Khon Kaen","thai_name":"โรงพยาบาลกรุงเทพขอนแก่น","bu":"048"},
#         {"group":4,"site":"BPD","name":"Bangkok Hospital Phrapadaeng","thai_name":"โรงพยาบาลกรุงเทพพระประแดง","bu":"003"},
#         {"group":4,"site":"RPH","name":"Royal Phnom Penh Hospital","thai_name":"โรงพยาบาล รอยัล พนมเปญ","bu":"027"},
#         {"group":4,"site":"RAH","name":"Royal Angkor International Hospital","thai_name":"โรงพยาบาล รอยัล อังกอร์ อินเตอร์เนชั่นแนล","bu":"020"},
#         {"group":4,"site":"BKY","name":"Bangkok Hospital Khaoyai","thai_name":"โรงพยาบาลกรุงเทพเขาใหญ่","bu":"030"},
#         {"group":5,"site":"PPG","name":"Prasit Patana PCL","thai_name":"บริษัท ประสิทธิ์พัฒนา จำกัด (มหาชน)","bu":"070"},
#         {"group":5,"site":"PT1","name":"Phyathai 1 Hospital","thai_name":"โรงพยาบาลพญาไท 1","bu":"071"},
#         {"group":5,"site":"PT2","name":"Phyathai 2 Hospital","thai_name":"โรงพยาบาลพญาไท 2","bu":"072"},
#         {"group":5,"site":"PT3","name":"Phyathai 3 Hospital","thai_name":"โรงพยาบาลพญาไท 3","bu":"073"},
#         {"group":5,"site":"PTS","name":"Phyathai Sriracha Hospital","thai_name":"โรงพยาบาลพญาไทศรีราชา","bu":"074"},
#         {"group":5,"site":"PTN","name":"Phyathai Nawamin Hospital","thai_name":"โรงพยาบาลพญาไทนวมินทร์","bu":"075"},
#         {"group":5,"site":"PHT","name":"Paolo Memorial Hospital Phaholyothin","thai_name":"โรงพยาบาลเปาโลเมโมเรียล พหลโยธิน","bu":"076"},
#         {"group":5,"site":"CC4","name":"Paolo Memorial Hospital Chokchai 4","thai_name":"โรงพยาบาลเปาโลเมโมเรียล โชคชัย 4","bu":"077"},
#         {"group":5,"site":"SPK","name":"Paolo Memorial Hospital Samutprakarn","thai_name":"โรงพยาบาลเปาโลเมโมเรียล สมุทรปราการ","bu":"078"},
#         {"group":5,"site":"RST","name":"Paolo Memorial Hospital Rangsit","thai_name":"โรงพยาบาลเปาโลเมโมเรียล รังสิต","bu":"079"},
#         {"group":6,"site":"BPK","name":"Bangkok Hospital Phuket","thai_name":"โรงพยาบาลกรุงเทพภูเก็ต","bu":"005"},
#         {"group":6,"site":"PIH","name":"Bangkok Phuket International Hospital","thai_name":"โรงพยาบาลสิริโรจน์","bu":"067"},
#         {"group":6,"site":"DBK","name":"Dibuk Hospital","thai_name":"โรงพยาบาลดีบุก","bu":"051"},
#         {"group":6,"site":"BHH","name":"Bangkok Hospital Hatyai","thai_name":"โรงพยาบาลกรุงเทพหาดใหญ่","bu":"007"},
#         {"group":6,"site":"BSH","name":"Bangkok Hospital Samui ","thai_name":"โรงพยาบาลกรุงเทพสมุย","bu":"019"},
#         {"group":6,"site":"BSR","name":"Bangkok Hospital Surat","thai_name":"โรงพยาบาลกรุงเทพสุราษฎร์","bu":"054"},
#         {"group":6,"site":"DBK","name": "Dibuk Hospital","thai_name":"โรงพยาบาลดีบุก","bu":"051"},
#         {"group":7,"site":"N Health","name":"National Healthcare Systems","thai_name":"บริษัท เนชั่นแนล เฮลท์แคร์ ซิสเท็มส์ จำกัด ","bu":"010"},
#         {"group":7,"site":"BML","name":"Bio Molecular Laboratories","thai_name":"บริษัท ไบโอ โมเลกุลลาร์ แลบบอราทอรี่ส์ (ประเทศไทย) จำกัด","bu":"014"},
#         {"group":7,"site":"NKH","name":"N Health Cambodia","thai_name":"N Health Cambodia","bu":"060"},
#         {"group":7,"site":"NMM","name":"N Health Myanmar","thai_name":"N Health Myanmar","bu":"061"},
#         {"group":7,"site":"NLA","name":"N Health Laos","thai_name":"N Health Laos","bu":"062"},
#         {"group":7,"site":"NHP","name":"N Health Pathology","thai_name":"N Health Pathology","bu":"069"},
#         {"group":7,"site":"MPC","name":"Medicpharma","thai_name":"บริษัท สหแพทย์เภสัช จำกัด ","bu":"008"},
#         {"group":7,"site":"ANB","name":"ANB Laboratories","thai_name":"บริษัท เอ.เอ็น.บี. ลาบอราตอรี่ (อำนวยเภสัช) จำกัด","bu":"037"},
#         {"group":7,"site":"SDC","name":"Save Drug Center","thai_name":"บริษัท กรุงเทพ เซฟดรัก จำกัด","bu":"068"},
#         {"group":None,"site":"GLS","name":"GreenLine Synergy","thai_name":"บริษัท กรีนไลน์ ซินเนอร์จี้ จำกัด","bu":"028"},
#         {"group":None,"site":"BTC","name":"BDMS Training Company","thai_name":"บริษัท บีดีเอ็มเอส เทรนนิ่ง จำกัด","bu":"032"},
#         {"group":None,"site":"BPB","name":"Bangkok Premier Life Insurance Broker","thai_name":"บริษัทกรุงเทพพรีเมียร์นายหน้าประกันชีวิต ","bu":"034"},
#         {"group":None,"site":"BHI","name":"Bangkok Health Insurance","thai_name":"บริษัท กรุงเทพประกันสุขภาพ จำกัด (มหาชน)","bu":"047"},
#         {"group":None,"site":"ACC","name":"BDMS Accounting","thai_name":"บริษัท บีดีเอ็มเอส แอคเคาท์ติ้ง จำกัด","bu":"052"}
#     ]

#     def find(self, key, value):
#         """
#         Find BDMS sites's detail
#         :param key: must be 'site', or 'bu'
#         :param value: value of this key
#         :return: object of site's detail contains: 'group', 'site', 'name', 'thai_name', and 'bu'
#         """
#         for item in self.sites:
#             if key in item and item[key] == value:
#                 return item
#         return None
