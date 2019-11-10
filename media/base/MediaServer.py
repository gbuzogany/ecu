class MediaServer:
	def __init__(self, config):
		self.config = config

	def onPropertyChanged(self, interface, changed, invalidated):
	    print(interface)
	    for prop, value in changed.items():
	        if prop == 'Status':
	            print('Playback Status: {}'.format(value))
	        elif prop == 'Track':
	            print('Music Info:')
	            for key in ('Title', 'Artist', 'Album'):
	                print('   {}: {}'.format(key, value.get(key, '')))