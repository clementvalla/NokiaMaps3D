import Rhino
from Rhino.FileIO import FileReadOptions
import scriptcontext
import rhinoscriptsyntax as rs
import os.path
import math

def importFiles(filePathList):
    '''Import a list of files'''
    # opt = FileReadOptions()
    # opt.ImportMode = True
    for f in filePathList:
        print 'Importing %s' % f
        loaded = scriptcontext.doc.ReadFile(f, opt)
        return loaded

def importFile(filePath):
    '''import one file.'''
    print 'Importing %s' % filePath
    loaded = scriptcontext.doc.ReadFile(filePath, opt)
    return loaded

folder = "/Users/clementvalla/projects/1301_nokia_maps/nokia_map_3d/tile_sets/"
opt = FileReadOptions()
opt.ImportMode = False
count = 0
grid = 15
spacing = 256
imported = False

print len(os.listdir(folder))
for filename in os.listdir(folder):
    if filename.endswith('.obj'):
        print filename
		
        loaded = False
        while not loaded: 
            loaded = importFile(folder+filename)

        rs.Command('-_SelAll')
        objects = rs.SelectedObjects()

        if len(objects) > 0:
          rs.Command('-_Move 0,0,0 %d,%d,0' % (spacing*(count%grid),spacing*math.floor(count/grid)))
          rs.Command('-_Lock')

        count += 1
	    	