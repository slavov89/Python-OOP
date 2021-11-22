from .album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        info = f"Band {self.name}"

        for album in self.albums:
            info += f"\n{album.details()}"

        return info

"""
The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list). 
The class has three methods:
    • add_album(album: Album)
        ◦# Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
        ◦# If the album is already added, returns "Band {band_name} already has {album_name} in their library."
    • remove_album(album_name: str)
        ◦ Removes the album from the collection and returns "Album {name} has been removed."
        ◦ If the album is published, returns "Album has been published. It cannot be removed."
        ◦ If the album is not in the collection, returns "Album {name} is not found."
    • details()
        ◦ Returns the information of the band, with their albums, in this format: 
"Band {name}
 {album details}
 ...
 {album details}"
"""