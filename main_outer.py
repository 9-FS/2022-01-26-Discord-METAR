import asyncio
import KFS.log
import traceback    #Exceptionnachricht vollständig wenn Programm als .exe abschmiert
from main import main


try:
    asyncio.run(main())
except:
    KFS.log.write(traceback.format_exc())
    
    print("\n\nPress enter to close program.")
    input() #pause