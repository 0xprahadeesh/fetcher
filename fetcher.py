import piexif

import os 
from termcolor import colored
cmd = 'figlet -kp FETCHER | lolcat -a -d 7'

cn = 'cyan'
re = 'red'
ora = 'orange'

name = colored("Open Source Information Gatherer Tool",cn)


credits = colored("[Prahadeesh,Vinith,Sowmi_Saltonya,Jegatheesh]",re)

print("Here is our" ,name)

print("CREATED BY: == ",credits)

os.system(cmd)

entry = input("DO U HAVE VICTIM NAME OR IMG OR BOTH:")

if entry == "IMG":

    image_name = input("ENTER YOUR FILE NAME WITH EXTENSION:")

    exif_dict = piexif.load(image_name)

# Extract thumbnail and save it, if exists
    thumbnail = exif_dict.pop('thumbnail')
    if thumbnail is not None:
        with open('thumbnail.jpg', 'wb') as f:
            f.write(thumbnail)

# Iterate through all the other ifd names and print them
    print(f'Metadata for {image_name}:')
    for ifd in exif_dict:
        print(f'{ifd}:')
        for tag in exif_dict[ifd]:
            tag_name = piexif.TAGS[ifd][tag]["name"]
            tag_value = exif_dict[ifd][tag]
        # Avoid print a large value, just to be pretty
            if isinstance(tag_value, bytes):
                tag_value = tag_value[:10]
            print(f'\t{tag_name:25}: {tag_value}')
    print()


elif entry == "NAME":
    victim_name = input("Enter victim name:")

    cmd = ('python3 username.py -u '+ victim_name)
    os.system(cmd)
    
# CODE IS AGAI REPRODUCED DUE TO THE OPTION FOR BOTH     
    
elif entry == "BOTH":
    image_name = input("ENTER YOUR FILE NAME WITH EXTENSION:")

    exif_dict = piexif.load(image_name)

# Extract thumbnail and save it, if exists
    thumbnail = exif_dict.pop('thumbnail')
    if thumbnail is not None:
        with open('thumbnail.jpg', 'wb') as f:
            f.write(thumbnail)

# Iterate through all the other ifd names and print them
    print(f'Metadata for {image_name}:')
    for ifd in exif_dict:
        print(f'{ifd}:')
        for tag in exif_dict[ifd]:
            tag_name = piexif.TAGS[ifd][tag]["name"]
            tag_value = exif_dict[ifd][tag]
        # Avoid print a large value, just to be pretty
            if isinstance(tag_value, bytes):
                tag_value = tag_value[:10]
            print(f'\t{tag_name:25}: {tag_value}')
    print()
    
    victim_name = input("Enter victim name:")

    cmd = ('python3 username.py -u '+ victim_name)
    os.system(cmd)
    

