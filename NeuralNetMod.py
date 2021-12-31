class Neuron:
	def __init__(self, bias=0):
		self.InWeights = []
		OutValue = bias
		self.bias = bias
	def max_add(self):
		return 1 - sum(self.InWeights)
	def add_weight(self, weight):
		if sum(self.InWeights) + weight > 1:
			return
		self.InWeights += [weight]
		return self.InWeights
	def output(self, inputs):
		if OutValue != 0:
			OutValue = self.bias
		if sum(self.InWeights) != 1 or len(inputs) != len(self.InWeights):
			return
		for i in range(0, len(self.InWeights)):
			OutValue += inputs[i] * self.InWeights[i]
		return OutValue
class Layer:
	def __init__(self):
		self.neurons = []
	def add_neuron(self, neuron):
		self.neurons += [neuron]
	def get_outputs(self, inputs):
		outputs = [self.neurons[i].output() for i in range(0, len(self.neurons))]
		if None in outputs:
			return
		return outputs
	def Neuron__max_add(self, index):
		return self.neurons[index].max_add()
	def Neuron__add_weight(self, weight, index):
		return self.neurons[index].add_weight(weight)
	def Neuron__output(self, inputs, index):
		return self.neurons[index].output(inputs)
class NeuralNet:
	def __init__(self):
		self.InputLayer = None
		self.HiddenLayers = []
		self.OutputLayer = None
	def CreateInputLayer(self, layer):
		self.InputLayer = layer
	def CreateOutputLayer(self, layer):
		self.OutputLayer = layer
	def add_layer(self, layer):
		self.HiddenLayers += [layer]
	def run(self, inputs):
		if None in [self.InputLayer, self.OutputLayer]:
			return
		tempLayer = Layer()
		for neuron in self.InputLayer.neurons[:]:
			if neuron.bias == 0:
				tempLayer.add(neuron)
		if len([Neuron(input_val) for input_val in inputs]) != len(self.InputLayer):
			return
		firstInputLayer = self.InputLayer
		firstOutputLayer = self.OutputLayer
		self.InputLayer = [Neuron(input_val) for input_val in inputs]
		#CONTINUE HERE... START EXECUTING
	def Layer__add_neuron(self, neuron, index):
		if index == 0:
			self.InputLayer[index].add_neuron(neuron)
		elif index > len(HiddenLayers):
			self.OutputLayer[0].add_neuron(neuron)
		else:
			self.HiddenLayer[index - 1].add_neuron(neuron)
	def Layer__get_outputs(self, inputs, index):
		if index == 0:
			self.InputLayer[index].get_outputs(inputs)
		elif index > len(HiddenLayers):
			self.OutputLayer[0].get_outputs(inputs)
		else:
			self.HiddenLayer[index - 1].get_outputs(inputs)
