import os
import os.path

class File:
	def __init__(self, path):
		self.path = path
		self.mtime = None
		self.ctime = None
		self.size = 0

	def get_metadata(self):
		date = os.path.getmtime(self.path)
		mtime = os.path.getmtime(self.path)
		size = os.path.getsize(self.path)
		return [date, mtime, size]

	def is_binary(self):
		pass

	def preview(self):
		pass

	


class Listener:

	'''
	 revers
	def by_name
	def by_name_reverse
		def by_date(self):
		print(map(lambda x: os.path.getmtime(x), self.path))
		return os.listdir(self.path)
'''
dir = Listener(os.getcwd())
print(dir.by_date())