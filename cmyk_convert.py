import numpy as np
from PIL import Image




def tiff_to_array(path_to_file):
    img = Image.open(path_to_file, 'r')
    return np.asarray(img)

def array_to_tiff(array, path_to_file):
    img = Image.fromarray(array, mode='CMYK')
    img.save(path_to_file, compression='tiff_deflate')


def rescale_by_element(original_cmyk_array, ink_limit):
    cmyk_array = np.copy(original_cmyk_array)
    rows = np.shape(cmyk_array[:, 0])[0]
    cols = np.shape(cmyk_array[0, :])[0]
    for row in range(rows):
        for col in range(cols):
            element = cmyk_array[row, col]
            total_ink = sum(element)
            if total_ink > ink_limit:
                # rescale here
                amount_over = total_ink - ink_limit
                percent_of_ink = element / total_ink
                element -= (amount_over * percent_of_ink).astype(np.uint8)
    return cmyk_array

def rescale_by_array(original_cmyk_array, ink_limit):
    cmyk_array = np.copy(original_cmyk_array)
    rows = np.shape(cmyk_array[:, 0])[0]
    #cols = np.shape(cmyk_array[0, :])[0]

    total_ink = np.sum(cmyk_array, axis = 2)
    print(cmyk_array.shape)
    print(total_ink.shape)

    amount_over = total_ink - ink_limit
    percent_of_ink = cmk_array / total_ink
    cmk_array[amount_over > 0] -= (percent_of_ink * )#cmk_array[where] / total_ink)

    # for row in range(rows):
    #     for col in range(cols):
    #         element = cmyk_array[row, col]
    #         total_ink = sum(element)
    #         if total_ink > ink_limit:
    #             # rescale here
    #             amount_over = total_ink - ink_limit
    #             percent_of_ink = element / total_ink
    #             element -= (amount_over * percent_of_ink).astype(np.uint8)
    return cmyk_array

ink_limit = 200 #somewhere between 0 and 400
test_image = 'testimage.tiff'
save_image = 'saveimage.tiff'

cmyk_array_original = tiff_to_array(test_image)
cmyk_array = rescale_by_array(cmyk_array_original, ink_limit)
#cmyk_array = rescale(cmyk_array_original, ink_limit)
#array_to_tiff(cmyk_array, save_image)





