# Import SDK
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from rox.core.entities.rox_string import RoxString
from rox.core.entities.rox_int import RoxInt
from rox.server.rox_options import RoxOptions, NetworkConfigurationsOptions

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

# OVERWRITING network configs to point to a custom environment (VPC/Preprod for example).  Default is production.
network_config = NetworkConfigurationsOptions(
    'https://api.vpc-install-test.saas-tools.beescloud.com/device/get_configuration',
    'https://rox-conf.vpc-install-test.saas-tools.beescloud.com',
    'https://api.vpc-install-test.saas-tools.beescloud.com/device/update_state_store/',
    'https://rox-state.vpc-install-test.saas-tools.beescloud.com',
    'https://fm-analytics.vpc-install-test.saas-tools.beescloud.com',
    'https://sdk-notification-service.vpc-install-test.saas-tools.beescloud.com/sse')

options = RoxOptions(network_configuration_options=network_config)

# Setup the SDK key
sdk_key = '<YOUR-SDK-KEY>'
cancel_event = Rox.setup(sdk_key, options).result();

# Boolean flag example
print('showMessage is {}'.format(flags.showMessage.is_enabled()))

# String flag examples
print('font color is {}'.format(flags.fontColor.get_value()))
print('message is {}'.format(flags.message.get_value()))

# Double flag examples
print('fontSize is {}'.format(flags.fontSize.get_value()))

