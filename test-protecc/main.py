from protecc.vortex import Vortex

vtx = Vortex()

vtx.SECRETS['test'] = 'ab'

@vtx.register_endpoint
def does_something(x):
    return x

does_something(vtx.SECRETS['test'])