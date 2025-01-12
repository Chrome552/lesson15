import pickle
from f import names

result = pickle.dumps(names)
print(result)

reload = pickle.loads(result)
print(reload)