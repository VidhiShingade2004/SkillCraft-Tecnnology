from PIL import Image
import numpy as np
import argparse

def load_image(image_path):
    """Load an image from file and return as numpy array"""
    img = Image.open(image_path)
    return np.array(img)

def save_image(image_array, output_path):
    """Save a numpy array as an image file"""
    img = Image.fromarray(image_array)
    img.save(output_path)

def swap_channels(pixel, swap_pattern):
    """Swap RGB channels according to the pattern"""
    if len(pixel) == 4:  # RGBA
        r, g, b, a = pixel
    else:  # RGB
        r, g, b = pixel
        a = None
    
    swapped = list(pixel)
    for i, channel in enumerate(swap_pattern):
        if channel == 'r':
            swapped[i] = r
        elif channel == 'g':
            swapped[i] = g
        elif channel == 'b':
            swapped[i] = b
        elif channel == 'a' and a is not None:
            swapped[i] = a
    
    if a is None:
        return tuple(swapped[:3])
    return tuple(swapped)

def apply_operation_to_pixel(pixel, operation, value):
    """Apply a mathematical operation to each channel of a pixel"""
    result = []
    for channel in pixel:
        if operation == 'add':
            new_val = (channel + value) % 256
        elif operation == 'sub':
            new_val = (channel - value) % 256
        elif operation == 'xor':
            new_val = channel ^ value
        elif operation == 'mult':
            new_val = (channel * value) % 256
        else:
            new_val = channel
        result.append(new_val)
    return tuple(result)

def scramble_pixels(image_array, seed=None):
    """Scramble pixels using a random permutation"""
    if seed is not None:
        np.random.seed(seed)
    
    # Flatten the image and create a permutation
    original_shape = image_array.shape
    flat = image_array.reshape(-1, image_array.shape[-1])
    perm = np.random.permutation(flat.shape[0])
    
    # Apply permutation
    scrambled = flat[perm]
    
    # Reshape back to original dimensions
    return scrambled.reshape(original_shape)

def encrypt_image(image_path, output_path, operations):
    """Apply encryption operations to an image"""
    img_array = load_image(image_path)
    
    for op in operations:
        if op['type'] == 'swap':
            # Swap RGB channels
            swap_pattern = op['pattern']
            for i in range(img_array.shape[0]):
                for j in range(img_array.shape[1]):
                    img_array[i,j] = swap_channels(img_array[i,j], swap_pattern)
        
        elif op['type'] == 'math':
            # Apply mathematical operation
            operation = op['operation']
            value = op['value']
            for i in range(img_array.shape[0]):
                for j in range(img_array.shape[1]):
                    img_array[i,j] = apply_operation_to_pixel(img_array[i,j], operation, value)
        
        elif op['type'] == 'scramble':
            # Scramble pixels
            seed = op.get('seed', None)
            img_array = scramble_pixels(img_array, seed)
    
    save_image(img_array, output_path)
    print(f"Image encrypted and saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output image file path")
    
    # Operation arguments
    parser.add_argument("--swap", help="Channel swap pattern (e.g., 'grb' to swap red and green)")
    parser.add_argument("--math", help="Math operation and value (e.g., 'add:50', 'xor:128')")
    parser.add_argument("--scramble", type=int, help="Scramble pixels with optional seed")
    
    args = parser.parse_args()
    
    operations = []
    
    if args.swap:
        operations.append({
            'type': 'swap',
            'pattern': args.swap.lower()
        })
    
    if args.math:
        op, val = args.math.split(':')
        operations.append({
            'type': 'math',
            'operation': op.lower(),
            'value': int(val)
        })
    
    if args.scramble is not None:
        operations.append({
            'type': 'scramble',
            'seed': args.scramble
        })
    
    if not operations:
        print("No operations specified. Please provide at least one operation.")
        return
    
    encrypt_image(args.input, args.output, operations)

if __name__ == "__main__":
    main()