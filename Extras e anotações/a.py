import math
import random

random.seed(42)

def sigmoid(x):
    if x < -700: return 0.0
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(output):

    return output * (1.0 - output)


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.in_nodes = input_nodes
        self.hid_nodes = hidden_nodes
        self.out_nodes = output_nodes
        self.learning_rate = 0.5


        self.weights_ih = [[random.uniform(-1, 1) for _ in range(self.hid_nodes)] for _ in range(self.in_nodes)]

        self.weights_ho = [[random.uniform(-1, 1) for _ in range(self.out_nodes)] for _ in range(self.hid_nodes)]


        self.bias_h = [random.uniform(-1, 1) for _ in range(self.hid_nodes)]
        self.bias_o = [random.uniform(-1, 1) for _ in range(self.out_nodes)]

    def feedforward(self, input_array):

        

        hidden = []
        for i in range(self.hid_nodes):
            soma = self.bias_h[i]
            for j in range(self.in_nodes):
                soma += input_array[j] * self.weights_ih[j][i]
            hidden.append(sigmoid(soma))

        output = []
        for i in range(self.out_nodes):
            soma = self.bias_o[i]
            for j in range(self.hid_nodes):
                soma += hidden[j] * self.weights_ho[j][i]
            output.append(sigmoid(soma))

        return hidden, output

    def train(self, input_array, target_array):
        

        hidden, output = self.feedforward(input_array)


        output_errors = [target_array[i] - output[i] for i in range(self.out_nodes)]


        output_gradients = []
        for i in range(self.out_nodes):
            grad = output_errors[i] * sigmoid_derivative(output[i]) * self.learning_rate
            output_gradients.append(grad)


        for i in range(self.hid_nodes):
            for j in range(self.out_nodes):
                self.weights_ho[i][j] += output_gradients[j] * hidden[i]
        for i in range(self.out_nodes):
            self.bias_o[i] += output_gradients[i]


        hidden_errors = []
        for i in range(self.hid_nodes):
            erro = 0.0
            for j in range(self.out_nodes):
                erro += output_errors[j] * self.weights_ho[i][j]
            hidden_errors.append(erro)


        hidden_gradients = []
        for i in range(self.hid_nodes):
            grad = hidden_errors[i] * sigmoid_derivative(hidden[i]) * self.learning_rate
            hidden_gradients.append(grad)


        for i in range(self.in_nodes):
            for j in range(self.hid_nodes):
                self.weights_ih[i][j] += hidden_gradients[j] * input_array[i]
        for i in range(self.hid_nodes):
            self.bias_h[i] += hidden_gradients[i]



if __name__ == "__main__":

    nn = NeuralNetwork(2, 4, 1)


    training_data = [
        {"input": [0, 0], "target": [0]},
        {"input": [1, 0], "target": [1]},
        {"input": [0, 1], "target": [1]},
        {"input": [1, 1], "target": [0]}
    ]

    print("Treinando a Rede Neural. Isso exige milhares de iterações...\n")
    epocas = 10000
    for epoca in range(epocas):

        random.shuffle(training_data) 
        for data in training_data:
            nn.train(data["input"], data["target"])
            
        if (epoca + 1) % 2500 == 0:
            print(f"Progresso: {epoca + 1} épocas concluídas.")

    print("\n--- TESTE FINAL: A IA APRENDEU? ---")

    for data in training_data:
        _, previsao = nn.feedforward(data["input"])
        entrada = data["input"]
        esperado = data["target"][0]

        resultado_final = round(previsao[0], 4)
        
        print(f"Entrada: {entrada} | Esperado: {esperado} | IA Previu: {resultado_final}")
