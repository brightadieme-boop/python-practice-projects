def make_album (artist_name, album_title, tracks=None):
    album =  { 
             'artist':artist_name.title(),
              'title':album_title.title() 
        }
    if tracks is not None:
        album['tracks'] = tracks
    return album