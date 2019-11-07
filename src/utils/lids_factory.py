from queue import Queue


def create(lids):
    imperat_lids = Queue()
    imperan_lids = Queue()
    for i in lids['imperat']:
        for j in range(100):
            imperat_lids.put(i)
    for i in lids['imperan']:
        for j in range(100):
            imperan_lids.put(i)
    return {'imperat': imperat_lids, 'imperan': imperan_lids}
