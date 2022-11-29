import lbwb.GameMainLoop


def main():
    lbwb.GameMainLoop.GameMainLoop().get_to_mainloop()
#mac: /Users/osakana/Library/Application Support/KJTRGames/
if __name__ == "__main__":
    import sys, glob
    mods = glob.glob("./mods/*.pyz")
    for modname in mods:
        sys.path.append(modname)
    
    main()