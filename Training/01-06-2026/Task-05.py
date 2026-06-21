# Given:
#
# Dataset = 1000 records
# Batch size = 100
# Epochs = 5
#
#
# Answers
# 1. Batches per epoch
# 1000 / 100 = 10 batches
#
#
# 2. Weight updates per epoch
# Each batch = 1 update
# So:
# 10 updates per epoch
#
#
# 3. Total updates after 5 epochs
# 10 × 5 = 50 updates


#Code
dataset_size = 1000
batch_size = 100
epochs = 5

batches_per_epoch = dataset_size // batch_size
updates_per_epoch = batches_per_epoch
total_updates = updates_per_epoch * epochs

print("Batches per epoch:", batches_per_epoch)
print("Updates per epoch:", updates_per_epoch)
print("Total updates after 5 epochs:", total_updates)