from PIL import Image

# Paths to assets - in a real scenario, these would be more dynamic and potentially user-provided
avatar_paths = ['avatar1.png', 'avatar2.png', 'avatar3.png']
banner_paths = ['banner1.png', 'banner2.png', 'banner3.png']

def select_asset(asset_list):
    """ Allow the user to select an asset """
    for i, asset in enumerate(asset_list, start=1):
        print(f"{i}. {asset}")
    choice = int(input("Select an asset by number: "))
    return asset_list[choice - 1]

def combine_images(avatar_path, banner_path):
    """ Combine avatar and banner images """
    try:
        avatar = Image.open(avatar_path).convert('RGBA')
        banner = Image.open(banner_path).convert('RGBA')

        # Calculate position: center the avatar on the banner
        banner_width, banner_height = banner.size
        avatar_width, avatar_height = avatar.size
        position = ((banner_width - avatar_width) // 2, (banner_height - avatar_height) // 2)

        # Place avatar on banner
        banner.paste(avatar, position, avatar)
        return banner
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_design(image, file_path='final_design.png'):
    """ Save the final design to a file """
    if image:
        image.save(file_path)
        print(f"Design saved to {file_path}")
    else:
        print("No design to save.")

def main():
    print("Welcome to the Avatar and Banner Design Tool!")
    
    print("\nSelect an avatar:")
    selected_avatar = select_asset(avatar_paths)
    
    print("\nSelect a banner:")
    selected_banner = select_asset(banner_paths)
    
    final_design = combine_images(selected_avatar, selected_banner)
    
    if final_design:
        save_design(final_design)
    else:
        print("Failed to create the design.")

if __name__ == '__main__':
    main()
