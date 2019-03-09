import pygame


class SoundSupervisor:
    """Handles the playing of sound over pygame mixer"""
    def __init__(self, audio_files, keys=None, channel=0, volume=None):
        self.audio_files = audio_files
        self.audio = {}
        self.channel = pygame.mixer.Channel(channel)
        if not keys:
            for s_file in audio_files:
                self.audio[s_file] = pygame.mixer.Sound('sounds/' + s_file)
        else:
            if len(keys) != len(audio_files):
                raise ValueError('number of keys must be the same as the number of sound files')
            for key, s_file in zip(keys, audio_files):
                self.audio[key] = pygame.mixer.Sound('sounds/' + s_file)
        if isinstance(volume, float):
            self.channel.set_volume(volume)

    def play(self, key):
        """Play a sound once"""
        self.channel.play(self.audio[key], loops=0)

    def play_loop(self, key):
        """Loop a sound indefinitely"""
        self.channel.play(self.audio[key], loops=-1)

    def stop(self):
        """Stop sound from playing"""
        self.channel.stop()