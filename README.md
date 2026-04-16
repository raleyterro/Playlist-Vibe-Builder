# Playlist-Vibe-Builder
A website that sorts a set playlist based on the users choice of energy level or song duration!

CISC 121 Project
🎵🌸 Playlist Vibe Builder🌸🎵
(Using Merge Sort)

The problem I chose to solve for this project was the Playlist Vibe Builder (2). The website I created lets the user choose how to sort the playlist (either by energy or duration of the song) and then a sorted version of the playlist is printed. 

For this problem I decided to use merge sort, because it would be quicker and more accurate at sorting the songs if there were multiple songs with the same energy level or duration time. 

Preconditions: The data for the playlist does not need to be already sorted, and can be any songs as long they fit the Songs class. The playlist in the website was made by me, but can be changed in the code. 

During the simulation, the user is presented with four buttons, they can either sort the playlist by energy or duration, OR view the sorting process of either options. Based on what they pick, the result will be displayed.

Playlist Vibe Builder:
Data: a list of songs (title, artist, energy score 0–100, duration). 
User action: choose a sorting key (e.g., energy or duration) and sort the playlist. 
App output: show the sorted playlist and animate comparisons/moves so the re-ordering is easy to follow. 

Problem Breakdown: 

Decomposition:
- Have set stored data of songs
- Let user pick sorting key
- Sort using merge sort algorithm
- Display sorted playlist

Pattern Recognition:
Sorting the songs by energy or duration uses the same method of sorting. 

Abstraction:
Ignoring irrelevant details such as the lyrics of the song, or artist. The only important details are the data of the chosen sorting key, and the title when displaying the sorted list. 

Algorithm Design: 

Input: unsorted playlist of songs, sorting key chosen by user.

Process: based on the sorting key, the list is sorted and movements are documented for animating.

Output: Sorted list and animation of movements during re-ordering. 

Steps to Run: 
Hugging Face Link

Hugging Face Link: https://huggingface.co/spaces/raley/Playlist-Vibe-Builder  

