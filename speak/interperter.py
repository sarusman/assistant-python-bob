from unidecode import unidecode 
import requests, random, os

def main(text):
	text=unidecode(text.lower())
	if "meteo" in text:
		return get_meteo(text.split(' ')[1])

	elif "blague" in text:
		return blague_depressive()
	elif "musique" in text:
		return find_msk()

	else:
		return text



def get_meteo(ville):
	return resolve_meteo(eval(requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095").text))


def blague_depressive():
	blague_pas_drole={'blague0': 'Comment appelle-t-on la maman loutre ?_._.-. Loutre mère',
	 'blague1': 'Si tu vois un oiseau sur un lac… .C’est un signe.',
	  'blague2': '2 bûcherons discutent :- « Je vais rester bûcheron toute ma vie… »,. L’autre répond : « Moi je vais changer de boulot… « ',
	   'blague3': 'Qu’est-ce que fait un pou dans une cloche ?_._.- Pou Ding',
	    'blague4': 'Que dit un médecin à une crevette avant de l’ausculter ?_._.- Décortiquez-vous !',
	     'blague5': 'Monsieur et madame Nouissement ont une fille. Comment s’appelle-t-elle ?_._.- Éva',
	      'blague6': 'Tu connais la blague de la chaise?_._.- Elle est pliante',
	       'blague7': 'Vous auriez pu me prévenir pour les clubs échangistes.  J’ai eu l’air con avec mes cartes Pokémon.',
	        'blague8': 'Monsieur et madame Métégal ont un fils. Comment s’appelle-t-il ?_._.- Sam',
	         'blague9': 'Monsieur et madame Dupoisson ont un fils. Comment s’appelle-t-il ?_._.- Ivan',
	          'blague10': '– Papa y’a quelqu’un a la porte avec une moustache.  – Dis-lui que j’en ai déjà une. ',
	           'blague11': 'Où les super héros vont-ils faire leurs courses ?_._.- Au supermarché',
	            'blague12': 'Quel est le légume le plus courageux ?_._.- Le pois chiche',
	             'blague13': 'Monsieur et madame Oto ont deux fils. Comment s’appellent-t-ils ?_._.- Ivan, Sam'}
	return blague_pas_drole['blague'+str(random.randint(0, 13))]



def find_msk():
	musique_l=os.listdir(os.getcwd()+"/musique")
	return random.choice(musique_l)




def resolve_meteo(dtc):
	try:
		temps=dtc['weather'][0]['description']
	except:
		return "Je n'ai pas trouvé votre ville"
	if temps=="clear sky":
		return "Il fait beau sur "+dtc['name']
	elif temps=="few clouds" or  temps=="scattered clouds":
		return "Le ciel est légérement nuageux sur "+dtc['name']
	elif temps=="overcast clouds" or temps=="broken clouds":
		return "Le ciel est très nuageux sur "+dtc['name']
	elif temps=="mist":
		return "Il y a du brouillard sur "+dtc['name']

	elif temps=="moderate rain":
		return "Il pleut légèrement sur "+dtc['name']

	elif "rain" in temps:
		return "Le temps est pluvieux sur "+dtc['name']
	else:
		return "Je ne sais pas. Il est indiqué "+ temps

