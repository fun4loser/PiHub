class NotificationDelegate:
	
	def __init__(notificationInstance):
		self.notificationInstance = notificationInstance

	def notify(self, data):
		print "Override this class with a custom implementation"

