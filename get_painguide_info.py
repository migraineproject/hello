# bbaasan
# extracts pain guide information from pain_guide.py



from pain_guide import PAIN_GUIDE
from pandas import DataFrame, unique
from collections import Counter

guide = PAIN_GUIDE()


# TODO: what are the most common muscles across all pain categories?

vertex = guide.VERTEX_PAIN
back_head = guide.BACK_OF_HEAD_PAIN
temp = guide.TEMPORAL_HEADACHE
frontal = guide.FRONTAL_HEADACHE
ear_temp = guide.EAR_TEMPOROMANDIBULAR_JOINT_PAIN
eye_eyebrow = guide.EYE_EYEBROW_PAIN
cheek_jaw = guide.CHEEK_JAW_PAIN
tooth = guide.TOOTHACHE
back_neck = guide.BACK_NECK_PAIN
throat_neck = guide.THROAT_FRONT_OF_NECK_PAIN

#print(guide.get_vertex())

def most_common():
	common_muscle_names = list()

	for facial_location in [vertex,back_head, temp, frontal, ear_temp, eye_eyebrow, cheek_jaw, tooth, back_neck, throat_neck]:
		for abbr, muscle_name in facial_location.items():
			if abbr == 'name':
				name = muscle_name
			else:
				pass
			common_muscle_names.append({
				'location': name, 
				'abbr': abbr, 
				'muscle_name': muscle_name})

	return DataFrame(common_muscle_names)

df = most_common()
print(unique(df.muscle_name))

