import numpy as np
#vár.ért: A: 5% B: 10%, szór: A:10% B:20% árfolyam
a_r=np.random.normal([0.05,0.1],[0.1,0.2],(100,2))
# print(a_r)
a_initial_price=np.array([[50,100]])
print(a_initial_price)
a_price=a_initial_price*np.exp(a_r)
# print(a_price)