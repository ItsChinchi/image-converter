from PIL import Image

def convert_webp_to_jpeg(input_path, output_path, quality=120):
    # Open the WebP image
    image = Image.open(input_path)
    image.save(output_path, 'JPEG', quality=quality)


# Example usage
input_file = "input.webp"
output_file = "output.png"
convert_webp_to_jpeg(input_file, output_file)
