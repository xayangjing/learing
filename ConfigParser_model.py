import configparser

config = configparser.ConfigParser()

# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'
#                      }
#
# config['bitbukete.org'] = {'User': 'hg'}
# config['topsecret.server.com'] = {}
# config['topsecret.server.com'] = {'config': 'topsecret.server.com'}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50222'
# topsecret['ForwardX11'] = 'no'
#
# config['DEFAULT']['ForwardX11'] = 'yes'
#
#
# with open('example.conf', 'w') as configfile:
#     config.write(configfile)


# config.remove_section('topsecret.server.com')

config.read('example.conf')

print(config.sections())


print(config.defaults())


print(config['bitbukete.org']['User'])

# config.remove_section('topsecret.server.com')

for key in config:
    print(key)


for key in config['bitbukete.org']:
    print(key)

config.set('bitbukete.org', 'User', 'John')

config.remove_option('bitbukete.org', 'User')

config.write(open('example.conf', 'w'))