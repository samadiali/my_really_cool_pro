class Monester:

	def __init__ (self,**kwargs):
		''' def __init__ (self,color, sound,number,weapon):
		'''
		self.color = kwargs.get('color','red')
		self.sound = kwargs. get ('sound','Roar')
		self.number = kwargs.get('number',3)
		self.weapon = kwargs.get ('weapon' , 'sword')


	def battelcry (self):
		return (self.sound)

	





