import gradio as gr 


def predict(inp, hospital):
	return "Looks good" 

examples = [["logo.png"]]

css = """
.input_image .edit_button {
	visibility: hidden; # hides edit button
}

.input_image {
	height: 50rem !important; # increases image size on screen, you can fine tune
}

.output_text {
	font-size: 2rem; # increases output text size 
}
"""

auth = [("user-1", "password-1"), ("user-2", "password-2")]
auth_message = "Welcome to the True Image interface! Please log in below."

dropdown = gr.inputs.Dropdown(["Hostpial 1", "Hospital 2", "None"], default="None",	 label="Hospital")


# allow_flagging and allow_screenshot set to false
# modifying css via css parameter
# set layout to vertical, but can remove this to keep it horizontal.
iface = gr.Interface(predict, ["image", dropdown], "text", examples=examples, allow_flagging=False, allow_screenshot=False,
					 layout="vertical", css=css)

# auth=auth for the two users
# auth_message is optional, displays text on html log in page
iface.launch(private_endpoint="https://trueimage.app/", auth=auth, auth_message=auth_message)

