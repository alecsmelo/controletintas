from cx_Freeze import setup, Executable
setup(
    name = "Controle Tintas",
    version = "1.6.0",
    author = "Alecsandro Ferreira Melo",
    options = {"build_exe": {
        'packages': ["sqlite3","tkinter"],
        'include_files': ['img/iconefinal.ico','EstoqueTintas.db','img/C_ink.png','img/C_ink80.png','img/C_ink50.png','img/C_ink20.png','img/M_ink.png','img/M_ink80.png','img/M_ink50.png','img/M_ink20.png','img/Y_ink.png','img/Y_ink80.png','img/Y_ink50.png','img/Y_ink20.png','img/K_ink.png','img/K_ink80.png','img/K_ink50.png','img/K_ink20.png'],
        'include_msvcr': True,
    }},
    executables = [Executable("ControleTintas.py",base="Win32GUI", icon="img/iconefinal.ico")]
    )
