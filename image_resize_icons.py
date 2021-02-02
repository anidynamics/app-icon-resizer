import os
import click
import cv2

dimensions = [
    (40, 40),
    (60, 60),
    (58, 58),
    (87, 87),
    (80, 80),
    (120, 120),
    (180, 180),
    (20, 20),
    (29, 29),
    (58, 58),
    (76, 76),
    (152, 152),
    (167, 167),
    (1024, 1024)
]

@click.command()
@click.option('--file_path' , default='', help='Path to image file')
@click.option('--output_folder', default='', help='Output folder. Default: current folder.')
def resize_image(file_path, output_folder):
    """Resize input image given by IMAGE_PATH to given resolutions and output to OUTPUT_FOLDER."""
    if output_folder is '':
        output_folder = os.getcwd()
    print(file_path)
    print(output_folder)

    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    print(img.shape)

    for dim in dimensions:
        img_resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        # print(img_resized.shape)
        new_file_name = os.path.basename(file_path).split('.')[:-1][0] + '_' + str(img_resized.shape[0]) + '.' + os.path.basename(file_path).split('.')[-1]
        # print(new_file_name)
        print('Writing image ' + os.path.join(output_folder, new_file_name))
        cv2.imwrite(os.path.join(output_folder, new_file_name), img_resized)

if __name__ == '__main__':
    resize_image()
