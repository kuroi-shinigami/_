import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

detected_envs = {}

for key in ('PROD', 'DEV', 'TEST', 'STAGE'):
    val = os.environ.get(key)
    if val:
        detected_envs.update({key: val})

if len(detected_envs) == 0:
    env = 'DEV'
elif len(detected_envs) > 1:
    raise ValueError('No predefined environment detected!')
else:
    env = detected_envs.popitem()[0]

print('Considered {} envirnment'.format(env))

__import__('{}'.format(env.lower()), globals(), locals())
