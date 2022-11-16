import random
shots = int(input('shots: '))
_days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
for i in range(shots):
    r = random.choice(_days)
    _days.remove(r)
    print(r)