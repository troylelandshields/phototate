# A very simple program. Drag photos into boxes and click rotate.


""" This is for rotating photos in batch. """

# Import wx.Python
import wx
import Image

# Declare GUI Constants
MENU_FILE_EXIT = wx.NewId()
DRAG_SOURCE    = wx.NewId()

# Define File Drop Target class
class FileDropTarget(wx.FileDropTarget):
   """ This object implements Drop Target functionality for Files """
   def __init__(self, obj):
      """ Initialize the Drop Target, passing in the Object Reference to
          indicate what should receive the dropped files """
      # Initialize the wxFileDropTarget Object
      wx.FileDropTarget.__init__(self)
      # Store the Object Reference for dropped files
      self.obj = obj

   def OnDropFiles(self, x, y, filenames):
      """ Implement File Drop """
      # For Demo purposes, this function appends a list of the files dropped at the end of the widget's text
      # Move Insertion Point to the end of the widget's text
      self.obj.SetInsertionPointEnd()
      # append a list of the file names dropped

      for file in filenames:
         self.obj.WriteText(file + '\n')



class MainWindow(wx.Frame):
   """ This window displays the GUI Widgets. """
   def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent, wx.ID_ANY, title, size = (710,350), style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
		self.SetBackgroundColour(wx.WHITE)

		# Menu Bar
		# Create a MenuBar
		menuBar = wx.MenuBar()
		# Build a Menu Object to go into the Menu Bar
		menu1 = wx.Menu()
		menu1.Append(MENU_FILE_EXIT, "E&xit", "Quit Application")
		# Place the Menu Item in the Menu Bar
		menuBar.Append(menu1, "&File")
		# Place the Menu Bar on the ap
		self.SetMenuBar(menuBar)
		#Define Events for the Menu Items
		wx.EVT_MENU(self, MENU_FILE_EXIT, self.CloseWindow)

		# GUI Widgets
		# Define a Text Control from which Text can be dragged for dropping
		# Label the control

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		grid = wx.GridBagSizer(hgap=5, vgap=5)

		# Define a Text Control to receive Dropped Files
		# Label the control
		lbl1 = wx.StaticText(self, -1, "90 CW", (50, 30))
		# Create a read-only Text Control
		self.text1 = wx.TextCtrl(self, -1, "", pos=(50, 50), size=(200,235), style = wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
		# Make this control a File Drop Target
		# Create a File Drop Target object
		dt1 = FileDropTarget(self.text1)
		# Link the Drop Target Object to the Text Control
		self.text1.SetDropTarget(dt1)

		lbl2 = wx.StaticText(self, -1, "180", (255, 30))
		# Create a read-only Text Control
		self.text2 = wx.TextCtrl(self, -1, "", pos=(255, 50), size=(200,235), style = wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
		# Make this control a File Drop Target
		# Create a File Drop Target object
		dt2 = FileDropTarget(self.text2)
		# Link the Drop Target Object to the Text Control
		self.text2.SetDropTarget(dt2)

		lbl3 = wx.StaticText(self, -1, "270 CW", (460, 30))
		# Create a read-only Text Control
		self.text3 = wx.TextCtrl(self, -1, "", pos=(460, 50), size=(200,235), style = wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
		# Make this control a File Drop Target
		# Create a File Drop Target object
		dt3 = FileDropTarget(self.text3)
		# Link the Drop Target Object to the Text Control
		self.text3.SetDropTarget(dt3)

		self.processBtn = wx.Button(self, label="Process", pos=(300, 300))
		self.Bind(wx.EVT_BUTTON, self.OnProcess, self.processBtn)

		grid.Add(lbl1, pos=(0,0))
		grid.Add(self.text1, pos=(1,0))
		grid.Add(lbl2, pos=(0,1))
		grid.Add(self.text2, pos=(1,1))
		grid.Add(lbl3, pos=(0,2))
		grid.Add(self.text3, pos=(1,2))
		
		mainSizer.Add(grid, 1, wx.ALL|wx.EXPAND, 5)
		mainSizer.Add(self.processBtn, 0, wx.CENTER)
		self.SetSizerAndFit(mainSizer)

		# Display the Window
		self.Show(True)

	   
	   
   def CloseWindow(self, event):
       """ Close the Window """
       self.Close()

   def OnDragInit(self, event):
       """ Begin a Drag Operation """
       # Create a Text Data Object, which holds the text that is to be dragged
       tdo = wx.PyTextDataObject(self.text.GetStringSelection())
       # Create a Drop Source Object, which enables the Drag operation
       tds = wx.DropSource(self.text)
       # Associate the Data to be dragged with the Drop Source Object
       tds.SetData(tdo)
       # Initiate the Drag Operation
       tds.DoDragDrop(True)

   def OnProcess(self,e):
      #get list of 90 degree files.
      #for file in filenames:
      self.RotateFiles(self.text1, 270)
      self.RotateFiles(self.text2, 180)
      self.RotateFiles(self.text3, 90)
      self.text1.Clear()
      self.text2.Clear()
      self.text3.Clear()
      
   def RotateFiles(self, textBx, degree):
      str = textBx.GetValue()
      list = str.splitlines()
      for file in list:
      	img = Image.open(file)
      	rotated = img.rotate(degree)
      	rotated.save(file)
      
        	
class MyApp(wx.App):
   """ Define the Drag and Drop Example Application """
   def OnInit(self):
      """ Initialize the Application """
      # Declare the Main Application Window
      frame = MainWindow(None, -1, "Rotate Photos")
      # Show the Application as the top window
      self.SetTopWindow(frame)
      return True


# Declare the Application and start the Main Loop
app = MyApp(0)
app.MainLoop()