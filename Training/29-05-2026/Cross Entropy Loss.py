import torch
import torch.nn as nn

#Predicting the Scores(Logits)
predictions = torch.tensor(
    [[2.5, 1.2, 0.3]], #Pass, Fail, Absent
    requires_grad=True
)

#Actual Class
target = torch.tensor([0])
#Cross Entropy Loss
criterion = nn.CrossEntropyLoss()
#Calculate the loss
loss = criterion(predictions, target)
print(loss)