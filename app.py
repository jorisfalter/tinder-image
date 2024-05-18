import replicate

input_image = open("joris.jpeg", "rb");
input_image2 = open("joris2.jpeg", "rb");
input_image3 = open("joris3.jpeg", "rb");
input_image4 = open("joris4.jpeg", "rb");



input = {
    "prompt": "A man img with a enthusiastic happy spark in his eyes, looks into the camera, wears a shirt, narrow face,  perfect skin, white background",
    "num_steps": 50,
    "input_image": input_image,
    "input_image2": input_image2,
    "input_image2": input_image3,
    "input_image2": input_image4,
    "guidance_scale": 5,
    "style_strength_ratio": 20,
    "style_name": "Photographic (Default)",
    "negative_prompt": "big teeth, tired, nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"
}

output = replicate.run(
    "tencentarc/photomaker:ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4",
    input=input
)
print(output)
#=> ["https://replicate.delivery/pbxt/WPelbpCPIDTmIiye4CGXbQP...