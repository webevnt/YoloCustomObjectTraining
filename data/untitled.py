from __future__ import print_function
from config import *
from utils.darknet_classify_image import *
from utils.tesseract_ocr import *
import utils.logger as logger
import sys
from PIL import Image
import time
import os
import re
from operator import itemgetter
PYTHON_VERSION = sys.version_info[0]
OS_VERSION = os.name
import pandas as pd

class PanOCR():
	''' Finds and determines if given image contains required text and where it is. '''

	def __init__(self):
		''' Run PanOCR '''
		logger.good("Initializing Darknet")
		try:
			self.classifier = DarknetClassifier()
			print("self.classifier",self.classifier)
		except Exception as error:
			print(error,"@@@@@@@@@@@@@")



if __name__ == "__main__":
		extracter = PanOCR()
		tim = time.time()
		
		# data=[]
		# for filename in os.listdir('pancards'):,"^^^^^^^^^^")
		# 	print(filename)
		# 	filename='pancards/'+filename
		# 	result=extracter.find_and_classify(filename)
		# 	#print(df1)
		# 	#df=df.append(df1)
		# 	if result==None:
		# 		continue
		# 	else:
		# 		data.append(result)
		
		# df=pd.DataFrame(data)
		# #print(df)
		# df.to_csv (r'output/ocr_result_pan.csv', index = None, header=True,sep='\t')
		# en = time.time()
		# print('TOTAL TIME TAKEN',str(en-tim))
