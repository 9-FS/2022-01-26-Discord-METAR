# Copyright (c) 2023 구FS, all rights reserved. Subject to the CC BY-NC-SA 4.0 licence in `licence.md`.
if __name__=="__main__":
    import asyncio
    from KFSlog import KFSlog
    import logging
    import traceback
    from main import main


    KFSlog.setup_logging("", logging.INFO)
    #KFSlog.setup_logging("", logging.DEBUG, filepath_format="./log/%Y-%m-%dT%H_%M.log", rotate_filepath_when="M")

    try:
        asyncio.run(main())
    except:
        logging.critical(traceback.format_exc())
        print("\nPress enter to close program.", flush=True)
        input() # pause