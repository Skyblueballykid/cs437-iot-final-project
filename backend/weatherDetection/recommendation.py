from weatherDetection import weather

items = []

if weather["temp"] == "cold":
    items.append(["snow boots", "shovel", "gloves", "mittens", "scarves", "space heaters", "jackets", "parkas"])
if weather["temp"] == "chilly":
    items.append(["windbreaker", "boots", "skis", "ski poles", "snowboard", "gloves", "hats"])
if weather["temp"] == "room_temp":
    items.append(["golf driver", "boat", "windbreaker", "sweater", "fleece", "parashute", "fishing rod"])
if weather["temp"] == "warm":
    items.append(["golf driver", "tennis racquet", "running shoes", "flip flops", "sunscreen", "bikes", "fishing rod"])
if weather["temp"] == "hot":
    items.append(["sunscreen", "air conditioner", "fan", "flip flops", "bathing suit", "surfboard", "hats"])

if weather["image"] == "clear":
    items.append(["tennis racquet", "sneakers", "flip flops", "shirt", "shorts", "pants", "tennis racquet", "basketball"])
if weather["image"] == "cloudy":
    items.append(["sweaters", "sweatshirts", "fleece", "jacket", "book", "basketball", "tennis racquet"])
if weather["image"] == "rainy":
    items.append(["rain boots", "parka", "umbrella", "sweaters", "sweatshirts", "fleece", "raincoat", "book"])
if weather["image"] == "sunrise":
    items.append(["headlamp", "flashlight", "mosquito repellent", "sunglasses"])

if weather["humidity"] == "comfortable":
    items.append(["basketball", "tennis racquet", "golf driver", "surfboard", "sweaters", "rockclimbing gear", "tennis racquet", "basketball"])
if weather["humidity"] == "uncomfortable":
    items.append(["fan", "antiperspirant", "fleece", "dehumidifier", "water", "talcum powder", "air conditioning"])

if weather["winds"] == "none":
    items.append(["golf driver", "tennis", "swimsuit", "basketball", "golf drivers", "lacrosse racquet", "running shoes"])
if weather["winds"] == "light":
    items.append(["golf driver", "tennis", "surfboard", "sailing", "kite surfing", "windsurfing", "parasailing"])
if weather["winds"] == "moderate":
    items.append(["cars", "boats", "windbreaker", "running shoes", "kiteboarding equipment", "parashute", "fishing rod"])
if weather["winds"] == "strong":
    items.append(["kites", "flags", "windsurf boards", "coat"])

recommendations = set([item for sublist in items for item in sublist])
print(recommendations)