import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import math



df = pd.read_csv("sales_time_series.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

sales = df['sales'].values.reshape(-1,1)

scaler = MinMaxScaler(feature_range=(0,1))
sales_scaled = scaler.fit_transform(sales)

sequence_length = 3
X = []
y = []

for i in range(len(sales_scaled)-sequence_length):
    X.append(sales_scaled[i:i + sequence_length])
    y.append(sales_scaled[i + sequence_length])

X = np.array(X)
y = np.array(y)

train_size = int(len(X) * 0.8)

X_train = X[:train_size]
X_test = X[train_size:]

y_train = y[:train_size]
y_test = y[train_size:]

model = Sequential([
    LSTM(50, activation = 'tanh',
         input_shape = (sequence_length, 1)), Dense(1)])

model.compile(
    optimizer = 'adam',
    loss = 'mse'
)

history = model.fit(
    X_train,
    y_train,
    epochs = 100,
    batch_size = 1,
    verbose = 1
)

predictions = model.predict(X_test)

predictions = scaler.inverse_transform(predictions)
actual = scaler.inverse_transform(y_test)

rmse = math.sqrt(mean_squared_error(actual, predictions))
print("RMSE :", rmse)

plt.figure(figsize = (10, 5))
plt.plot(actual, label = 'Actual Sales')
plt.plot(predictions, label = 'Predicted Sales')
plt.title("Actual vs Predicted Sales")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.legend()
plt.show()

future_steps = 10

last_sequence = sales_scaled[-sequence_length:]
future_predictions = []
current_sequence = last_sequence.copy()

for _ in range(future_steps):
    pred = model.predict(current_sequence.reshape(1, sequence_length, 1),
                         verbose = 0
                         )
    future_predictions.append(pred[0][0])
    current_sequence = np.append(current_sequence[1:],pred).reshape(sequence_length, 1)

future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

print("\n Next 10 Forecasted Scales Values :")
for i, value in enumerate(future_predictions, start = 1):
    print(f"Day {i}:{value[0]:2f}")

plt.figure(figsize = (10, 5))
plt.plot(
    range(len(sales)),
    sales,
    label = "HostoricalScales"
)

plt.plot(
    range(len(sales),len(sales) + future_steps),
    future_predictions,
    label = "Forecasted Sales"
)


plt.title("Sales Forecast")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.legend()
plt.show()






