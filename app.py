from dataclasses import dataclass
import gradio as gr

@dataclass
#creates a class so defining songs is quick.
class Song: 
    title: str
    artist: str
    energy: int
    duration: int


#set playlist for testing
playlist = [
    Song("Better in the Dark", "TV Girl", 55, 155),
    Song("The Blonde", "TV Girl", 48, 228),
    Song("Hate Yourself", "TV Girl", 57, 213),
    Song("Lovers Rock", "TV Girl", 62, 213),
    Song("Tejano Blue", "Cigarettes After Sex", 40, 234),
    Song("Nothing's Gonna Hurt You Baby", "Cigarettes After Sex", 30, 286),
    Song("Manchild", "Sabrina Carpenter", 80, 213),
    Song("Such A Funny Way", "Sabrina Carpenter", 74, 232),
    Song("The Bolter", "Taylor Swift", 60, 238),
    Song("Slim Pickins", "Sabrina Carpenter", 55, 152),
    Song("Toronto Mug", "Slaughter Beach, Dog", 48, 98)
]


#merge sort algorithm
def sort_songs(songs, key):
    if len(songs) <= 1:
        return songs
    
    mid = len(songs) //2 
    left = sort_songs(songs[:mid], key)
    right = sort_songs(songs[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        #gets attribute from class to sort (energy or duration)
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def format_playlist(sorted_playlist, sort_key):
    #will store what to print depending on option chosen by user
    output = ""
    if sort_key == "energy":
        #prints subtitle and sorted list by energy lvl
        output += "Playlist sorted by energy level:\n\n"
        for song in sorted_playlist:
            output += f"{song.title} by {song.artist} — {song.energy}% energy\n"

    else:
        # prints subtitle and sorted list based on duration of songs.
        output += "Playlist sorted by duration:\n\n"
        for song in sorted_playlist:
            mins = round(song.duration / 60, 2)
            output += f"{song.title} by {song.artist} — {song.duration}s ({mins} mins)\n"

    return output


def sort_by_energy():
    sorted_playlist = sort_songs(playlist, "energy")
    return format_playlist(sorted_playlist, "energy")


def sort_by_duration():
    sorted_playlist = sort_songs(playlist, "duration")
    return format_playlist(sorted_playlist, "duration")


with gr.Blocks() as interface:
    # adds title 
    gr.Markdown("# 🎵🌸 Playlist Vibe Builder🌸🎵 (Using Merge Sort)\n\n\n")
# adds textbox area for sorted list. 
    output = gr.Textbox(label="Sorted Playlist")

    with gr.Row():
        energy_btn = gr.Button("Sort by Energy")
        duration_btn = gr.Button("Sort by Duration")
# adds buttons with two options for sorting the playlist, energy or duration. 
    energy_btn.click(fn=sort_by_energy, outputs=output)
    duration_btn.click(fn=sort_by_duration, outputs=output)

interface.launch(inbrowser=True)
