import json
# import dbus
# import dbus.mainloop.glib
# from gi.repository import GLib

import grpc
import media_pb2
import media_pb2_grpc

from MediaClient import MediaClient

config_file = 'config.json'

if __name__ == '__main__':
	with open(config_file) as data_file:
		config = json.load(data_file)

	mc = MediaClient(config)

	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
	bus = dbus.SystemBus()
	bus.add_signal_receiver(
			ms.onPropertyChanged,
			bus_name='org.bluez',
			signal_name='PropertiesChanged',
			dbus_interface='org.freedesktop.DBus.Properties')
	GLib.MainLoop().run()
