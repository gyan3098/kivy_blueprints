from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.config import Config
Config.set('graphics','width','600')
Config.set('graphics','height','900')
from jnius import autoclass
# from kivy.logger import Logger

Environment = autoclass("android.os.Environment")
MediaRecorder = autoclass('android.media.MediaRecorder')
AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')
path = Environment.getExternalStorageDirectory().getAbsolutePath()
# Logger.info('App: storage path == "%s" ' %path)



storage_path = (path + "/kivy_recording.3gp")

recorder = MediaRecorder()

MediaPlayer = autoclass('android.media,MediaPlayer')
player = MediaPlayer()



def reset_player():
    if(player.isPlaying()):
        player.stop()

    player.reset()


def restart_player():
    reset_player()
    try:
        player.setDataSource(storage_path)
        player.prepare()
        player.start()

    except:
        player.reset()

def init_recorder():
    recorder.setAudioSource(AudioSource.MIC)
    recorder.setOutputFormat(OutputFormat.THREE_GPP)
    recorder.setAudioEncoder(AudioEncoder.AMR_NB)
    recorder.setOutputFile(storage_path)
    recorder.prepare()


class Tiles(GridLayout):
    pass

File = autoclass('java.io.file')

class RecorderApp(App):
    is_recording = False

    def delete_file(self):
        reset_player()
        File(storage_path).delete()

    def begin_playback(self):
        restart_player()

    def begin_end_recording(self):
        if (self.is_recording):
            recorder.stop()
            recorder.reset()
            self.is_recording = False
            self.root.ids.begin_end_recording.text = ('[font=Modern Pictograms][size=80]"e"[/size][/font]\nBegin recording')
            return

        init_recorder()
        recorder.start()
        self.is_recording = True
        self.root.ids.begin_end_recording.text = ('[font=Modern Pictograms][size=80]"e"[/size][/font]\nBegin recording')



if __name__=="__main__":
    LabelBase.register(name="Modern Pictograms",fn_regular="modernpics.ttf")
    RecorderApp().run()

