import os
def options(file):
    import wave
    import numpy as np
    import matplotlib.pyplot as plt
    import tkinter
    from scipy.io import wavfile
    from PIL import ImageTk, Image  
    from pydub import AudioSegment
    import librosa
    import customtkinter
    import sys
    sound = AudioSegment.from_file(file, format="wav")

    def originalwave():
        wav= wave.open(file,"r")
        raw=wav.readframes(-1)
        raw=np.frombuffer(raw,"int16")
        plt.title("The Original Wave")
        sampleRate=wav.getframerate()
        time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
        plt.plot(time,raw,color="blue")
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.show()

    def xshiftleft():
        sound= AudioSegment.from_wav(file)
        StartMin=1
        StartSec=16
        EndMin=2
        EndSec=16
        StartTime=StartMin*60*1000+StartSec*1000
        EndTime=EndMin*60*1000+EndSec*1000
        extract= sound[StartTime:EndTime]
        extract.export("shift left.wav",format="wav")
        wav= wave.open("shift left.wav","r")
        raw=wav.readframes(-1)
        raw=np.frombuffer(raw,"int16")
        orwav= wave.open(file,"r")
        orraw=orwav.readframes(-1)
        orraw=np.frombuffer(orraw,"int16")
        sampleRate=wav.getframerate()
        sampleRate2=orwav.getframerate()
        time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
        time2 = np.linspace(0, len(orraw)/sampleRate2, num=len(orraw))
        f, plots = plt.subplots(2, sharex=True)
        plots[0].set_title('Original Wave')
        plots[0].plot(time2,orraw,color="Blue")
        plots[1].set_title('shift left Wave')
        plots[1].plot(time,raw,color="Red")
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.show()

    def xshiftright():
        # create 5 sec of silence audio segment
        sec_segment = AudioSegment.silent(duration=5000)  #duration in milliseconds

        #read wav file to an audio segment
        song = AudioSegment.from_wav(file)

        #Add above two audio segments    
        final_song = sec_segment + song

        #Either save modified audio
        final_song.export("shift right.wav", format="wav")
        wav= wave.open("shift right.wav","r")
        raw=wav.readframes(-1)
        raw=np.frombuffer(raw,"int16")
        orwav= wave.open(file,"r")
        orraw=orwav.readframes(-1)
        orraw=np.frombuffer(orraw,"int16")
        sampleRate=wav.getframerate()
        sampleRate2=orwav.getframerate()
        time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
        time2 = np.linspace(0, len(orraw)/sampleRate2, num=len(orraw))
        f, plots = plt.subplots(2, sharex=True)
        plots[0].set_title('Original Wave')
        plots[0].plot(time2,orraw,color="Blue")
        plots[1].set_title('shift right Wave')
        plots[1].plot(time,raw,color="Red")
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.show()

    def low():
        customtkinter.set_default_color_theme("green")
        root=customtkinter.CTk()
        root.geometry("150x130")
        my_label=customtkinter.CTkLabel(root,text="Enter the speed",text_font=('calibre',10, 'bold'))
        my_label.pack(pady=5,padx=5)
        rate= customtkinter.CTkEntry(root)
        def P():
            wav= wave.open(file,"r")
            raw=wav.readframes(-1)
            raw=np.frombuffer(raw,"int16")
            rawh=raw-float(rate.get())
            sampleRate=wav.getframerate()
            time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
            f, plots = plt.subplots(2, sharex=True)
            plots[0].set_title('Original Wave')
            plots[0].plot(time,raw,color="Blue")
            plots[1].set_title('Low Wave')
            plots[1].plot(time,rawh,color="Red")
            plt.ylabel("Amplitude")
            plt.xlabel("Time")
            plt.show()
            # wavfile.write("low.wav",sampleRate,(rawh))
        btn5=customtkinter.CTkButton(root,text="Done",command=P)
        rate.pack(pady=5,padx=5)
        btn5.pack(pady=5,padx=5)
        root.mainloop()

    def high():
        customtkinter.set_default_color_theme("green")
        root=customtkinter.CTk()
        root.geometry("150x130")
        my_label=customtkinter.CTkLabel(root,text="Enter the speed",text_font=('calibre',10, 'bold'))
        my_label.pack(pady=5,padx=5)
        rate= customtkinter.CTkEntry(root)
        def P():
            wav= wave.open(file,"r")
            raw=wav.readframes(-1)
            raw=np.frombuffer(raw,"int16")
            rawh=raw+float(rate.get())
            sampleRate=wav.getframerate()
            time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
            f, plots = plt.subplots(2, sharex=True)
            plots[0].set_title('Original Wave')
            plots[0].plot(time,raw,color="Blue")
            plots[1].set_title('High Wave')
            plots[1].plot(time,rawh,color="Red")
            plt.ylabel("Amplitude")
            plt.xlabel("Time")
            plt.show()
            # wavfile.write("high.wav",sampleRate,(rawh))
        btn5=customtkinter.CTkButton(root,text="Done",command=P)
        rate.pack(pady=5,padx=5)
        btn5.pack(pady=5,padx=5)
        root.mainloop()

    def reflection():
        wav= wave.open(file,"r")
        raw=wav.readframes(-1)
        raw=np.frombuffer(raw,"int16")
        raw2 = raw[::-1]
        sampleRate=wav.getframerate()
        time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
        f, plots = plt.subplots(2, sharex=True)
        plots[0].set_title('Original Wave')
        plots[0].plot(time,raw,color="Blue")
        plots[1].set_title('Reversed Wave')
        plots[1].plot(time,raw2,color="Green")
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.show()
        wavfile.write("ref.wav",sampleRate,raw2)

    def speed(rate):
        #reload the audio to use librosa's expected format
        lr_speech_data, lr_speech_rate  = librosa.load(file)

        stretched = librosa.effects.time_stretch(lr_speech_data, rate)

        wavfile.write('Playback.wav', lr_speech_rate, stretched)
        f, plots = plt.subplots(2, sharex=True)
        plots[0].set_title('Original')
        plots[0].plot(np.arange(lr_speech_data.size)/lr_speech_rate, lr_speech_data)
        plots[1].set_title('Playback')
        plots[1].plot(np.arange(stretched.size)/lr_speech_rate, stretched)
        plt.show()
        
    def speed_change(sound, speed=1.0):
        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
        return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    def Expantion():
        customtkinter.set_default_color_theme("green")
        root=customtkinter.CTk()
        root.geometry("150x130")
        my_label=customtkinter.CTkLabel(root,text="Enter the speed",text_font=('calibre',10, 'bold'))
        my_label.pack(pady=5,padx=5)
        rate= customtkinter.CTkEntry(root)
        def P():
            sound = AudioSegment.from_file(file, format="wav")
            slow_sound = speed_change(sound, float(rate.get()))
            slow_sound.export("slow.wav", format="wav")
            wav= wave.open("slow.wav","r")
            raw=wav.readframes(-1)
            raw=np.frombuffer(raw,"int16")
            plt.title("The Expantion Wave")
            sampleRate=wav.getframerate()
            time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
            plt.plot(time,raw,color="blue")
            plt.ylabel("Amplitude")
            plt.xlabel("Time")
            plt.show()
        btn5=customtkinter.CTkButton(root,text="Done",command=P)
        rate.pack(pady=5,padx=5)
        btn5.pack(pady=5,padx=5)
        root.mainloop()

    def Compression():
        customtkinter.set_default_color_theme("green")
        root=customtkinter.CTk()
        root.geometry("150x130")
        my_label=customtkinter.CTkLabel(root,text="Enter the speed",text_font=('calibre',10, 'bold'))
        my_label.pack(pady=5,padx=5)
        rate= customtkinter.CTkEntry(root)
        def P():
            sound = AudioSegment.from_file(file, format="wav")
            fast_sound = speed_change(sound, float(rate.get()))
            fast_sound.export("fast.wav", format="wav")
            wav= wave.open("fast.wav","r")
            raw=wav.readframes(-1)
            raw=np.frombuffer(raw,"int16")
            plt.title("The Compression Wave")
            sampleRate=wav.getframerate()
            time = np.linspace(0, len(raw)/sampleRate, num=len(raw))
            plt.plot(time,raw,color="blue")
            plt.ylabel("Amplitude")
            plt.xlabel("Time")
            plt.show()
            
        btn5=customtkinter.CTkButton(root,text="Done",command=P)
        rate.pack(pady=5,padx=5)
        btn5.pack(pady=5,padx=5)
        root.mainloop()

    def playback():
        customtkinter.set_default_color_theme("green")
        root=customtkinter.CTk()
        root.geometry("150x130")
        my_label=customtkinter.CTkLabel(root,text="Enter the speed",text_font=('calibre',10, 'bold'))
        my_label.pack(pady=5,padx=5)
        rate= customtkinter.CTkEntry(root)
        def P():
            # root.quit()
            speed(float(rate.get())) 
        btn5=customtkinter.CTkButton(root,text="Done",command=P)
        rate.pack(pady=5,padx=5)
        btn5.pack(pady=5,padx=5)
        root.mainloop()

    def exit():
        sys.exit(0)


    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app=customtkinter.CTk()
    app.resizable(0,0)
    app.title('Signal Process')
    app.geometry('480x665')
    image1 = Image.open("logo.png")
    resized=image1.resize((400,170),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(resized)
    label1 = customtkinter.CTkLabel(image=test)
    label1.place(relx=0.5,y=20, anchor=tkinter.N)

    frame_1 = customtkinter.CTkFrame(master=app, width=300, height=400, corner_radius=15)
    frame_1.grid(row=0, column=0, padx=10, pady=190, sticky="nsew")

    btn1=customtkinter.CTkButton(master=frame_1,text="Original Wave", width=190, height=40,fg_color="#00bf75", hover_color="#01a365", command=originalwave,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn1.grid(row=1, column=0, padx=20, pady=20)

    btn2=customtkinter.CTkButton(master=frame_1,text="Shift up,y-axis", width=190, height=40,command=high,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn2.grid(row=2, column=0, padx=20, pady=20)

    btn3=customtkinter.CTkButton(master=frame_1,text="Shift down,y-axis", width=190, height=40,command=low,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn3.grid(row=3,column=0, padx=20, pady=20)

    btnn=customtkinter.CTkButton(master=frame_1,text="Shift left,x-axis", width=190, height=40,command=xshiftleft,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btnn.grid(row=4,column=0, padx=20, pady=20)

    btnnn=customtkinter.CTkButton(master=frame_1,text="Shift right,x-axis", width=190, height=40,command=xshiftright,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btnnn.grid(row=5,column=0, padx=20, pady=20)

    btn4=customtkinter.CTkButton(master=frame_1,text="Reflection", width=190, height=40,command=reflection,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn4.grid(row=1,column=1, padx=20, pady=20)

    btn5=customtkinter.CTkButton(master=frame_1,text="Expantion", width=190, height=40,command=Expantion,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn5.grid(row=2,column=1, padx=20, pady=20)

    btn6=customtkinter.CTkButton(master=frame_1,text="Compression", width=190, height=40,command=Compression,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn6.grid(row=3,column=1, padx=20, pady=20)

    btn7=customtkinter.CTkButton(master=frame_1,text="Playback Speed", width=190, height=40,command=playback,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    btn7.grid(row=4,column=1, padx=20, pady=20)

    out=customtkinter.CTkButton(master=frame_1,text="Exit", width=190, height=40, fg_color="#D35B58", hover_color="#C77C78",command=exit,text_color="#ffffff", text_font=('calibre',11, 'bold'))
    out.grid(row=5,column=1, padx=20, pady=20)

    customtkinter.CTkLabel(app,text=" © 2022 Signal Process \n By : Mazen Elnahla & Karim Elnady \n Presented to : Prof. Dr/Eslam Shalan",justify=LEFT).place(x=0,y=610)
    app.mainloop()
# Main window
from tkinter import *
from tkinter import filedialog
import customtkinter
import sys
def exit():
    sys.exit(0)

def talk():
    m=customtkinter.CTk()
    m.resizable(0,0)
    m.title('Web Search using voice')
    m.geometry('300x200')
    head=customtkinter.CTkLabel(m,text="Welcome to Voice Recognization")
    head.pack(pady=20)
    def mas():
        import speech_recognition as sr
        import webbrowser
        with sr.Microphone() as source:
            sr.Microphone()
            r = sr.Recognizer()
            r.energy_threshold = 5000
            print("Speak!")
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                label6=customtkinter.CTkLabel(m,text="You said : {}".format(text))
                label6.pack()
                url = 'https://www.google.com/search?q='
                search_url = url+text

                #webbrowser.open() open your default web browser with a given url.
                webbrowser.open(search_url)
            except:
                label2=customtkinter.CTkLabel(m,text="Can't Recognize")
                label2.pack()
                print("Can't Recognize")
    btn1=customtkinter.CTkButton(m,text="Speak",command=mas,width=120)
    btn1.pack(pady=10)
    m.mainloop()

def record():
    import threading
    import pyaudio
    import wave
    import customtkinter

    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    class rv():
        chunk = 1024 
        sample_format = pyaudio.paInt16 
        channels = 1
        fs = 44100  

        frames = []  
        def __init__(self, master):
            self.isrecording = False
            self.button1 = customtkinter.CTkButton(frame_1, text='Record',command=self.startrecording, text_font=('calibre',11, 'bold'))
            self.button2 = customtkinter.CTkButton(frame_1, text='Stop',command=self.stoprecording, text_font=('calibre',11, 'bold'))
            self.button1.grid(row=0,pady=20, padx=20)
            self.button2.grid(row=1,pady=20, padx=20)

        def startrecording(self):
            self.p = pyaudio.PyAudio()  
            self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
            self.isrecording = True

            print('Recording')
            t = threading.Thread(target=self.record)
            t.start()

        def stoprecording(self):
            self.isrecording = False
            print('recording complete')

            self.filename = "rec.wav"

            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            main.destroy()

        def record(self):

            while self.isrecording:
                data = self.stream.read(self.chunk)
                self.frames.append(data)


    main = customtkinter.CTk()
    main.title('recorder')
    main.geometry('240x250')
    frame_1 = customtkinter.CTkFrame(master=main, width=200, height=300, corner_radius=15)
    frame_1.grid(row=0, column=0,pady=50,padx=40, sticky="nsew")
    app = rv(main)
    main.mainloop()

window=customtkinter.CTk()
window.resizable(0,0)
window.title('Main Window')
window.geometry('500x280')
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
frame_1 = customtkinter.CTkFrame(master=window, width=300, height=400, corner_radius=15)
frame_1.grid(row=1, column=1, sticky="N")

def br():
    import wave
    filename = filedialog.askopenfilename(initialdir="/", title="Choose Mono Wav File", filetypes=[("wav Files", "*.wav")])
    window.destroy()
    wav = wave.open(filename, "r")
    if wav.getnchannels() == 2:
        print("Stereo Files are not supported. Use Mono Files")
        sys.exit(0)
    options(filename)

def txt():
    os.system('python txt_to_speach.py')
    
btn1=customtkinter.CTkButton(frame_1,text="Browse", width=190, height=40, command=br,text_color="#ffffff", text_font=('calibre',11, 'bold'))
btn1.grid(row=0, column=0, padx=20, pady=20, sticky="N")

rec=customtkinter.CTkButton(master=frame_1,text="Record", width=190, height=40,command=record,text_color="#ffffff", text_font=('calibre',11, 'bold'))
rec.grid(row=0,column=1, padx=20, pady=20)

btn7=customtkinter.CTkButton(master=frame_1,text="Speach Browser", width=190, height=40,command=talk,text_color="#ffffff", text_font=('calibre',11, 'bold'))
btn7.grid(row=1,column=0, padx=20, pady=20)


btn8=customtkinter.CTkButton(master=frame_1,text="Text To Speach", width=190, height=40,command=txt,text_color="#ffffff", text_font=('calibre',11, 'bold'))
btn8.grid(row=1,column=1, padx=20, pady=20)

out=customtkinter.CTkButton(frame_1,text="Exit",command=exit, width=200, height=40,fg_color="#D35B58", hover_color="#C77C78",text_color="#ffffff", text_font=('calibre',11, 'bold'))
out.grid(row=2,columnspan=2, padx=20, pady=20, sticky="N")
frame_1.pack(pady=20)
window.mainloop()