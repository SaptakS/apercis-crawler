import sys
import logging

def print_info():
	# Get the previous frame on calling stack.
	fr_obj = sys._getframe(1)
	# Output file name and line number. 
	print "%s: %d" % (fr_obj.f_code.co_filename, fr_obj.f_lineno)
	
	

