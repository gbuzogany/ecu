import twisted.internet.protocol
import twisted.internet.reactor

class MediaServer(twisted.internet.protocol.Protocol):
	def __init__(self, config):
		self.config = config
		self.currentlyPlaying = None
		self.playStatus = 'unknown'

	def connectionMade(self):
		self.peer = self.transport.getPeer()[1:]
		print "Connected from", self.peer
	def dataReceived(self, data):
		self.transport.write(data)
	def connectionLost(self, reason):
		print "Disconnected from", self.peer, reason.value

	def onPropertyChanged(self, interface, changed, invalidated):
		if interface != 'org.bluez.MediaPlayer1':
			return

		for prop, value in changed.items():
			if prop == 'Status':
				self.playStatus = value

				print('Playback Status: {}'.format(value))
			elif prop == 'Track':
				# Album, Duration, Genre, Title, Artist
				currentlyPlaying = {
					'title': value.get('Title', ''),
					'artist': value.get('Artist', ''),
					'album': value.get('Album', '')
				}

				if currentlyPlaying['title'] != '':
					self.currentlyPlaying = currentlyPlaying
				else:
					self.currentlyPlaying = None

				print('Music Info:')
				for key in ('Title', 'Artist', 'Album'):
					print('   {}: {}'.format(key, value.get(key, '')))
