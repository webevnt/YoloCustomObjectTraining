import pexpect
import os
from config import *
from typing import Tuple
from config import settings


class DarknetClassifier():

	def initialize(self):
		command = settings.DARKNET_BINARY_LOCATION + " detector train " + settings.DARKNET_DATA_FILE + " " + settings.DARKNET_CFG_FILE \
			+ " " + "darknet53.conv.74"
		print(command)
		self.proc = pexpect.spawn(command)

	def classify_image(self, image:str) -> str:
		self.proc.sendline(image)
		self.proc.expect('Enter Image Path:', timeout=90)
		res = self.proc.before
		return res.decode('utf-8')
	def extract_info(self, line:str) -> Tuple:
		nameplate_info = line.split()
		#print(nameplate_info)
		nameplate_confidence = nameplate_info[1]
		nameplate_left_x = int(nameplate_info[3])
		nameplate_top_y = int(nameplate_info[5])
		nameplate_width = int(nameplate_info[7])
		nameplate_height = int(nameplate_info[9][:-1])

		area = (nameplate_left_x, nameplate_top_y, (nameplate_left_x + nameplate_width), (nameplate_top_y + nameplate_height))

		return area
