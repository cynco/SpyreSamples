# Create a WebApp using Spyre
# This example is from http://cgerson.github.io/Spyre/

# pip install dataspyre

# To launch this app:
# On the command line (in the app's directory), type
# python [insert filename ending in .py]
# Open your browser and go to localhost:8000. (typically http://127.0.0.1:8000) 
# App's up!

# Import the module

from spyre import server

# Create the App class

class SimpleApp(server.App): #inherits the server.App class

# Give our app a title
    title = "My Spyre Example"

# Inside your class, define your inputs dictionary

    inputs =     [{ "type":"text",
                  "key":"words",
                  "label":"write words here",
                  "value":"hello world",
                  "action_id":"update_data"}]

# "type" is to specify the input format. this is a textbox
# "key" is the variable name to refer to the value
# "label" is the label for the textbox (optional)
# "value" is the initial value in the textbox
# "action_id" tells Spyre what to do when value is entered

# Inside your class, define your outputs dictionary

    #outputs =   [{"type":"html","id":"update_data"}]
    
#tells Spyre to use getHTML file to generate output

    tabs = ["Text","Plot","Table"] #this creates the tabs. names should not have spaces here

    controls = [{"control_type" : "hidden", "control_id" : "update_data"}]

#name of control_id doesn't matter, as long it matches the outputs

    outputs = [{"output_type":"html",
                "output_id":"html",
                "control_id" : "update_data",
                "tab" : "Text"},
               {"output_type" : "plot",
                "output_id" : "plot",
                "control_id" : "update_data",
                "tab" : "Plot"},
               {"output_type" : "table",
                "output_id" : "table",
                "control_id" : "update_data",
                "tab" : "Table"}]
    
#                    "output_id" : "update_data",
#                "control_id" : "submit_plot",

#tells Spyre to use getData file to generate output
#matches 'controls' control_id above
#match our tab name
#tells Spyre to use getPlot file to generate output
#needs unique id
#matches 'controls' control_id above
#match our tab name



# Override the getHTML method

    def getHTML(self, params):
            words = params["words"]
            return "Here's what you wrote in the textbox: <b>%s</b>" % words 
        #return a string

#argument params allows you to access inputs
#params is a dictionary. grab value entered in textbox with the key 'words'

# Launch

if __name__ == '__main__':
     app = SimpleApp()
     app.launch(port=8000) #or the port of your choice
