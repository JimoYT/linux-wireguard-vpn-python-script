#!/urs/bin/env python
import os

print('disconnecting vpn')
os.system('sudo wg-quick down wg0-client')
print('Success!')
