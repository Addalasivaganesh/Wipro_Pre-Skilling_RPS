import torch
import torch.nn as nn

#Create LSTM Model
lstm = nn.LSTM(
    input_size = 5,
    hidden_size = 10,
    num_layers = 1,
    batch_first = True
)

#Dummy import
x = torch.randn(
    2,
    3,
    5
)
#Forward Pass
output, (hidden, cell) = lstm(x)

print("Output Shape")
print(output.shape)
print("Sequence, Steps, Hidden Output")
print("------------------------------------------------------")
print("\n Hidden state shape")
print(hidden.shape)
print("Number of RNN Layers, Batch size, Hidden outputs")
print("------------------------------------------------------")
print("\n Cell State Shape")
print(cell.shape)
print("Layers, Sequence, Hidden Neurons")
print("------------------------------------------------------")