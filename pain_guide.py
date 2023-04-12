
class PAIN_GUIDE:

	VERTEX_PAIN = {
		#'name':'vertex pain',
		'SC1': 'Sternocleidomastoid (sternal) (7)',
		'SPL1': 'Splenius capitis (15)'
		}

	BACK_OF_HEAD_PAIN = {
		#'name':'back of head pain',
		'TRAP':'Trapezius (TrPJ (6) )',
		'SC1':'Sternocleidomastoid (sternal) (7)',
		'SC2': 'Sternocleidomastoid (clavicular) (7)',
		'SSC1':'Semispinalis capitis (16)',
		'SSC2': 'Semispinalis cervicis (16)',
		'SPL2':'Splenius cervicis (15)',
		'SO1':'Suboccipital group (17)',
		'SO2':'Occipitalis (14)',
		'DM':'Digastric (12)',
		'TP':'Temporalis (TrPJ (9)' }

	TEMPORAL_HEADACHE = {
		#'name':'temporal headache',
		'TRAP':'Trapezius (TrPJ (6)',
		'SC1':'Sternocleidomastoid (sternal) (7)',
		'TP':'Temporalis (TrPsli2>3 ) (TrPJ (9)',
		'SPL2':'Splenius cervicis (15)',
		'SO1':'Suboccipital group (17)',
		'SSC1':'Semispinalis capitis (16)'}

	FRONTAL_HEADACHE = {
		#'name':'frontal headache',
		'SC2': 'Sternocleidomastoid (clavicular) (7)',
		'SC1':'Sternocleidomastoid (sternal) (7)',
		'SSC1':'Semispinalis capitis (16)',
		'FRO':'Frontalis (14)',
		'ZM':'Zygomaticus major (13)'}

	EAR_TEMPOROMANDIBULAR_JOINT_PAIN = {
		#'name':'ear tmj pain',
		'PTl':'Lateral pterygoid (11)',
		'MAR':'Masseter (superficial) (8)',
		'SC2': 'Sternocleidomastoid (clavicular) (7)',
		'PTm':'Medial pterygoid (10)' }

	EYE_EYEBROW_PAIN = {
		#'name':'eye eyebrow pain',
		'SC1':'Sternocleidomastoid (sternal) (7)',
		'TP':'Temporalis (TrPJ (9)',
		'SPL2':'Splenius cervicis (15)',
		'MAR':'Masseter (superficial) (8)',
		'SO1':'Suboccipital group (17)',
		'SO2':'Occipitalis (14)',
		'OOc':'Orbicularis oculi (13)',
		'TRAP':'Trapezius (TrPJ (6)'}

	CHEEK_JAW_PAIN = {
		#'name':'cheek jaw pain',
		'SC1':'Sternocleidomastoid (sternal) (7)',
		'MAR':'Masseter (superficial) (8)',
		'PTl':'Lateral pterygoid (11)',
		'TRAP':'Trapezius (TrPJ (6)',
		'MAR':'Masseter (deep) (8)',
		'DM':'Digastric (12)',
		'PTm':'Lateral pterygoid (10)',
		'BUC':'Buccinator (13)',
		'PLA':'Platysma (13)',
		'OOc':'Orbicularis oculi (13)',
		'ZM':'Zygomaticus major (13)' }

	TOOTHACHE = {
		#'name':'toothache',
		'TP':'Temporalis  (TrPsj 2 3 ) (TrPJ (9)',
		'MAR':'Masseter (superficial) (8)',
		'DM':'Digastric (anterior)(12)'}

	BACK_NECK_PAIN = {
		#'name':'back neck pain',
		'TRAP':'Trapezius (TrPJ (6)',
		'TRAP':'Trapezius (TrPJ (6)',
		'TRAP':'Trapezius (TrP3) (6)',
		'MF':'Multifidi (16)',
		'LS':'Levator scapulae (19)',
		'SPL2':'Splenius cervicis (15)',
		'ISP':'Infraspinatus (22)'}

	THROAT_FRONT_OF_NECK_PAIN = {
		#'name':'throat front of neck pain',
		'SC1':'Sternocleidomastoid (sternal) (7)',
		'DM':'Digastric (12)',
		'PTm':'Medial pterygoid (10)'}

	def get_vertex(self):
		return self.VERTEX_PAIN