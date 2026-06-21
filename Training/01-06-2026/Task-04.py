# Given:
#
# Dataset = 100 records
#
# Answers
# 1. Batch size = 10
# Number of batches =
# 100 / 10 = 10 batches
#
#
# 2. Batch size = 20
# 100 / 20 = 5 batches
#
#
# 3. Batch size = 25
# 100 / 25 = 4 batches
#
#
# 4. Which batch size gives more weight updates?
# Smaller batch size → More updates
#
# Batch size 10 → 10 updates
# Batch size 20 → 5 updates
# Batch size 25 → 4 updates
#
# Answer: Batch size = 10

# Dataset size Demo code
dataset_size = 100

batch_sizes = [10, 20, 25]

for batch in batch_sizes:
    num_batches = dataset_size // batch
    print(f"Batch size {batch}: {num_batches} batches (weight updates)")


