# Pytho_Desktop_Organizer

## Purpose:

This is a python tool to organize a pariticular folder on your system. Currently it's design de-clutter the folder by moving all ".jpg", ".pdf", and ".deb" files to the specified folders that will be set up in the config stage by the end user in the "config.py" and "paths.py" files. 

## Motivation:

Motivation for this project was twofold: 
  
  * Learn more about automation and python
  * Build a tool that can be used to run on a schedule to keep a cluttered file system organized

## Tech/framework used:

  * Python version 3.8.5
  * argparse

## Contents:
  * fileMover.py - main script which has the entire implementation and logic
  * config.py - config file where user will have to specify system and destination paths 
  * paths.py - similar to the config file, only this one uses a disctionary 
  * .gitignore - list of files which are not beeing tracked currently 
 
## Directions:

In order for the script to work, user would have have to populate all the "" fields in the config.py and paths.py file such paths to various source and 
destination folders.  
