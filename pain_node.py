from pandas import DataFrame, unique
from pain_guide import PAIN_GUIDE
from muscle_information import MUSCLE_INFO

guide = PAIN_GUIDE()


def pain_guide_table(cls = guide):
	ref = []

	vertex_pain = cls.VERTEX_PAIN
	head_pain = cls.BACK_OF_HEAD_PAIN
	temp_head = cls.TEMPORAL_HEADACHE
	front = cls.FRONTAL_HEADACHE
	tmj = cls.EAR_TEMPOROMANDIBULAR_JOINT_PAIN
	eyebrow = cls.EYE_EYEBROW_PAIN
	jaw = cls.CHEEK_JAW_PAIN
	tooth = cls.TOOTHACHE
	neck = cls.BACK_NECK_PAIN
	throat = cls.THROAT_FRONT_OF_NECK_PAIN

	for pain in [vertex_pain, head_pain,temp_head,front,tmj,eyebrow,jaw,tooth,neck,throat]:
		for abbr, descr in pain.items():
			if abbr == 'name':
				name = descr
			ref.append({
				'location':pain, 
				'muscle_abbr':abbr,
				'description':descr})

	return DataFrame(ref)

pain = pain_guide_table()
for i in unique(pain.description):
	print(i)