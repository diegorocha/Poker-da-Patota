#!/usr/bin/env python

from sys import argv
from os import path, mkdir
from shutil import rmtree, copytree

def deploy(deployDirectory):
  folderOrigin = path.abspath(path.join('.', 'src'))
  print 'Starting deploying to folder', deployDirectory,'\nAll content of the directory will be erased.'
  
  print 'Erasing previously data.'
  rmtree(deployDirectory)
  
  print 'Copying files to', deployDirectory
  copytree(folderOrigin, deployDirectory)
  
  print 'Done.'

def displayHelp():
  print 'usage python PokerPatotaDeploy.py [--help] deployDirectory' 
  return None

def displayNoParamError():
  print 'No path to deploy.\nSee help [--help] for more information.'

def displayDirectoryError(deployDirectory):
  print 'Path', deployDirectory, 'does not exists.'
  
if __name__ == '__main__':
  if len(argv) == 1:
    displayNoParamError()
  else:
    param = argv[1]
    if param == "--help":
      displayHelp()
    else:
      deployDirectory = path.abspath(argv[1])
      if(path.exists(deployDirectory)):
        deploy(deployDirectory)
      else:
        displayDirectoryError(deployDirectory)
