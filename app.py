from dataclasses import dataclass
import gradio as gr
import time

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


#merge sort algorithm start for sorting songs
def sort_songs(songs, key):
    if len(songs) <= 1:
        return songs
    
    mid = len(songs) //2 
    left = sort_songs(songs[:mid], key)
    right = sort_songs(songs[mid:], key)

    return merge(left, right, key)

#merge sort algorithm with visualization steps (same as merge sort but stores steps for visualization)
def sort_songs_visual(songs, key):
    if len(songs) <= 1:
        return songs

    mid = len(songs) // 2
    left = sort_songs_visual(songs[:mid], key)
    right = sort_songs_visual(songs[mid:], key)

    return merge_visual(left, right, key)

#merge sort algorithm that sorts based on users chosen attribute
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


# stores steps for visualization
animation_steps = []

def merge_visual(left, right, key):
    result = []
    i = j = 0

#merge sort steps but for visualization.
    while i < len(left) and j < len(right):
        animation_steps.append(
            f"Comparing {left[i].title} ({getattr(left[i], key)}) "
            f"vs {right[j].title} ({getattr(right[j], key)})"
        )

        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            animation_steps.append(f"→ Move {left[i].title}")
            i += 1
        else:
            result.append(right[j])
            animation_steps.append(f"→ Move {right[j].title}")
            j += 1

    for item in left[i:]:
        result.append(item)
        animation_steps.append(f"→ Remaining {item.title}")

    for item in right[j:]:
        result.append(item)
        animation_steps.append(f"→ Remaining {item.title}")

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

#calls when user clicks energy sort button
def sort_by_energy():
    sorted_playlist = sort_songs(playlist, "energy")
    return format_playlist(sorted_playlist, "energy")

#calls when user clicks duration sort button
def sort_by_duration():
    sorted_playlist = sort_songs(playlist, "duration")
    return format_playlist(sorted_playlist, "duration")

#calls when user clicks visualize sort button for either.
def visualize_sort(key):
    global animation_steps
    animation_steps = []

    sorted_playlist = sort_songs_visual(playlist, key)

    output = ""
#animation steps
    for step in animation_steps:
        output += step + "\n"
        time.sleep(0.3)
        yield output   # stream updates

    output += "\nFINAL SORTED PLAYLIST:\n\n"
    output += format_playlist(sorted_playlist, key)
    yield output

#gradio interface for user interaction
with gr.Blocks() as interface:
    gr.Markdown("# 🎵🌸 Playlist Vibe Builder🌸🎵 (Using Merge Sort)")

    output = gr.Textbox(label="Sorted Playlist")
#buttons for sorting and visualizing (for both energy and duration)
    with gr.Row():
        energy_btn = gr.Button("Sort by Energy")
        duration_btn = gr.Button("Sort by Duration")
        visualize_energy_btn = gr.Button("🎬 Visualize Energy Sort")
        visualize_duration_btn = gr.Button("🎬 Visualize Duration Sort")

#connects buttots and functions
    energy_btn.click(sort_by_energy, outputs=output)
    duration_btn.click(sort_by_duration, outputs=output)
    visualize_energy_btn.click(visualize_sort, inputs=gr.State("energy"), outputs=output)
    visualize_duration_btn.click(visualize_sort, inputs=gr.State("duration"), outputs=output)

interface.launch(share=True)
