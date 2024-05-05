import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as f:
    data = json.load(f)

widths = [entry['width'] for entry in data]
sums = [int(entry['sum'], 16) for entry in data]  

plt.plot(widths, sums)
plt.xlabel('Width')
plt.ylabel('Sum')
plt.title('Sum vs. Width')
plt.grid(True)
plt.show()