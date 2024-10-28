from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(output_path)
        print(f"Resized image saved to: {output_path}")


def resize_images():
    images_to_resize = {
        "assets/outerspace_background.jpg": ("assets/space_bg_resized.gif", (1320, 800)),
        "assets/shooter.gif": ("assets/shooter_resized.gif", (90, 90)),
        "assets/alien_large.gif": ("assets/alien_large_resized.gif", (75, 75)),
        "assets/alien_medium.gif": ("assets/alien_medium_resized.gif", (55, 55)),
        "assets/alien_small.gif": ("assets/alien_small_resized.gif", (45, 45)),
        "assets/explosion.gif": ("assets/explosion_resized.gif", (80, 80))
    }

    for input_path, (output_path, size) in images_to_resize.items():
        resize_image(input_path, output_path, size)

if __name__ == "__main__":
    resize_images()
