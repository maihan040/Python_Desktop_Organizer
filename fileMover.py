#!/usr/bin/python3

'''fileMover.py
   Small app which will move all the files from a specified directory to their dedicated location
   Idea is to keep the "download" folder as light as possible to prevent any confusion on subesequent downloads

   Created: 10/26/2019

   Version: 1.0

   Improvement suggestions: 

'''

############################ Import modules ###########################
import os 
import paths
import argparse
import configparser

###################### Set up config file values ######################
config = configparser.ConfigParser()
config.read('<insert the path to where the config.py file has been placed')

########################  Function Definition ########################
def moveFiles(src, dst, ext):

	#check whether the source directory exists 
	if not os.path.exists(dst):
		os.mkdir(dst)

	#local variables
	fileList = [] #to keep track of the files that need to be moved 

	#populate the list of files for the given directory 
	for file in os.listdir(src):
		if(file.endswith(ext)):
			fileList.append(file)

	#start moving the files if there are any to move
	if(len(fileList) > 0):
		for file in fileList:

			#build full source and file pathnames 
			source = src + "/" + file
			destination = dst + "/" + file
			
			#move
			os.rename(source, destination)
	else: 
		print("There are no files to be moved from the source directory!")

def main():
	
	###################################################################################
	# Build mechanism to parse user input in order to determine which 
	#directory and files to clean up
	###################################################################################
	
	#create parser
	parser = argparse.ArgumentParser(description='De-clutter a specified directory.')
	
	#define arguments for the directories/files 
	parser.add_argument('-dir',choices=['Desktop', 'Document', 'Downloads'], help='De-clutter the specified directory')
	parser.add_argument('-ext',choices=['cpp', 'cu', 'py', 'js', 'pdf', 'jpg', 'zip', 'deb'], help='De-clutter the specified files based on the file extension')

	#get arguments
	args = parser.parse_args()

	###################################################################################
	#start cleaning 
	###################################################################################
	print("Cleaning up " + args.ext + " files from the " + args.dir + " directory....")

	#call the moveFiles method and pull the paths from the config file
	moveFiles(config['SysPaths'][args.dir], config['DestPaths'][args.ext], args.ext)
	print("Cleaned up directory")

########################     MAIN       ########################
#run the main method 
if __name__ == '__main__':
	main()