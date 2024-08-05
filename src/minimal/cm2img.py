import cm2py as cm2
from PIL import Image

def imageconvert(path, wid):
    image = Image.open(path)
    save = cm2.Save()

    size = image.size
    reduced = image.resize((wid, round(size[1] / (size[0] / wid))))
    dimensions = reduced.size
    colordata = list(reduced.getdata())

    for width in range(dimensions[0]):
        for height in range(dimensions[1]):
            rgb = colordata[height * dimensions[0] + width]
            y = dimensions[1] - 1 - height
            if isinstance(rgb, int):
                save.addBlock(cm2.TILE, (width, y, 0), properties=[rgb, rgb, rgb])
            else:
                save.addBlock(cm2.TILE, (width, y, 0), properties=[rgb[0], rgb[1], rgb[2]])
            
    saveString = save.exportSave()
    return saveString
