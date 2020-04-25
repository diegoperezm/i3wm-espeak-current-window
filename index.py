from i3ipc.aio import Connection
from i3ipc import Event
import asyncio
from espeak import espeak

rate = 1
vol   = 2
pitch = 3
rangE = 4
punctuation = 5
capitals = 6
wordgap = 7

# espeak default
espeak.set_parameter(rate, 200)
espeak.set_parameter(vol, 200)
espeak.set_parameter(pitch, 30)
espeak.set_parameter(wordgap, 30)

# mbrola
#espeak.set_voice('mb-en1')
#espeak.set_parameter(rate, 180)
#espeak.set_parameter(vol, 200)
#espeak.set_parameter(pitch, 30)
##espeak.set_parameter(rangE, 30)
#espeak.set_parameter(wordgap, 10)

async def main():
    def on_window(self, e):
        window_class =  e.ipc_data["container"]["window_properties"]["class"]
        window_title =   e.ipc_data["container"]["window_properties"]["title"]
       
        if type == 'Emacs': 
         espeak.synth(window_class)
         espeak.synth('emacs')
         
        else: 
         espeak.synth(window_class)
         espeak.synth(window_title)
        

    c = await Connection(auto_reconnect=True).connect()

    workspaces = await c.get_workspaces()

    c.on(Event.WINDOW_FOCUS, on_window)

    await c.main()

asyncio.get_event_loop().run_until_complete(main()) 

