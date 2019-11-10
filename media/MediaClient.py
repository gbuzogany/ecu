import twisted.internet.protocol

class MediaClient:
	def __init__(self, config):
		self.config = config

	def notifyPlayStatusChanged(self, status):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = media_pb2_grpc.MediaPlayerStub(channel)
			response = stub.PlayStatusChanged(media_pb2.PlayStatus(playStatus=status))
			print(response.status)

	def notifyPlayStatusChanged(self, mediaItem):
		with grpc.insecure_channel('localhost:50051') as channel:
			response = stub.MediaChanged(media_pb2.MediaItem(
				title=mediaItem['title'],
				artist=mediaItem['artist'],
				album=mediaItem['album'])
			)
			print(response.status)

	def onPropertyChanged(self, interface, changed, invalidated):
		if interface != 'org.bluez.MediaPlayer1':
			return

		for prop, value in changed.items():
			if prop == 'Status':
				self.notifyPlayStatusChanged(value);
				print('Playback Status: {}'.format(value))

			elif prop == 'Track':
				# Available: Album, Duration, Genre, Title, Artist
				self.notifyPlayStatusChanged({
					'title': value.get('Title', ''),
					'artist': value.get('Artist', ''),
					'album': value.get('Album', '')
				})
				print('Music Info:')
				for key in ('Title', 'Artist', 'Album'):
					print('   {}: {}'.format(key, value.get(key, '')))
