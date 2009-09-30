#python
# Export Selected To Obj
# Exports the Selected Geomtetry to an OBJ file

# @author: Johan Steen
# @author URI: http://www.artstorm.net/
# @copyright: Johan Steen
# @date: 30 September 2009
# @modified: 30 September 2009
# @version: 1.0

# @revisions

import lx

#** CLASSES **#
# Debugging class (Experimental while learning some python)
class Debugging:
    # Constructor
    def __init__(self, contents=None):
        self.contents = contents or []
        lx.out('Debugging class initialized')
        
    def set_trace(self, state=False):
        lx.trace(state)

#** FUNCTIONS **#

#** APPLICATION **#
# Output script info to the Event Log
lx.out("Script: exportSelectedToObj.py")
lx.out("Version: 1.0")

#Debug = Debugging()
#Debug.set_trace(True)

# Copy the selection to a new temporary scene
lx.eval('select.copy')
lx.eval('scene.new')
lx.eval('select.paste')

# Setup the file dialog and open it
lx.eval('dialog.setup fileSave')
lx.eval('dialog.title "Export as..."')
lx.eval('dialog.fileType scene');
lx.eval('dialog.fileSaveFormat obj extension');
try:
    lx.eval('dialog.open')
except:
    dialogAbort = True
    lx.eval('!scene.close')
    
# If file requester wasn't aborted
try:
    dialogAbort
except NameError:
    # Get the filename, save it and close the temporary scene
    filename = lx.eval('dialog.result ?')
    lx.eval('scene.saveAs {%s} wf_OBJ false' %filename)
    lx.eval('scene.close')

