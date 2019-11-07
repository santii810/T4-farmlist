import queue
from src.utils import setup_values

imperat_lids = queue.Queue()
imperan_lids = queue.Queue()
for i in setup_values.lids['imperat']:
    for j in range(100):
        imperat_lids.put(i)
for i in setup_values.lids['imperat']:
    for j in range(100):
        imperan_lids.put(i)

print(imperan_lids.get())
for i in range (100):
    imperan_lids.get()
print(imperan_lids.get())
