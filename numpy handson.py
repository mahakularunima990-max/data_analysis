import numpy as np
sales=np.array([[100, 200, 300, 400, 500],
                [150, 250, 350, 450, 550],
                [260, 360, 460, 560, 660],
                [370, 470, 570, 670, 770],
                [480, 580, 680, 780, 880]])
print(sales.shape)
print(sales[0])
print(sales[1, 2])
print(sales[:, -1])
print(sales[2:4])
print(sales[1:4:2])
print(sales[1:4, 2:5])
mask=sales < 50
filtered_sales=sales[mask]
print(filtered_sales)
print(sales.reshape(5,-1))
daily_bonus=np.array([[10, 20, 30, 40, 50]])
print(daily_bonus)
sales_with_bonus=sales + daily_bonus
print(sales_with_bonus)
