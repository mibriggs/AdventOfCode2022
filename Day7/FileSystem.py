class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
    
    def __str__(self) -> str:
        return f'{self.name} (file, size={self.size})'

    def get_file_size(self) -> int:
        return int(self.size)
    
    def __hash__(self) -> int:
        return hash(self.name) + hash(self.size)
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, File):
            return hash(__o) == hash(self)
        return False

class FileSystem:
    def __init__(self, name: str, parent=None) -> None:
        self.name: str = name
        self.parent = parent
        self.files: list[File] = []
        self.sub_folders: list[FileSystem] = []

    def add_child(self, file_system) -> None:
        self.sub_folders.append(file_system)

    def add_file(self, file_obj: File) -> None:
        self.files.append(file_obj)
    
    def get_sub_folder(self, file_system):
        if file_system in self.sub_folders:
            indx = self.sub_folders.index(file_system)
            return self.sub_folders[indx]
        return None
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, FileSystem):
            return hash(__o) == hash(self)
        return False
    
    def __str__(self) -> str:
        msg = ''
        msg += f'- {self.name} (dir)\n'
        return self.build_string(msg, 1)
    
    def build_string(self, message, depth):
        for file_name in self.files:
            line = ((' ' * 4)*depth) + f'- {str(file_name)}\n'
            message += line
        for folder in self.sub_folders:
            line = ((' ' * 4)*depth) + f'- {folder.name} (dir)\n'
            message += line
            message = folder.build_string(message, depth + 1)
        return message

    def __hash__(self) -> int:
        return hash(self.get_path())
        
    def get_hash(self) -> int:
        return self.__hash__()
    
    def get_path(self) -> str:
        return self.get_path_helper('')
    
    def get_path_helper(self, path_so_far: str) -> str:
        if self.parent is None:
            if self.name == '/':
                return path_so_far
            return self.name + path_so_far
        else:
            return self.parent.get_path_helper(f'/{self.name}'+path_so_far)
    
    def get_size(self) -> int:
        total_size = 0
        for fle in self.files:
            total_size += fle.get_file_size()
        for sub_folder in self.sub_folders:
            total_size += sub_folder.get_size()
        return total_size
