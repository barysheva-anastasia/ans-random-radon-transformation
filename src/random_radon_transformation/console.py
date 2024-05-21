from . import __version__, random_radon_transformation as rrt
from PIL import Image
import numpy as np
import click



@click.command()
@click.option(
    "--img_dir",
    default="tests/pictures",
    show_default=True
)
@click.option(
    "--input_file",
    default="input_file.jpg",
    show_default=True
    
)
@click.option(
    "--output_file",
    default="output_file.jpg",
    show_default=True
)
@click.option(
    "--rho_steps",
    default=220,
    show_default=True
)
@click.option(
    "--theta_steps",
    default=440,
    show_default=True
)
@click.option(
    "--n_iter",
    default=100000,
    help="# of iterations",
    show_default=True
)
@click.version_option(version=__version__)
def main(
    img_dir: str,
    input_file: str,
    output_file: str,
    rho_steps: int,
    theta_steps: int,
    n_iter: int
) -> None:

    init_img = np.array(Image.open(img_dir + f"/{input_file}"))
    transformed_image = rrt.random_radon_transformation(
        init_img[:,:,0],
        rho_steps,
        theta_steps,
        n_iter
    )

    output_img = Image.fromarray(transformed_image).convert("RGB")
      
    output_img.save(img_dir + f"/{output_file}") 

