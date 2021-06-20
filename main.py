import csv

from pytube import YouTube
import music_tag


csv_path = "example.csv"

def main():
    with open(csv_path, newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            title = row["Title"]
            yt = YouTube(row["Link"])
            stream = yt.streams.filter(type="audio").first()
            audio_path = stream.download(output_path="output", filename=title)

            audio_file = music_tag.load_file(audio_path)
            audio_file["title"] = title
            audio_file["artist"] = row["Artist"]
            audio_file["genre"] = row["Genre"]
            audio_file.save()

            print(f"Track {title} downloaded")

    print("Done")


if __name__ == "__main__":
    main()
