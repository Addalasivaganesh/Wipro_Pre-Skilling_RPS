import torch
import torch.nn as nn

#Create RNN Model
rnn = nn.RNN(
    input_size = 5,
    hidden_size = 10,
    num_layers = 1,
    batch_first = True
)

#Dummy input
x = torch.randn(
    2,  #BATCH
    3,  #Sequence
    5   #Features
)

#Forward Pass
output, hidden = rnn(x)
print("output shape")
print(output.shape)
print("Sequence, Steps, Hidden Output")
print("\n Hidden state shape")
print(hidden.shape)
print("Number of RNN Layers, Batch size, Hidden outputs")