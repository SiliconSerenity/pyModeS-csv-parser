from web_listener import WebListener

# Define a handler function
def data_received_handler(data):
    # Write your code that does stuff with the data here!
    print(data) #for example, simply print the data to the console

# Create a new WebListener
wl = WebListener(port=5000)
# Subscribe the handler
wl.subscribe(data_received_handler)
