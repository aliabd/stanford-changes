import gradio as gr 


def predict(inp):
	return "Looks good" 

examples = [["logo.png"]]

css = """
.input_image .edit_button {
	visibility: hidden; # hides edit button
}

.flag {
	visibility: hidden; # hides flag button 
}

.input_image {
	height: 50rem !important; # increases image size on screen, you can fine tune
}

.output_text {
	font-size: 2rem; # increases output text size 
}
"""


# auth just checks if username field isn't empty, password can be empty
def auth(username, password):
	return len(username) > 0


auth_message = "Welcome to the True Image interface! Please log in below."


# allow_screenshot set to false
# allow_flagging set to auto - every prediction will be saved at the source directory (where interface was launched)
# modifying css via css parameter
# set layout to vertical, but can remove this to keep it horizontal.
iface = gr.Interface(predict, "image", "text", examples=examples, allow_flagging='auto', allow_screenshot=False,
					 layout="vertical", css=css)

# auth=auth
# auth_message is optional, displays text on html log in page
iface.launch(private_endpoint="https://trueimage.app/", auth=auth, auth_message=auth_message)

