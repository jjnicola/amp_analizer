import os, signal, sys
from .play_rec import PlayRec
from .analyzer import Analyzer
from .sample_generator import create_audio_sample


import argparse
class CliParser:
    def __init__(self) -> None:
        """Create a command-line arguments parser."""
        parser = argparse.ArgumentParser(description=None)

        parser.add_argument(
            '--analyzer-only', action='store_true', help='Performer an analysis over the audio file without running the profiler.'
        )

        parser.add_argument(
            '--generate-audio-sample', action='store_true', help='Generates an audio which increase the frecuency.'
        )
                
        self.parser = parser

    def parse_known_args(self):
        return self.parser.parse_args()

def play_and_rec():
    """Forks 2 process to play an audio file and to record the mic."""
    p = PlayRec()
    rec_proc = os.fork()
    if rec_proc == 0:
        signal.signal(signal.SIGINT, p.signal_handler)
        p.record_audio()
    elif rec_proc < 0:
        print ("ERROR FORKING THE RECORDER")
        return
    
    play_proc = os.fork ()
    if play_proc == 0:
        p.play_audio_sample()
    elif play_proc < 0:
        print ("ERROR FORKING THE PLAYER")
        return
   
    print ("Waiting in the parent process for the player to finish")
    os.waitpid(play_proc, 0)
   
    os.kill(rec_proc, signal.SIGINT)
    os.waitpid(rec_proc, 0)

def analyze():
    """ Load an audio file an perform an FFT. Then plots the output. """
    a = Analyzer()
    a.plot_2()

def main():
    parser = CliParser()
    args = parser.parse_known_args()
    
    
    if args.generate_audio_sample == True:
        create_audio_sample()

    if args.analyzer_only == False:
        play_and_rec()
    analyze()

  
if __name__ == "__main__":
    main()
