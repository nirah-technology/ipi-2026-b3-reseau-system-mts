from winsound import Beep
from threading import Thread

class Note:
    def __init__(self, frequence: float, duration: float):
        self.frequence = frequence
        self.duration = duration

class Partition:
    def __init__(self, notes: list[Note]):
        self.notes = notes

class MusicInstrument(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.partition: Partition|None = None

    def run(self):
        for note in self.partition.notes:
            Beep(note.frequence, note.duration)


    def play_music_partition(self, partition: Partition):
        self.partition = partition
        self.start()


part_guitare = Partition([
    Note(443, 0.2),
    Note(657, 0.5),
    Note(550, 0.28),
])

part_violon = Partition([
    Note(657, 0.2),
    Note(550, 0.5),
    Note(443, 0.28),
])

guitare = MusicInstrument()
violon = MusicInstrument()

guitare.play_music_partition(part_guitare)
violon.play_music_partition(part_violon)
