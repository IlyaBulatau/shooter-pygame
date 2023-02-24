import pathlib

FPS = 30
W, H = 495, 895
BASE_DIR = pathlib.Path(__file__).parent
path_to_image = BASE_DIR.joinpath('image')
path_to_textfile_model_gan = pathlib.Path(__file__).parent.resolve().joinpath('model.txt')
