# Import SDK
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from rox.core.entities.rox_string import RoxString
from rox.core.entities.rox_int import RoxInt

# Create Roxflags in the Flags container class
class Flags:
    def __init__(self):
        #Define the feature flags
        self.showMessage = RoxFlag(False)
        self.message = RoxString('This is the default message; try changing some flag values!')
        self.fontColor = RoxString('Black', ['Red', 'Green', 'Blue', 'Black'])
        self.fontSize = RoxInt(99, [10, 50, 99])
        
flags = Flags()

# Register the flags container
Rox.register(flags)

# Setup the environment key
environment_key = '41e6957f-9472-4a83-5d47-dec57cc6947e'
cancel_event = Rox.setup(environment_key).result();

# Boolean flag example
print('showMessage is {}'.format(flags.showMessage.is_enabled()))

# String flag examples
print('font color is {}'.format(flags.fontColor.get_value()))
print('message is {}'.format(flags.message.get_value()))

# Double flag examples
print('fontSize is {}'.format(flags.fontSize.get_value()))

