import maya.cmds as cmds

def renameSelection(name):
    sels = cmds.ls(selection=True)
    if not sels:
        cmds.warning("No objects selected to rename.")
        return

    for i, sel in enumerate(sels):
        newname = f'{name}{i+1:04d}_GEO'
        cmds.rename(sel, newname)