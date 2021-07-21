import gradio as gr 


def predict(inp):
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

# allow_flagging and allow_screenshot set to false
# modifying css via css parameter
# set layout to vertical, but can remove this to keep it horizontal.
iface = gr.Interface(predict, "image", "text", examples=examples, allow_flagging=False, allow_screenshot=False,
					 layout="vertical", css=css)

iface.launch(private_endpoint="https://trueimage.app/") 

