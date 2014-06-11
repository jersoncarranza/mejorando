from random import choice

frases = ['soy', 'milton', 'como', 'estas']

def basico(request):
	return {'titulo': choice(frases)}