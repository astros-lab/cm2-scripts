import cm2py as cm2

def textconvert(text):
    save = cm2.Save()

    row, col = 0
    for char in text:
        asciival = ord(char)

        if asciival == 10:
            col = 0
            row += 1
        else:
            save.addBlock(cm2.TEXT, (col, 0, row), properties=[asciival])
            col += 1

    saveString = save.exportSave
    return saveString
