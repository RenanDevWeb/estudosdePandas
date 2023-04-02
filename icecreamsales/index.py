import pandas as pd 

import matplotlib.pyplot as plt



data = pd.read_csv('IceCreamData.csv')


result = data.sort_values('Temperature', ascending=False)

plt.plot(result['Temperature'],result['Revenue'], 'r.--', label='US$')
plt.title('Ice cream sales')
plt.ylabel("Sales US$")
plt.xlabel("Temperature (Fahrenheit)")
plt.legend()
plt.show()