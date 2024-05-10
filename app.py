import replicate



output = replicate.run(
    "tencentarc/photomaker:ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4",
    input={
        "prompt": "A photo of a scientist img receiving the Nobel Prize",
        "num_steps": 50,
        "style_name": "Photographic (Default)",
        "input_image": "https://replicate.delivery/pbxt/KFkSv1oX0v3e7GnOrmzULGqCA8222pC6FI2EKcfuCZWxvHN3/newton_0.jpg",
        "num_outputs": 1,
        "guidance_scale": 5,
        "negative_prompt": "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
        "style_strength_ratio": 20
    }
)
print(output)