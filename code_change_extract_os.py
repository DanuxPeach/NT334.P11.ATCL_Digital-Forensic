import struct

def replace_unix_with_msdos(zip_path, output_path):
    with open(zip_path, 'rb') as zip_file:
        data = zip_file.read()
    
    modified_data = bytearray(data)
    
    central_directory_signature = b"PK\x01\x02"
    local_file_header_signature = b"PK\x03\x04"
    
    central_directory_offset = modified_data.find(central_directory_signature)
    while central_directory_offset != -1:
        version_made_by_offset = central_directory_offset + 4
        current_version_made_by = struct.unpack("<H", modified_data[version_made_by_offset:version_made_by_offset + 2])[0]
        
        new_version_made_by = (0 << 8) | (current_version_made_by & 0xFF)
        struct.pack_into("<H", modified_data, version_made_by_offset, new_version_made_by)
        
        version_needed_offset = central_directory_offset + 6
        current_version_needed = struct.unpack("<H", modified_data[version_needed_offset:version_needed_offset + 2])[0]
        
        new_version_needed = (0 << 8) | (current_version_needed & 0xFF)
        struct.pack_into("<H", modified_data, version_needed_offset, new_version_needed)
        
        central_directory_offset = modified_data.find(central_directory_signature, central_directory_offset + 46)
    
    local_file_header_offset = modified_data.find(local_file_header_signature)
    while local_file_header_offset != -1:
        version_needed_offset = local_file_header_offset + 4
        current_version = struct.unpack("<H", modified_data[version_needed_offset:version_needed_offset + 2])[0]
        
        new_version = (0 << 8) | (current_version & 0xFF)
        struct.pack_into("<H", modified_data, version_needed_offset, new_version)
        
        local_file_header_offset = modified_data.find(local_file_header_signature, local_file_header_offset + 30)
    
    with open(output_path, 'wb') as output_file:
        output_file.write(modified_data)
    
    print(f"Change Unix to MS-DOS success!")

zip_file_path = "C:\\Users\\Lenovo\\DanuxPeach\\FileHocTap\\Nam4\\Foren\\doan\\sample\\7z-linux-bzip2.zip"
output_file_path = "C:\\Users\\Lenovo\\DanuxPeach\\FileHocTap\\Nam4\\Foren\\doan\\output\\modified_linux_to_msdos.zip"
replace_unix_with_msdos(zip_file_path, output_file_path)