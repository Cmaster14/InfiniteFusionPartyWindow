from tkinter import *
import Paths


# Transparent window to display a party of up to 6 Pokemon, and allow their repositioning within the window
class PartyWindow:

    def __init__(self, party, orientation="vertical"):
        self.party = party
        self.orientationDimensions = {
            "vertical": [600, 900, 500, 15],
            "horizontal": [900, 600, 800, 35]
        }
        self.oriX = self.orientationDimensions[orientation][0]
        self.oriY = self.orientationDimensions[orientation][1]
        self.cutX = self.orientationDimensions[orientation][2]
        self.pad = self.orientationDimensions[orientation][3]
        self.canvas = Canvas(self.party, width=self.oriX, height=self.oriY)
        self.buttonCanvas = Canvas(self.party, width=self.oriX, height=100)
        self.imagePathList = []
        self.imageList = []
        self.imageButtonList = []
        self.buttonList = []
        self.coords = {}
        self.selectedButton = 0

    # Run setup sequence
    def setup(self):
        self.readPartyFile()
        self.setupImages()
        self.positionImages()
        self.setupButtons()

    # Read party file and image path file to add to imagePathList
    def readPartyFile(self):
        keep = []
        with open(Paths.partyFile, 'r') as f:
            partyList = f.read().splitlines()
            for poke in partyList:
                if "B" in poke:
                    scrambledImage = poke.replace("B", "").split("H")
                    mon = scrambledImage[1] + "." + scrambledImage[0]
                else:
                    mon = poke

                imagePath = self.getImagePath(mon)
                if imagePath:
                    self.imagePathList.append("../" + imagePath)
                    keep.append(imagePath)

        with open(Paths.pathFile, 'w') as w:
            for path in keep:
                w.write(path + "\n")

    # Create image objects and add them to working lists
    def setupImages(self):
        for im in self.imagePathList:
            self.imageList.append(PhotoImage(file=im).subsample(3, 3).zoom(2, 2))
            self.imageButtonList.append(PhotoImage(file=im).subsample(5, 5))

    # Get image path
    def getImagePath(self, mon):
        with open(Paths.pathFile, 'r') as r:
            alts = r.read().splitlines()
        alts.reverse()
        for a in alts:
            if mon in a:
                return a
        return False

    # Positioning the Images inside the canvas
    def positionImages(self):
        imgX = 50
        yStart = 20
        for index, image in enumerate(self.imageList, start=1):
            imgX += image.width() / 2
            if imgX >= self.cutX:
                imgX = image.width() / 2 + 50
                yStart += 300
            imgY = yStart + image.height() / 2
            if self.coords and not len(self.coords) < index:
                self.canvas.create_image(
                    self.coords[str(index)][0], self.coords[str(index)][1],
                    anchor="center", image=image, tag="mon" + str(index))
            else:
                self.canvas.create_image(imgX, imgY, anchor="center", image=image, tag="mon" + str(index))
                self.coords[str(index)] = [imgX, imgY]
            imgX += image.width()
        self.canvas.pack()

    # Create the buttons that allow repositioning of the party Pokemon within the window
    def setupButtons(self):
        buttonListLength = len(self.imageButtonList)
        if buttonListLength >= 1:
            activate1 = Button(self.buttonCanvas, image=self.imageButtonList[0], background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.activate1.configure(self.bindMon(str(1))))
            self.buttonList.append(activate1)
            self.buttonCanvas.activate1 = activate1

        if buttonListLength >= 2:
            activate2 = Button(self.buttonCanvas, image=self.imageButtonList[1], background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.activate2.configure(self.bindMon(str(2))))
            self.buttonList.append(activate2)
            self.buttonCanvas.activate2 = activate2

        if buttonListLength >= 3:
            activate3 = Button(self.buttonCanvas, image=self.imageButtonList[2], background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.activate3.configure(self.bindMon(str(3))))
            self.buttonList.append(activate3)
            self.buttonCanvas.activate3 = activate3

        if buttonListLength >= 4:
            activate4 = Button(self.buttonCanvas, image=self.imageButtonList[3], background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.activate4.configure(self.bindMon(str(4))))
            self.buttonList.append(activate4)
            self.buttonCanvas.activate4 = activate4

        if buttonListLength >= 5:
            activate5 = Button(self.buttonCanvas, image=self.imageButtonList[4], background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.activate5.configure(self.bindMon(str(5))))
            self.buttonList.append(activate5)
            self.buttonCanvas.activate5 = activate5

        if buttonListLength >= 6:
            activate6 = Button(self.buttonCanvas, image=self.imageButtonList[5], background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.activate6.configure(self.bindMon(str(6))))
            self.buttonList.append(activate6)
            self.buttonCanvas.activate6 = activate6

        for button in self.buttonList:
            button.pack(side=LEFT, ipadx=self.pad)

        reload = Button(self.buttonCanvas, text="Reload", background="#ffffff",
                           command=lambda root=self.buttonCanvas: root.reload.configure(self.reload(0)))
        self.buttonList.append(reload)
        reload.pack(side=LEFT, ipadx=15, ipady=19)
        self.buttonCanvas.reload = reload
        self.party.bind("r", self.reload)

        for i in range(1, buttonListLength+1):
            self.party.bind(str(i), self.keyPress)

        self.buttonCanvas.pack()

    # Allow buttons to be activated by 1-6 key press as well
    def keyPress(self, b):
        self.bindMon(b.char)

    # Update the coordinates of the selected Pokemon image and store for subsequent reloads
    def setCoords(self, e, mon):
        self.canvas.coords(mon, e.x, e.y)
        self.coords[mon[-1]] = [e.x, e.y]

    # Bind Mouse 1 click (and hold) to selected Pokemon image to allow for moving within the window
    def bindMon(self, mon):
        if int(mon) == self.selectedButton:
            self.canvas.unbind("<B1-Motion>")
            self.updateImageColors(-1)
            self.selectedButton = 0
        else:
            self.canvas.bind("<B1-Motion>", lambda e: self.setCoords(e, "mon" + mon))
            self.updateImageColors(int(mon)-1)
            self.selectedButton = int(mon)

    # Change background color of buttons to indicate which Pokemon is selected
    def updateImageColors(self, index):
        for i, button in enumerate(self.buttonList):
            if i == index:
                button.config(background="#206e10")
            else:
                button.config(background="#ffffff")

    # Recreates the canvases for images and buttons, then re-runs setup
    def reload(self, e):
        self.canvas.destroy()
        self.canvas = Canvas(self.party, width=self.oriX, height=self.oriY)
        self.buttonCanvas.destroy()
        self.buttonCanvas = Canvas(self.party, width=self.oriX, height=100)
        self.imagePathList = []
        self.imageList = []
        self.imageButtonList = []
        self.buttonList = []
        self.selectedButton = 0
        self.setup()


orientation = "vertical"
horizontalOptions = ["horizontal", "h", "horiz", "side", "flat", "trios", "thicc", "small"]
with open(Paths.orientationFile, 'r') as f:
    lines = f.readlines()
    if lines[0].strip() in horizontalOptions:
        orientation = "horizontal"
partyWindow = PartyWindow(party=Tk(), orientation=orientation)
partyWindow.party.attributes('-transparentcolor', '#f0f0f0')
partyWindow.party.title('Party')
partyWindow.setup()


# Starts the GUI
partyWindow.party.mainloop()
